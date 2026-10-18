class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ""

        for char in s:
            if char.isalnum():
                clean_text += char.lower()
        

        if clean_text == clean_text[::-1]:
            return True
        else:
            return False