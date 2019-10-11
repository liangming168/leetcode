# -*- coding: utf-8 -*-
"""
Q127 word ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
Seen this question in a real interview before?
"""
'''
method bfs
use queue to store current and next level words,
if curr_level start from the begining word and together push in its length=1
then if curr_level queue is not empty, while
iterate all curr_level, for each curr_word, if it has a transfomation word, then add to next_level
                                                and remove the transformed word from the wordList
                                                
note: to save time, use a hashset to store wordList, so only O(1) to search for a word
      to find a transformation, change each letter of the curr_word to check wether in wordlist
      rememeber to remove word transformed from the wordList
      
time: O(n*l), n is the number of words in wordList, l is the length of a word
space: O(n), myList hashset and curr/next_level
'''

class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        
        if endWord not in wordList:
            return 0
        myList = set(wordList)
#        myList.add(beginWord)
        curr_level = [(beginWord,1)]
        next_level = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        while curr_level:
            for curr in curr_level:
                curr_word = curr[0]
                curr_len = curr[1]
                if curr_word == endWord:
                    return curr_len
                for i in range(len(beginWord)):
                    for j in alpha:
                        if curr_word[i]==j:
                            continue
                        w = curr_word[:i] + j + curr_word[i+1:]
                        if w in myList:
                            next_level.append((w,curr_len+1))
                            myList.remove(w)
            curr_level = next_level
            next_level = []
        return 0
    
if __name__ =='__main__':
    mySolution = Solution()
    print(mySolution.ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"]))
        