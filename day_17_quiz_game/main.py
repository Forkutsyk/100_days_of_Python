from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# How it works: We have a list of questions (question_data) which consists of dictionaries that have
# a question and answer (12 questions)
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"}]
# We also have a class that initializes 2 attributes: question and answer (class Question)

question_bank = []
# Now we create a list where, using a for loop, we fill it with objects of the Question class,
# and the data is taken from question_data.
# Each object will have 2 attributes, question and answer.
for question in question_data:
    q_data = question['text']
    a_data = question['answer']
    question_bank.append(Question(q_data, a_data))

# We also have a QuizBrain class (a class with the main game logic) that initializes question_number and user_score
# attributes, as well as question_pool (a list of questions) which we take
# from the previously filled question_bank.
# QuizBrain contains 3 methods: still_has_questions, next_question, check_answer
quiz = QuizBrain(question_bank)

# still_has_questions always returns True when the value of the question_number attribute (the question we are
# currently on) is less than the length of the question list. As soon as it is no longer
# less, the method returns False. This means that this loop will call the next_question method as long as
# there are questions in the database.

while quiz.still_has_question():
    quiz.next_question()
    # next_question is a method that outputs the current question (before that it increases the
    # question_number attribute by 1) and accepts the user's answer, after which it passes it to check_answer along
    # with the correct answer where this answer is checked and the result is output: Correct
    # (increasing the user_score attribute) / Incorrect (the user_score attribute does not change)
    # At the end of the method, the correct answer is displayed

# After the loop ends (after 12, the last question) the game summary is displayed and we say goodbye
print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
