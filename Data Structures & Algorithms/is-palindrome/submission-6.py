class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        s = re.sub(pattern, '', s)
        s = s.lower()
        i = 0
        j = len(s)-1
        while i != j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True