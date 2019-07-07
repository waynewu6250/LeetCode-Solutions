class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = str(version1).split('.')
        ver2 = str(version2).split('.')
        
        a = (ver1, ver2) if len(ver1) > len(ver2) else (ver2, ver1)
        big, short = a
        
        for i in range(len(short)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return -1
        
        if sum([int(i) for i in big[len(short):]]) != 0:
            return 1 if big == ver1 else -1
        else:
            return 0