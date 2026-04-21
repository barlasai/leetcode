class Solution:
    def calculate(self, s: str) -> int:

        result = 0        # Holds the final result of the expression
        number = ''       # Accumulates digits to form the current number
        aux_num = ''      # Stores intermediate results for multiplication and division
        prev_op = '+'     # Keeps track of the previous operator, initialized to '+'

        # Process each character in the string, with an extra '+' to ensure the last number is processed
        for char in s + '+':
            if char.isdigit():
                number += char  # Build the current number from consecutive digits
            
            elif char == ' ':
                continue  # Ignore spaces

            elif char in '-+':
                # Update result based on the previous operator
                match prev_op:
                    case '+':
                        result += int(number)  # Add the current number to result
                        number = ''
                    case '-':
                        result -= int(number)  # Subtract the current number from result
                        number = ''
                    case '*':
                        result += int(number) * int(aux_num)  # Multiply with stored value and add to result
                        number, aux_num = '', ''
                    case '/':
                        result += int(int(aux_num) / int(number))  # Divide stored value by the current number and add to result
                        number, aux_num = '', ''

                prev_op = char  # Update previous operator to the current one

            elif char in '*/':
                # Update auxiliary number based on the previous operator
                match prev_op:
                    case '+':
                        aux_num = number  # Set aux_num to the current number for future multiplication/division
                        number = ''
                    case '-':
                        aux_num = '-' + number  # Set aux_num to the negative of the current number
                        number = ''
                    case '*':
                        aux_num = int(number) * int(aux_num)  # Multiply current number with the stored value
                        number = '' 
                    case '/':
                        aux_num = int(int(aux_num) / int(number))  # Divide stored value by current number
                        number = ''
                
                prev_op = char  # Update previous operator to the current one

        return result  # Return the final result of the evaluated expression