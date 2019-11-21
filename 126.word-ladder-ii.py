#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        cache = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                cache[key].append(word)
        
        distances = self.bfs(endWord, wordList, cache)
        
        answer = []
        items = [beginWord]
        self.dfs(beginWord, endWord, wordList, distances, answer, items, cache)
        return answer
    
    
    def bfs(self, startWord, wordList, cache):
        
        distances = {startWord: 0}
        queue = collections.deque([startWord])
        
        while queue:
            word = queue.popleft()
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                if key in cache:
                    for nextword in cache[key]:
                        if nextword not in distances:
                            distances[nextword] = distances[word]+1
                            queue.append(nextword)
        return distances
    
    def dfs(self, beginWord, endWord, wordList, distances, answer, items, cache):
        
        if beginWord == endWord:
            answer.append(list(items))
            return
        
        for i in range(len(beginWord)):
            key = beginWord[:i]+"*"+beginWord[i+1:]
            if key in cache:
                for nextword in cache[key]:
                    if nextword in distances and beginWord in distances:
                        if distances[nextword] != distances[beginWord]-1:
                            continue
                        items.append(nextword)
                        self.dfs(nextword, endWord, wordList, distances, answer, items, cache)
                        items.pop()
        
# @lc code=end

