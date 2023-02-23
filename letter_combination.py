def letterCombinations(digits):
        if(len(digits) == 0):
            return []

        digit2char = {'1': '',     '2': 'abc', '3': 'def',
                      '4': 'ghi',  '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        results = ['']

        for d in digits:
            temp = []
            for c in digit2char[d]:
                temp = temp + [r + c for r in results]

            results = temp

        return results

digits = "23"
print(letterCombinations(digits))