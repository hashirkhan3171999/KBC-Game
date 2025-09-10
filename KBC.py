import random
questions =[
    {"question": "Who won the men FIFA 2010 World Cup?", "options": ["England", "Germany", "Spain", "Brazil"], "answer": "Spain"},
    {"question": "Who won the men FIFA 2006 World Cup?", "options": ["France", "Germany", "Italy", "Brazil"], "answer": "Italy"}, 
    {"question": "Who won the men FIFA 2014 World Cup?", "options": ["France", "Germany", "Italy", "Argentina"], "answer": "Germany"},
    {"question": "Who won the men FIFA 2018 World Cup?", "options": ["France", "Germany", "Italy", "Argentina"], "answer": "France"},
    {"question": "Who won the men FIFA 2022 World Cup?", "options": ["France", "Germany", "Italy", "Argentina"], "answer": "Argentina"},
    {"question": "Who is the top goal scorer in history of football?", "options": ["Pele", "Maradona", "C.Ronaldo", "Messi"], "answer": "C.Ronaldo"},
    {"question": "Who has won the most Ballon d'Or awards?", "options": ["Pele", "Maradona", "C.Ronaldo", "Messi"], "answer": "Messi"},
    {"question": "Which country has won the most FIFA World Cups?", "options": ["Italy", "Germany", "Brazil", "Argentina"], "answer": "Brazil"},
    {"question": "Which club has won the most UEFA Champions League titles?", "options": ["Barcelona", "Real Madrid", "Bayern Munich", "AC Milan"], "answer": "Real Madrid"},
    {"question": "Who is known as 'Greatest Player of All Time (G.O.A.T)'?", "options": ["Pele", "Maradona", "C.Ronaldo", "Messi"], "answer": "Messi"}
]

# Shuffle the questions list.
random.shuffle(questions)

# This variable will keep track of the player's score. We start it at 0.
Score = 0

# This is a loop that goes through each question, one by one. 
# It's like going through a list of items and doing something with each one.
for question in questions:
    print(question["question"])
    
# Enumerate function adds a counter to an iterable like a list and shows the index along with the item. And i is the index.
# and option is the item in the list.
# 1 is the starting index.
    for i, option in enumerate(question["options"], 1):
# f is format string, which allow us to type variables and expressions inside string literals, using curly braces {}.
# f is calling literal string interpolation.
# Interpolation means inserting the value of variables or expressions into a string.
        print(f"{i}. {option}")
# we are asking the user for their answer and storing it in a variable called user_answer.
    user_answer = input("Enter your answer (just type the name): ")
# We are checking if the user's answer is the same as the correct answer.
# We are using the .lower() method to make the comparison case-insensitive.
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
# and we are increasing the score by 1.
        Score += 1
# If the answer is wrong, we are printing the correct answer.
    else:
        print(f"Incorrect. The correct answer is:, {question["answer"]}")
# This line prints a separator to make the quiz easier to read.        
# "- " is used to create a string of 25 hyphens. 25 hyp
    print("-" * 25)
# This line prints the final score after the quiz is completed. Out of len(questions) counts how many questions were in the list.
print("Your final score is:", Score, "out of", len(questions)) 
