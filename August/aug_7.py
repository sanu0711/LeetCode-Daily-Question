class Solution:
    def numberToWords(self, num: int) -> str:

        def helper(self,num):
            one_digit_list = ['' , 'One', 'Two', 'Three', 'Four' , 'Five', 'Six', 'Seven', 'Eight', 'Nine']
            two_digit_list = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
            tens_list = ['' , '' , 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            
            if num == 0:
                return ''
            elif num < 10:
                return one_digit_list[num]
            elif num < 20:
                return two_digit_list[num-10]
            elif num < 100:
                return tens_list[num//10] + ' ' + helper(self,num%10)
            else:
                return one_digit_list[num//100] + ' Hundred ' + helper(self,num%100)
        if num == 0:
            return 'Zero'
        higher_list = ['' , 'Thousand', 'Million', 'Billion']
        result = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                helper_output = helper(self,num % 1000)
                result = helper_output.strip() + ' ' + higher_list[i] + ' ' + result
            num = num // 1000
            i += 1
            
        return result.strip()
    
# obj = Solution()
# print(obj.numberToWords(50868))

# https://leetcode.com/problems/integer-to-english-words/description/ 
    
            