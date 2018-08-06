class Player(object):
    def __init__(self, name="Siri", guess=-1, score=-1):
        self.name = name
        self.guess = guess
        self.score = score

    def get_name(self):
        return self.name

    def get_guess(self):
        return self.guess

    def get_score(self):
        return self.score

    def set_name__(self, name):
        self.name = name

    def set_guess(self, guess):
        self.guess = guess

    def set_score(self, score):
        self.score = score

    def get_state(self):
        return self.name + 'last guess is', self.guess, 'and his score is', self.score;