import quiz_bank

def check_ans(ans, attempts, score):
    if quiz_bank.question_data[0]['correct_answer'].lower() == ans.lower():
        return True
    else:
        return False

