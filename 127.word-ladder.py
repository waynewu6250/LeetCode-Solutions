#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        n = len(beginWord)
        
        # 1. put in dictionary: wordpattern (a*c) : abc
        cache = {}
        for word in wordList:
            for i in range(n):
                key = word[:i]+"*"+word[i+1:]
                cache[key] = cache.get(key,[]) + [word]
        
        print(cache)
        
        # 2. set up queue and visited
        q = collections.deque([(beginWord, 1)])
        visited = set()
        
        # 3. bfs
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            
            if word not in visited:
                visited.add(word)
            
                for i in range(n):
                    key = word[:i]+"*"+word[i+1:]
                    if key in cache:
                        for possible_word in cache[key]:
                            q.append((possible_word, level+1))
        return 0