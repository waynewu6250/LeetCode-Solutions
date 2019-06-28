class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        def count(string):
            dic = {}
            for i,s in enumerate(string):
                dic[s] = dic.get(s,[])+[i]
            return dic
        
        secret_count = count(secret)
        
        a_count = 0
        b_count = 0
        
        # Handle A
        for i,g in enumerate(guess):
            if g == secret[i]:
                a_count += 1
                secret_count[g].remove(i)
        
        # handle B
        for i,g in enumerate(guess):
            if g not in secret_count:
                continue
            if g != secret[i] and len(secret_count[g]):
                b_count += 1
                secret_count[g].pop()
                    
        return str(a_count)+"A"+str(b_count)+"B"