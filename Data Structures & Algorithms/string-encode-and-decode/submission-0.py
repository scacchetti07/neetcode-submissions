class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypt = ''
        for s in strs:
            l = len(s)
            encrypt += f'{l}{s}#'
        print(encrypt)
        return encrypt
        
        
        
    def decode(self, s: str) -> List[str]:
        cl = 0
        decrypted = []
        for i, w in enumerate(s):
            if w.isnumeric():
                cl = i+1
            if w == '#':
                decrypted.append(s[cl:i])

        return decrypted