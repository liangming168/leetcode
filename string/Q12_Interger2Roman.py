# -*- coding: utf-8 -*-
"""
Q12 interger to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

'''
method 1
since the question limit 4000, so enumerate all the digits Roman, 1 for 1,100,1000;2 for 2,200,200, etc ->table
then find out each digit from right to left, and search the table

time complexity: O(1)
space comlexity: O(1)

'''
class Solution1:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = [['I','X','C','M'],
                 ['II','XX','CC','MM'],
                 ['III','XXX','CCC','MMM'],
                 ['IV','XL','CD'],
                 ['V','L','D'],
                 ['VI','LX','DC'],
                 ['VII','LXX','DCC'],
                 ['VIII','LXXX','DCCC'],
                 ['IX','XC','CM']]
        res = ''
        for i in range(4):
            remain = num//(10**i)%10
            if remain>0:
                res = digit[remain-1][i] + res
        return res
    
'''
method 2
get each digit, discuss different situations
1,2,3 add 'I'
4, add 'I' and 'V'
5,6,7,8 , add 'I' then for digit-5 times, then add 'V' at the left
9, add 'IX'
0, add'X' 

time complexity: O(n), n is the number of digits
space comlexity: O(n)

'''
    
class Solution2:
    def intToRoman(self,num):
        """
        :type num: int
        :rtype: str
        """
        int2Roman = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        base = 1
        res = ''
        while(num):
            digit = num%10
            if digit<4:
                res = int2Roman[base]*digit +res
            elif digit == 4:
                res = int2Roman[base] + int2Roman[base*5] + res
            elif digit<9:
                digit = digit -5
                res = int2Roman[base]*digit + res
                res = int2Roman[5*base] + res
            elif digit == 9:
                res = int2Roman[base] + int2Roman[10*base] + res
            else:
                res = int2Roman[base*10] + res
            base = base*10
            num = num//10
        return res
                    
            





        