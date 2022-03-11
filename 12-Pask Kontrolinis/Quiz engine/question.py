import quiz_bank
import global_variables

class S_question:
    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers, question_num, answer, score, highscore, attempts):
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

    def print_question(self):
        print("-------------------------------------------------")
        print(f"Score: {question.score}\t\tHighscore: {question.highscore}\t\tAttemps: {question.attempts}")
        print("-------------------------------------------------")

        print(f"Question {question.question_num} ({question.difficulty}):", question.question)
        global_variables.answer = input("Answer (True/False): ")

        S_question.check_asnwers(tuple)

    def check_asnwers(self):
        if global_variables.answer == question.correct_answer:
            global_variables.score = global_variables.score + 10
            print("-------------------------------------------------")
            print(f"Score: {question.score}\t\tHighscore: {question.highscore}\t\tAttemps: {question.attempts}")
            print("-------------------------------------------------")
        elif global_variables.answer == question.incorrect_answers:
            print("-------------------------------------------------")
            print(f"Score: {question.score}\t\tHighscore: {question.highscore}\t\tAttemps: {question.attempts}")
            print("-------------------------------------------------")
        else:
            print("ERROR")
            exit()

        if global_variables.quiz_lenght >= 3:
            print("------------------------------------------------------")
            print(f"Total Score: {question.score}\t\tHighscore: {question.highscore}\t\tAttemps: {question.attempts}")
            print("------------------------------------------------------")
            exit()
        else:
            global_variables.next = global_variables.next + 1
            global_variables.question_num = global_variables.question_num + 1
            S_question.print_question(tuple)

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
                      global_variables.attempts)