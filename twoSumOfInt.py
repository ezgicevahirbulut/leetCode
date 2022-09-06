from operator import xor


class Solution:
    def getSum(self, a:int,b:int) ->int:

        if a<b:
            return self.getSum(b,a)
            
        x,y = abs(a),abs(b)
        sign = 1
        if a<0:
            sign=-1



        if a*b>=0:
            while y:
                xor =x^y
                carry = (x&y)<<1
                x,y = xor,carry
        else:

            while y:
                xor =x^y
                carry = (-x&y)<<1
                x,y = xor,carry

        return sign*x   