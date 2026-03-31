class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(stack, tokens[i])
            
            if tokens[i] == '+':
                one = int(stack.pop())
                two = int(stack.pop())    
                stack.append(one + two)
            elif tokens[i] == '-':
                one = int(stack.pop())
                two = int(stack.pop())    
                stack.append(two - one)

            elif tokens[i] == '*':
                one = int(stack.pop())
                two = int(stack.pop())   
                stack.append(one * two)

                # takes 
            elif tokens[i] == '/':
                one = int(stack.pop())
                two = int(stack.pop())    
                # print(two, one, one // two)
                stack.append(two / one)
            else:
                stack.append(tokens[i])

 
        return int(stack[0])
