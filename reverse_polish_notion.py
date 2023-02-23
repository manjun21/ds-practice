def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                result = operations[token](left, right)
                stack.append(int(result))
        return stack.pop()

tokens =["4","13","5","/","+"]
#tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))