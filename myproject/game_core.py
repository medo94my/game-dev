from random import sample as S  # Sample elimantes duplicates
import json


class Student():

    def __init__(self):

        self.data = {}
        self.Value_Analyzer = []  # This list will be counting the correct numbers and                                 correct position for every guess made by the user
        self.answer = 0
        # This dictionary will be in the analyzer to save every step                         made by the user.
        self.Guesses_Dic = {}
        self.Score = 15
        self.Total_Score = 0
        # self.pos = {}
        self.Answer = 0
        self.cright = 0
        self.cwrong = 0
        self.num_correct = 0
        self.fors = ""
        self.Dicc = {}
        self.Counter = 0

    def randomize(self):
        self.Answer = S(range(1, 9), 4)
        for i in self.Answer:
            self.fors += str(i)

    def analyze(self):

        # This loop saves the correct values into each guess.
        for i in range(len(self.Value_Analyzer)):
            self.Guesses_Dic[i] = self.Value_Analyzer[i]

        # Every three tries without any progress makes you lose points.
        three_tries = 0

        # This for loop compares every guess with its next step to see if the score of the user should decrease.
        for i in range(len(self.Value_Analyzer)-1):

            if self.Guesses_Dic[i][0] > self.Guesses_Dic[i+1][0] and self.Guesses_Dic[i][1] > self.Guesses_Dic[i+1][1]:
                self.Score -= 10

            elif self.Guesses_Dic[i][0] > self.Guesses_Dic[i+1][0]:
                self.Score -= 5

            elif self.Guesses_Dic[i][0] == self.Guesses_Dic[i+1][0] and self.Guesses_Dic[i][1] == self.Guesses_Dic[i+1][1]:
                three_tries += 1

            elif self.Guesses_Dic[i][1] > self.Guesses_Dic[i+1][1]:
                three_tries += 1

            if three_tries == 3:  # If user has no progress for 3 turns he will lose points
                self.Score -= 5
                three_tries = 0

        three_tries = 0  # This resets the tries for the next loops

        # This loop compares the Guesses_Dic to see if the score should increase.
        for i in range(len(self.Value_Analyzer)-1):

            if self.Guesses_Dic[i][0] < self.Guesses_Dic[i+1][0] and self.Guesses_Dic[i][1] < self.Guesses_Dic[i+1][1]:
                self.Score += 10

            elif self.Guesses_Dic[i][0] < self.Guesses_Dic[i+1][0]:
                self.Score += 5

            elif self.Guesses_Dic[i][1] < self.Guesses_Dic[i+1][1]:
                three_tries += 1

            elif three_tries == 3:
                self.Score += 5
                three_tries = 0

        # self.Total_Score = self.Score + self.Guesses_Dic.count
        print("Your Score is ", self.Score, "\n")
        print("These are your number of guesses with the correct numbers and correct positions ")
        self.Dicc = self.Guesses_Dic
        print(self.Dicc)
        self.Guesses_Dic = {}

    def check(self, guess_director):  # ==========================================
        def restart(self):
            self.Counter == 0
            print("counter reseted")
        print(self.Answer)

        number = ['1', '2', '3', '4', '5', '6', '7', '8']

        def guess_num():

            Valid_counter = 0  # This variable detects if the input is valid or not
            guess = guess_director

            for i in range(len(guess)):

                if guess[i] in number:  # If the 4 digits were valid it will get through
                    Valid_counter += 1

                # This detects if there is any duplicate values
            if guess.count(guess[i]) != 1:
                print("Dont enter Duplicates")
                Valid_counter = 14
                return -1

            if Valid_counter == 4 and len(guess) == 4:
                return guess

            else:
                print("Enter four numbers! From 1 to 8")
                return -1

        checker = guess_num()

        if checker != -1:
            self.num_correct = 0
            self.cright = 0  # right position
            self.cwrong = 0  # wrong position

            for x in range(4):
                for y in range(4):  # This checks every guess with the final answer

                    if checker[x] == str(self.Answer[y]):
                        self.num_correct += 1
                        if x == y:
                            self.cright += 1
                        else:
                            self.cwrong += 1

            print("       Number of correct digits " + str(self.num_correct))
            print("       Right position " + str(self.cright))
            print("       Wrong position " + str(self.cwrong))

            self.Counter += 1

            # The function below appends every step into the Guesses_Dic dictionary to compare among each other.
            self.Value_Analyzer.append(
                [int(self.num_correct), int(self.cright)])

            # self.data['result'] = []
            # self.data['result'].append(
            #     {'correct': int(num_correct), 'Right': int(
            #         self.cright), 'Wrong': int(cwrong), 'score': self.Score})
            # self.data['result'] += self.data['result']

            if self.cright == 4:
                print("Congratulations!!! You won!!")
                self.Answer = S(range(1, 9), 4)

            # elif self.Counter == 10:
            #     print('try again')
            #     self.Answer = S(range(1, 9), 4)


#     def play(self):

#         from random import sample as S  # Sample elimantes duplicates
#         Answer = S(range(1, 9), 4)
#         # print ("\n",Answer)
#         # After declaring the Sample enter (the range of the numbers,the length of numbers)

#         print("\nWelcome to Mastermind! You need to guess the secret code! \nEnter 4 numbers from 1 to 8 - no duplicates allowed!\n")

#         number = ['1', '2', '3', '4', '5', '6', '7', '8']
#         no_Guesses_Dic = 0

#         def guess_num():
#             Valid_counter = 0  # This variable detects if the input is valid or not
#             guess = self.guessNo

#             for i in range(len(guess)):

#                 if guess[i] in number:  # If the 4 digits were valid it will get through
#                     Valid_counter += 1

#                 # This detects if there is any duplicate values
#                 if guess.count(guess[i]) != 1:
#                     print("Dont enter Duplicates")
#                     # flash('Dont enter Duplicates', 'danger')
#                     Valid_counter = 14
#                     return -1

#             if Valid_counter == 4 and len(guess) == 4:
#                 return guess

#             else:
#                 print("Enter four numbers! From 1 to 8")
#                 return -1

#         guess = 0

#         while guess != -1:  # The guess_num function will return -1 if it was invalid

#             guess = guess_num()

#             if guess != -1:

#                 num_correct = 0
#                 cright = 0  # right position
#                 cwrong = 0  # wrong position
#                 no_Guesses_Dic += 1

#                 for x in range(4):
#                     for y in range(4):  # This checks every guess with the final answer

#                         if guess[x] == str(Answer[y]):
#                             num_correct += 1
#                             if x == y:
#                                 cright += 1
#                             else:
#                                 cwrong += 1

#                 print("       Number of correct digits " + str(num_correct))
#                 print("       Right position " + str(cright))
#                 print("       Wrong position " + str(cwrong))
#                 # self.pos = {num_correct, cright, cwrong}
#                 # The function below appends every step into the Guesses_Dic dictionary to compare among each other.
#                 self.Value_Analyzer.append([int(num_correct), int(cright)])
#                 self.data['result'] = []
#                 self.data['result'].append(
#                     {'correct': int(num_correct), 'Right': int(
#                         cright), 'Wrong': int(cwrong), 'score': self.Score})
#                 self.data['result'] += self.data['result']
#

#                 elif no_Guesses_Dic == 10:
#                     print(
#                         "You have exceeded the limit of 10 tries. Good luck next time.  \nThe answer was ", Answer)
#                     self.data['result'][0]['answer'] = Answer

#                     break

#             elif (guess == -1):  # If the guess input was invalid it will loop without checking
#                 guess = 0


# # data = {}
# # data['students'] = []


# # def save(x, y, z, q, ts):

# #     for i in range(1):
# #         data['students'].append({
# #             "id": x,
# #             "name": y,
# #             "age": z,
# #             "Score": q,
# #             "Total Score": ts})
# #     with open('data.txt', 'w') as outfile:
# #         json.dump(data, outfile, indent=(4))
# # ================================+MAIN+==========================================
