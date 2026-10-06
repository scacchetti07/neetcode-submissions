class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        # Partindo da primeira palavra da lista, contamos o tamanho máximo
        for i in range(len(prefix)):
            # checamos cada palavra incluindo a base
            for s in strs:
                # se a posição de letra da palavra base for igual ao tamanho total 
                # ou se a minha letra em I posição for diferente a da palavra base
                # Eu posso concluir que temos o mesmo prefixo e assim retorno as letras até I
                if i == len(s) or s[i] != strs[0][i]:
                    print(s[:i])
                    return s[:i]
        return strs[0] # Caso nada disso for verdade, não existe prefixo, então 
