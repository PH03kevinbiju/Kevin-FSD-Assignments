import itertools

class CryptarithmeticSolver:
    def __init__(self):
        self.word1 = "SEND"
        self.word2 = "MORE"
        self.result = "MONEY"
        self.unique_letters = set(self.word1 + self.word2 + self.result)

    def is_valid_solution(self, letter_to_digit):
        num1 = self.word_to_number(self.word1, letter_to_digit)
        num2 = self.word_to_number(self.word2, letter_to_digit)
        num_result = self.word_to_number(self.result, letter_to_digit)
        return num1 + num2 == num_result

    def word_to_number(self, word, letter_to_digit):
        return int(''.join(str(letter_to_digit[letter]) for letter in word))

    def solve(self):
        if len(self.unique_letters) > 10:
            return "Too many unique letters. Solution not possible with distinct digits."
        
        digits = range(10)
        for perm in itertools.permutations(digits, len(self.unique_letters)):
            letter_to_digit = dict(zip(self.unique_letters, perm))
            if letter_to_digit[self.word1[0]] == 0 or letter_to_digit[self.word2[0]] == 0 or letter_to_digit[self.result[0]] == 0:
                continue
            if self.is_valid_solution(letter_to_digit):
                return letter_to_digit
        return "No solution found."

kevin=CryptarithmeticSolver()
kevin.is_valid_solution(1)
kevin.word_to_number()
kevin.solve()
