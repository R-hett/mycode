import html

# define the trivia dictionary
trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca?",
    "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
    "incorrect_answers": [
        "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
        "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
        "&quot;Round up the usual suspects.&quot;"
    ]
}

# extract question and answers from trivia dictionary
question = trivia["question"]
correct_answer = html.unescape(trivia["correct_answer"])
incorrect_answers = [html.unescape(answer) for answer in trivia["incorrect_answers"]]
answers = incorrect_answers + [correct_answer]


# print the question
print(question)
for i, answer in enumerate(answers):
    print(f"{chr(i+65)}. {answer}")

# prompt user to answer with upper or lower case
guess = input("Enter your answer (A, B, C, or D): ").upper()

# check answer and give result
if guess == chr(answers.index(correct_answer) + 65):
    print("Correct!")
else:
    print("Incorrect. The correct answer was", correct_answer)

