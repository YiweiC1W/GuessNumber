import random
from Player import Player


class Game:
    def __init__(self):
        self.player1 = Player("yiwei", -1, 0)
        self.player2 = Player()
        self.guessNum = 0
        self.maximum = 100
        self.minimum = 1
        self.count = 1

    def compare_range(self, answer):
        if (self.minimum < answer) and (answer < self.maximum):
            if self.guessNum < answer:
                self.minimum = self.guessNum
            else:
                self.maximum = self.guessNum
            print(self.minimum, "< Answer <", self.maximum)

    def get_result(self):
        if self.player1.get_score() > self.player2.get_score():
            return "You win"
        elif self.player1.get_score() == self.player2.get_score():
            return "Draw"
        elif self.player1.get_score() < self.player2.get_score():
            return "You lose"

    def name_player1(self):
        name = input("Please enter your name: ")
        name = name.strip()
        while len(name) > 8 or len(name) == 0:
            print("Warning: Name should be 1-8 character(s)!")
            print("Please re-enter your name: ")
            name = input().strip()
        self.player1.set_name__(name)
        print("Hello,", name)

    def player1_make_guess(self):
        is_int = False
        while is_int is False:
            self.guessNum = input("Please enter a number: ")
            if self.guessNum.isdecimal():
                self.guessNum = int(self.guessNum)
                if (self.guessNum < 1 or self.guessNum > 100) and self.guessNum != 999:
                    print("Number must between 1-100(or 999)! Do again")
                else:
                    is_int = True
            else:
                print('Input error! You should enter a number!')

    def player2_make_guess(self):
        self.guessNum = random.randint(self.minimum, self.maximum)
        print("PC Player: ")
        print(self.guessNum)

    def player_set_score(self, player, is_correct, distance=0):
        if  is_correct is True:
            score = player.get_score() + 26 - self.count * (6 + (7 - self.count)) / 2
        else:
            if (10 - distance) > 0:
                score = player.get_score() + 10 - distance
        player.set_score(score)

    def player_attempt(self, abandon, answer, player):
        if player == self.player1:
            self.player1_make_guess()
        else:
            self.player2_make_guess()
        roll = random.randint(1, 20)
        if (self.guessNum != 999 and player == self.player1) or (abandon != roll and player == self.player2):
            player.set_guess(self.guessNum)
            if self.guessNum != answer:
                self.compare_range(answer)
            else:
                self.player_set_score(player, True)
                self.count = 10
            if self.count == 6:
                self.player_set_score(self.player1, False, abs(self.player1.get_guess()-answer))
                self.player_set_score(self.player2, False, abs(self.player2.get_guess()-answer))
        else:
            print('Abandon this round!')
            self.count = 20
        self.count += 1

    def print_score(self, answer):
        print('Answer is', answer)
        print(self.player1.get_state())
        print(self.player2.get_state())
        print()

    def reset(self):
        self.maximum = 100
        self.minimum = 1
        self.count = 1

    def run(self):
        print("Welcome to the  Gue55ing Game!")
        self.name_player1()
        for round_num in range(1, 5, 1):
            answer = random.randint(1, 100)
            abandon_round = random.randint(1, 20)
            roll_first = random.randint(1, 2)
            while self.count < 7:
                print("Round:", round_num, "/4")
                print("Turn:", int((self.count+1)/2), "/3")
                if roll_first == 1:
                    self.player_attempt(abandon_round, answer, self.player1)
                    if self.count < 7:
                        self.player_attempt(abandon_round, answer, self.player2)
                else:
                    self.player_attempt(abandon_round, answer, self.player2)
                if self.count < 7:
                    self.player_attempt(abandon_round, answer, self.player1)
                print()
            if self.count != 21:
                self.print_score(answer)
            self.reset()
        print('Game over!')
        print(self.get_result())
