class Solution:
    def generateParenthesis(self, n):
        result = []  # valid combinations store karne ke liye

        def backtrack(cur, open_count, close_count):
            # Jab length 2*n ho jaye, matlab poore parentheses use ho gaye
            if len(cur) == 2 * n:
                result.append(cur)
                return

            # '(' lagana hai jab tak open_count < n hai
            if open_count < n:
                backtrack(cur + '(', open_count + 1, close_count)

            # ')' lagana hai sirf jab close_count < open_count hai
            if close_count < open_count:
                backtrack(cur + ')', open_count, close_count + 1)

        # Empty string se start karna hai
        backtrack("", 0, 0)
        return result