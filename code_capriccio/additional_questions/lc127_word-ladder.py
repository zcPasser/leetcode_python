from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        visited = dict()
        visited[beginWord] = 1

        que = deque()
        que.append(beginWord)

        while que:
            word = que.popleft()
            path = visited[word]
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = ''.join(word_list)
                    if new_word == endWord:
                        return path + 1
                    if new_word in word_set and new_word not in visited:
                        visited[new_word] = path + 1
                        que.append(new_word)
        return 0


