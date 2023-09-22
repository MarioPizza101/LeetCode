class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mapping = {

            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []

        for c in s:

            if c in mapping:

                if not stack:

                    return False

                if stack.pop() != mapping[c]:

                    return False
            else:

                stack.append(c)
        
        return not stack
        
