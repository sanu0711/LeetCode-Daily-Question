class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five=0
        ten=0
        for i in bills:
            if i==5:
                five += 1
            elif i==10:
                five -= 1
                ten += 1
            else:
                if ten>0:
                    ten -= 1
                    five -= 1
                else :
                    five -= 3
            if five<0:
                return False
        return True
