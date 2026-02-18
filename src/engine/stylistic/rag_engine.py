import json
import os

class MicoPersonaEngine:
    """
    Simulates Mico's persona based on extracted stylistic data and chat history.
    Uses basic RAG logic (simulated for now) to provide context-aware responses.
    """
    def __init__(self, cleaned_data_path):
        with open(cleaned_data_path, 'r', encoding='utf-8') as f:
            self.history = json.load(f)
        
        # Stylistic traits derived from analysis
        self.traits = {
            "particles": ["拉", "吧", "喔", "呢"],
            "emojis": ["🤣🤣🤣", "!!", "✨", "💖"],
            "openings": ["HI KEN", "恩恩", "好喔"]
        }

    def find_relevant_context(self, query):
        """
        Simple keyword-based context lookup (RAG skeleton).
        """
        keywords = ["都更", "健身", "世界健身", "World Gym", "停車", "發票"]
        found_context = []
        for msg in self.history:
            for kw in keywords:
                if kw in msg['text'] and kw in query:
                    found_context.append(msg['text'])
        return list(set(found_context))[:3] # Return top 3 unique matches

    def generate_response(self, user_input):
        """
        Generates a Mico-style response.
        Note: In production, this would be a prompt to an LLM like Claude.
        """
        context = self.find_relevant_context(user_input)
        
        # Simulated LLM Prompt logic:
        # "You are Mico, a warm 'big sister' type neighbor. Use particles like '拉', '喔'. 
        # End with '🤣🤣🤣'. Reference context: {context}"
        
        if "健身" in user_input:
            return f"恩恩，你是說 World Gym 嗎？我記得那時候教練跟我說簽三年比較划算拉 🤣🤣🤣"
        
        if "都更" in user_input:
            return f"哎呀，都更的事情真的說來話長喔 !! 大家還是要一起努力一下拉，加油 💖"

        return f"HI KEN !! 收到你的訊息了喔，我會再幫你想想看拉，恩恩 ✨"

if __name__ == "__main__":
    engine = MicoPersonaEngine("/Users/framelab/.openclaw/workspace/line-ai-memorial/data/cleaned_chat.json")
    print(f"Mico test (Gym): {engine.generate_response('你覺得健身房報名好嗎')}")
    print(f"Mico test (Default): {engine.generate_response('早安')}")
