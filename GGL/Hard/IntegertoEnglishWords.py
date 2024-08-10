"""
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 
Constraints:
0 <= num <= 2**31 - 1
"""

class Solution:

    def numberToWords(self, num: int) -> str:
        num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

        def tens_unit(n):
            if n <= 20 or n % 10 == 0:
                return num2words.get(n, '')
            else:
                return num2words[n // 10 * 10] + ' ' + num2words[n % 10]
                
        def hundreds(n):
            if n == 0:
                return ''
            elif n < 100:
                return tens_unit(n)
            else:
                res = num2words[n // 100] + ' Hundred '
                if n % 100 != 0: 
                    res += tens_unit(n % 100)
                return res

        def thousands(n):
            if n == 0:
                return ''
            elif n < 1000:
                return hundreds(n)
            else:
                return hundreds(n // 1000).strip() + ' Thousand ' + hundreds(n % 1000)

        def millions(n):
            if n == 0:
                return ''
            elif n < 1000000:
                return thousands(n)
            else:
                return hundreds(n // 1000000).strip() + ' Million ' + thousands(n % 1000000)
        
        def billions(n):
            if n == 0:
                return num2words.get(n, '')
            elif n < 1000000000:
                return millions(n)
            else:
                return hundreds(n // 1000000000).strip() + ' Billion ' + millions(n % 1000000000)


        return billions(num).strip()  # Remove leading/trailing spaces
        
