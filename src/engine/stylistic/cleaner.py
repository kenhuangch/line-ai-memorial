import re
import json
import os

class LineTextCleaner:
    """
    Cleans LINE .txt export files for AI stylistic analysis.
    Supports the format: [Time]\t[Name]\t[Message]
    Example: 下午10:22	Ken Huang	[貼圖]
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def clean(self):
        cleaned_data = []
        # Support optional AM/PM prefix and tab-separated fields
        line_pattern = re.compile(r'^([上下]午\d{2}:\d{2})\t(.*?)\t(.*)$')
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                        
                    match = line_pattern.match(line)
                    if match:
                        timestamp, name, message = match.groups()
                        
                        # Data Cleaning: Filter out non-textual content
                        if "[貼圖]" in message or "[照片]" in message or "[影片]" in message or "[檔案]" in message:
                            continue
                        if "☎ 通話時間" in message or "☎ 未接來電" in message or "☎ 您已取消通話" in message:
                            continue
                        if "您已收回訊息" in message:
                            continue
                        if "轉帳給" in message or "您已收到NT$" in message:
                            continue
                        if message.startswith("http"):
                            continue
                            
                        # Remove quotes often added by LINE for multiline or special chars
                        message = message.strip('"')
                        
                        cleaned_data.append({
                            "name": name,
                            "text": message,
                            "time": timestamp
                        })
        except Exception as e:
            print(f"Error reading file: {e}")
            
        return cleaned_data

    def get_stylistic_stats(self, target_name):
        data = self.clean()
        user_data = [d for d in data if d['name'] == target_name]
        
        stats = {
            "total_messages": len(user_data),
            "common_particles": [],
            "emoji_usage": 0,
            "avg_length": 0
        }
        
        if not user_data:
            return stats
            
        particles = ["拉", "喔", "恩恩", "哈", "呀", "呢", "吧", "咩"]
        found_particles = {}
        total_len = 0
        emoji_count = 0
        
        for d in user_data:
            text = d['text']
            total_len += len(text)
            # Simple emoji detection (basic)
            emoji_count += len(re.findall(r'[^\x00-\x7F]+', text))
            
            for p in particles:
                if p in text:
                    found_particles[p] = found_particles.get(p, 0) + 1
        
        stats["avg_length"] = round(total_len / len(user_data), 2)
        stats["common_particles"] = sorted(found_particles.items(), key=lambda x: x[1], reverse=True)
        stats["emoji_usage_density"] = round(emoji_count / len(user_data), 2)
        
        return stats

if __name__ == "__main__":
    # Test with provided file if exists
    input_file = "/Users/framelab/.openclaw/media/inbound/file_2---28a7333c-db0a-4985-a642-9e7800db28b6.txt"
    if os.path.exists(input_file):
        cleaner = LineTextCleaner(input_file)
        # Extract target stats for Mico
        target = "❤️Mico🐑蓉蓉🎊🏠🌿💰🌸"
        stats = cleaner.get_stylistic_stats(target)
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        
        # Save cleaned data for RAG engine
        cleaned_data = cleaner.clean()
        output_json = "/Users/framelab/.openclaw/workspace/line-ai-memorial/data/cleaned_chat.json"
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
        print(f"Cleaned data saved to {output_json}")
