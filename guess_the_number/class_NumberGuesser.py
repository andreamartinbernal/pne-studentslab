from random import randrange

class NumberGuesser:
    def __init__(self, secret_number, attempts):
        self.secret_number = randrange(1, 10, 1)
        self.attempts = 0

    def guess_number(self, number):
        if int(number) < self.secret_number:
            self.attempts += 1
            return 1
        elif int(number) > self.secret_number:
            self.attempts += 1
            return 2
        elif int(number) == self.secret_number:
            total_attempts = self.attempts
            return 0

