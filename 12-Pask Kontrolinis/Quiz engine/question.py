import quiz_bank
import global_variables

class S_question:
    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers,
                 question_num, answer, score, highscore, attempts, next):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.question_num = question_num
        self.answer = answer
        self.score = score
        self.highscore = highscore
        self.attempts = attempts
        self.next = next

    def print_question(self):
        print("-------------------------------------------------")
        print(f"Score: {question.score}\t\tHighscore: {question.highscore}\t\tAttemps: {question.attempts}")
        print("-------------------------------------------------")

        print(f"Question {question.question_num} ({question.difficulty}):", question.question)
        self.answer = input("Answer (True/False): ")

        S_question.check_asnwers('self')

    def check_asnwers(self):
        if self.answer == question.correct_answer:
            self.score = self.score + 10
            self.next = self.next + 1
            self.question_num = self.question_num + 1
            S_question.print_question('self')
        elif self.answer == question.incorrect_answers:
            self.next = self.next + 1
            self.question_num = self.question_num + 1
            S_question.print_question('self')
        else:
            print("ERROR")
            exit()

question = S_question(quiz_bank.question_data[0 + global_variables.next]['category'],
                      quiz_bank.question_data[0 + global_variables.next]['type'],
                      quiz_bank.question_data[0 + global_variables.next]['difficulty'],
                      quiz_bank.question_data[0 + global_variables.next]['question'],
                      quiz_bank.question_data[0 + global_variables.next]['correct_answer'],
                      quiz_bank.question_data[0 + global_variables.next]['incorrect_answers'][0],
                      global_variables.question_num,
                      global_variables.answer,
                      global_variables.score,
                      global_variables.highscore,
                      global_variables.attempts,
                      global_variables.next)