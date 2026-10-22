class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypt = []
        for s in strs:
            l = len(s)
            encrypt.append(f'{l}{s}#')
        return ''.join(encrypt)
        
        
    def decode(self, s: str) -> List[str]:
        c = 0
        decrypted = []
        
        while c < len(s):
            if not s[c].isnumeric():
                c += 1
                continue
            hasht = c+int(s[c])+1
            w = s[c+1:hasht]
            print(w)
            decrypted.append(w)
            c = hasht
        return decrypted