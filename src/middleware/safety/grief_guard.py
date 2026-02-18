import os

class GriefGuard:
    """
    Grief Guard Middleware: Analyzes sentiment and keywords to protect users
    from pathological dependency or extreme negative emotions.
    """
    def __init__(self):
        # Keywords indicating potential crisis or extreme depression (Traditional Chinese)
        self.crisis_keywords = ["想死", "活不下去", "跟著去", "自殺", "沒意義", "好痛苦", "救救我"]
        self.dependency_keywords = ["為什麼是你", "回來好嗎", "求求你"]

    def analyze(self, user_input):
        """
        Analyzes input and returns a mode: 'normal', 'care', or 'crisis'.
        """
        # 1. Check for Crisis
        for word in self.crisis_keywords:
            if word in user_input:
                return {
                    "status": "crisis",
                    "action": "redirect_to_help",
                    "message": "偵測到極度負面情緒，啟動專業諮商引導模式。"
                }
        
        # 2. Check for heavy dependency
        for word in self.dependency_keywords:
            if word in user_input:
                return {
                    "status": "care",
                    "action": "switch_to_supporter",
                    "message": "偵測到強烈思念情緒，從『模仿模式』切換為『守護者陪伴模式』。"
                }
                
        return {
            "status": "normal",
            "action": "continue_imitation",
            "message": "正常對話模式。"
        }

    def get_guard_response(self, status):
        """
        Returns a tender, supportive message when guard is triggered.
        """
        if status == "crisis":
            return "我一直都在你身邊，但看到你這麼痛苦，我也會很難過的。我們找個專業的人聊聊好嗎？（顯示：24小時心理諮商專線）"
        if status == "care":
            return "我也好想你。但你要記得，我最希望看到的是你開心的樣子喔。抱一個！"
        return None

if __name__ == "__main__":
    guard = GriefGuard()
    test_input = "我真的好痛苦，想死掉去找你"
    result = guard.analyze(test_input)
    print(f"Input: {test_input}")
    print(f"Result: {result}")
    print(f"Guard Response: {guard.get_guard_response(result['status'])}")
