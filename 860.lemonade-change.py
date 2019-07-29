#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = 0
        tens = 0
        if not bills:
            return True
        
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                if fives == 0:
                    return False
                else:
                    fives -= 1
                    tens += 1
            else:
                if tens == 0:
                    if fives < 3:
                        return False
                    else:
                        fives -= 3
                elif fives == 0:
                    return False
                else:
                    fives -= 1
                    tens -= 1
        return True
        

