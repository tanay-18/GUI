from question_model import Question
from data import question_data
from quiz_brain import quizbrain
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_ans=question["answer"]
    new_q=Question(question_text,question_ans)
    question_bank.append(new_q)

quiz=quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")