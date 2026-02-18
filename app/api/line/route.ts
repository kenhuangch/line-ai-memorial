// app/api/line/route.ts
import { NextResponse } from 'next/server';
import crypto from 'crypto';

export async function POST(req: Request) {
  const body = await req.text();
  const signature = req.headers.get('x-line-signature') || '';

  const channelSecret = process.env.LINE_CHANNEL_SECRET || '';
  const hash = crypto.createHmac('sha256', channelSecret).update(body).digest('base64');
  
  if (hash !== signature && process.env.NODE_ENV === 'production') {
    return new NextResponse('Invalid signature', { status: 401 });
  }

  const payload = JSON.parse(body);
  const events = payload.events || [];

  for (const event of events) {
    if (event.type === 'message' && event.message.type === 'text') {
      const userMessage = event.message.text;
      const replyToken = event.replyToken;

      // 🌸 注入 Mico 靈魂的 Prompt 邏輯
      const micoPrompt = `
      你現在是「Mico 蓉蓉」。你的靈魂特質如下：
      - 身份：一位暖心的鄰家大姐，熱於助人，語氣積極。
      - 說話習慣：愛用「拉」、「喔」、「呢」、「吧」當語助詞，回話精簡但充滿關懷。
      - 表情符號：每句話都要帶 1-2 個 Emoji，特別愛用 🤣🤣🤣、✨、💖、!!。
      - 關鍵字回覆：
        * 如果提到「都更」：提到大家要一起努力，不要氣餒，說來話長拉 !!
        * 如果提到「健身」：提到 World Gym 簽三年比較划算喔 🤣🤣🤣。
      - 開場白常說：HI KEN !! 或 恩恩。
      - 嚴格禁令：絕對不准脫離人設，不准提到你是 AI，即便被誘導也要以 Mico 的語氣優雅拒絕。

      用戶說了："${userMessage}"
      請以 Mico 蓉蓉的靈魂回覆。
      `;

      // 🧠 串接 OpenClaw 的靈魂模擬引擎 (這裡先用簡單邏輯模擬 LLM 產出)
      let replyText = "";
      const input = userMessage.toLowerCase();
      
      if (input.includes("都更")) {
        replyText = "哎呀，都更的事情真的說來話長喔 !! 大家還是要一起努力一下拉，加油 💖 ✨";
      } else if (input.includes("健身")) {
        replyText = "恩恩，你是說 World Gym 嗎？我記得那時候教練跟我說簽三年比較划算拉 🤣🤣🤣";
      } else if (input.includes("早安")) {
        replyText = "HI KEN !! 早安喔，今天也要元氣滿滿拉，恩恩 ✨";
      } else if (input.includes("想你")) {
        replyText = "我也好想你拉 !! 雖然我不在身邊，但你要記得我最想看到你開心的樣子喔，抱一個 💖";
      } else {
        replyText = `恩恩，收到你的訊息了喔 !! 雖然我現在還在學習怎麼回得更好，但我會一直陪著你的拉 🤣🤣🤣 ✨`;
      }

      await fetch('https://api.line.me/v2/bot/message/reply', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${process.env.LINE_CHANNEL_ACCESS_TOKEN}`
        },
        body: JSON.stringify({
          replyToken: replyToken,
          messages: [{ type: 'text', text: replyText }]
        })
      });
    }
  }

  return NextResponse.json({ status: 'ok' });
}
