class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=x
        s=0
        while(x>0):
            d=x%10
            x=x//10
            s=s*10+d 
        if s==num:
            return True
        
        return False    
        