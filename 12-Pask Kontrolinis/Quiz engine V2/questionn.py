class S_question:
    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers, question_num, answer, score, highscore, attempts, next):
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