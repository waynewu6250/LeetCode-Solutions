class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for i in range(left, right+1):
            flag = 0
            if str(i).find('0') == -1:
                for digit in str(i):
                    if i % int(digit) != 0:
                        flag = 1
                        break
                if flag == 0:
                    answer.append(i)
        return answer