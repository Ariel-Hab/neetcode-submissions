class Solution:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        alphabet = "abcdefghijklmnñopqrstuvwxyz"
        queue = deque([(beginWord,1)])

        while queue:
            word,depth = queue.popleft()
            for n in range(len(beginWord)):
                for letter in alphabet:
                    if word[n] == letter:
                        continue
                    newWord= word[0:n] + letter + word[n+1:len(beginWord)]
                    if newWord == endWord:
                        wordSet.remove(newWord)
                        return depth+1
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord,depth+1))
        return 0
        


            
            