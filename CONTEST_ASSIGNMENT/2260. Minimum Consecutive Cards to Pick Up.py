class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mn = float('inf')
        has = defaultdict(int)
        for i in range(len(cards)):
            if(cards[i] in has):
                mn = min(mn,i-has[cards[i]][1]+1)
                has[cards[i]][1] = i 
                continue 
            k = has[cards[i]]+1
            has[cards[i]] = [k,i]
        if(mn==float('inf')):
            return -1 
        return mn