class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # A lógica aqui é ao contrária, ela segue a seguinte ordem:
        """
            1. Atribui o valor de hi a posição da array
            2. Atribui a uma variavel dumb o valor da array atual
            3. hi recebe o maior valor do hi atual e o presente na array
            4. o fluxo segue até chegar no final da array

            Obs: Só funciona caso a array esteja sendo lida de trás pra frente
        """
        hi = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = hi
            hi = max(tmp, hi)
        return arr