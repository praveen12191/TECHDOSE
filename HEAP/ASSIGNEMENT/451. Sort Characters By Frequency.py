class Solution:
    def frequencySort(self, s: str) -> str:
        has = Counter(s)
        k = ""
        for i,j in sorted(has.items(),key=lambda x:-x[1]):
            k+=(i*j)
        return k