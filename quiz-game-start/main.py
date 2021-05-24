from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# print(question_bank)
no_of_questions = int(len(question_data) -1)
# print(no_of_questions)
# print(question_data[1]['text'])

# new_q = Question()
for n in range(no_of_questions):
    t = question_data[n]['question']
    a = question_data[n]['correct_answer']
    question_bank.append(Question(t, a))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")