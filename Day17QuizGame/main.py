from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congrats! You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# TODO: Make it work with Open Trivia Database (https://opentdb.com/api_config.php)

