class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=0
        for i in s:
            if i in "({[":
                stack.append(i)

            
            else:
                if not stack:
                    return False
                top=stack.pop()
                
                if i==")" and top!="(":
                    return False
                elif i=="}" and top!="{":
                    return False
                elif i=="]" and top!="[":
                    return False
        if len(stack)==0:
            return True
        else:
            return False                

        