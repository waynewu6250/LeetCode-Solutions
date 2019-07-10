class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
#         # Get the length of word
#         locate = 0
#         counter = 0
#         while True:
#             counter += 1
#             locate += (26 ** counter)
#             if locate > n:
#                 break
        
#         # Get the index of character
#         i = counter - 1
#         cache = []
#         while i > 0:
#             cache.append(n / 26**i)
#             n %= 26**i
#             i -= 1
#         cache.append(n)
#         print(cache)
#         # Get the answer
#         str = ''
#         for i in cache:
#             str += chr(i+ord('A')-1)
#         return str
    
        alphabet="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    
        output=''

        dict={i:alphabet[i-1] for i in range(1,26)}
        dict[0]='Z'

        while True:
            yu=n%26
            output+=dict[yu]
            if yu==0:
                n=n-26
            if n<26:              
                break   
            else:
                n=n//26

        return output[::-1]