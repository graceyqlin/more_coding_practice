# LC150.Evaluate_Reverse_Polish_Notation.py
# Topic: stack
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

class Solution:
    def evalRPN(self, tokens):
        stack = []
        result = 0
        for i, t in enumerate(tokens):
                
            if tokens[i] not in ["+", "-", "*", "/"]:               
                stack.append(int(tokens[i]))
               
            else:
                r, l = stack.pop(), stack.pop()
                if tokens[i] == '+':
                    stack.append((l+r))
                elif tokens[i] == '-':
                    stack.append((l-r))
                elif tokens[i] == '*':
                    stack.append((l*r))
                    
                elif tokens[i] == '/':
                    if l*r < 0 and l % r != 0:
                        stack.append((l//r+1))
                    else:
                        stack.append((l//r))
                
            
        
        return stack[-1]

s = Solution()
print(s.evalRPN(["4", "13", "5", "/", "+"]))