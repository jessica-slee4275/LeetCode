"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]



        # res = []
        # t = ""
        # for word in words:
        #     t += word + " "
        #     if len(t) > maxWidth+1:
        #         t = t[:len(t)-(len(word)+1)]
        #         res.append(t[:-1].split(' '))
        #         t = word + " "
        # if len(t) > 0:
        #     res.append(t[:-1].split(' '))

        # ans = []
        # for r in res[:-1]:
        #     sentence = ""
        #     space = maxWidth-len(''.join(r))
        #     if len(r) > 1:
        #         base_space = space//(len(r)-1)
        #         if space//(len(r)-1) != space/(len(r)-1): base_space = (space//(len(r)-1))+1
        #         for w in r[:-1]:
        #             sentence += w
        #             sentence += ' '*int(base_space)
        #             # print(len(sentence+r[-1]), maxWidth)
        #             if len(sentence+r[-1]) > maxWidth:
        #                 sentence = sentence[:-1]+' '*(int(base_space)-2)
        #                 # rollback and set space//(len(r)-1)
        #         sentence += r[-1]
        #         # print(sentence)
        #         ans.append(sentence)
        #     else:
        #         ans.append(r[0] + ' '*int(space))

        # last = ' '.join(res[-1])
        # space = maxWidth-len(last)
        # ans.append(last+' '*int(space))

        # return ans
