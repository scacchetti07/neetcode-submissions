class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list) # Cria um dicionario com valores genericos para inicializar
        for an in strs:
            w = ''.join(sorted(an))
            cache[w].append(an)      
        return list(cache.values())