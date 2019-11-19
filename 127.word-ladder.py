#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not wordList or endWord not in wordList or not beginWord or not endWord:
            return 0
        
        cache = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                cache[key].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                if key in cache:
                    for nextword in cache[key]:
                        if nextword not in visited:
                            queue.append((nextword, level+1))
                            visited.add(nextword)
        return 0