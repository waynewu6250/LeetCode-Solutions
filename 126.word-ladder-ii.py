#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordList.append(beginWord)
        
        distances = self.bfs(endWord, wordList)
        
        answer = []
        items = [beginWord]
        self.dfs(beginWord, endWord, wordList, distances, answer, items)
        return answer
    
    
    def nextwords(self, word, wordList):
        words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i]+c+word[i+1:]
                if next_word != word and next_word in wordList:
                    words.append(next_word)
        return words
    
    def bfs(self, startWord, wordList):
        
        distances = {startWord: 0}
        queue = collections.deque([startWord])
        
        while queue:
            word = queue.popleft()
            for nextword in self.nextwords(word, wordList):
                if nextword not in distances:
                    distances[nextword] = distances[word]+1
                    queue.append(nextword)
        return distances
    
    def dfs(self, beginWord, endWord, wordList, distances, answer, items):
        
        if beginWord == endWord:
            answer.append(list(items))
            return
        
        for nextword in self.nextwords(beginWord, wordList):
            if distances[nextword] != distances[beginWord]-1:
                continue
            items.append(nextword)
            self.dfs(nextword, endWord, wordList, distances, answer, items)
            items.pop()
        
# @lc code=end

