#Python Quiz Game

import time

questions = ("Which scientist proposed the three laws of motion?", 
             "Which branch of philosophy deals with the nature of knowledge and how we know things?", 
             "What is the smallest unit of an element that retains its chemical properties?", 
             "Which fundamental force is responsible for keeping planets in orbit around the Sun?", 
             "Which philosopher was the teacher of Alexander the Great?",
             "What is the speed of light in a vacuum?", 
             "Which philosophical school teaches that happiness is achieved through virtue and living according to reason?", 
             "DNA is primarily responsible for: " )      
    
options = (("A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"),
           ("A. Ethics", "B. Metaphysics", "C. Epistemology", "D. Logic"),
           ("A. Molecule", "B. Proton", "C. Atom", "D. Electron"),
           ("A. Electromagnetic Force", "B. Strong Nuclear Force", "C. Weak Nuclear Force", "D. Gravity"),
           ("A. Socrates", "B. Aristotle", "C. Plato", "D. Pythagoras"),
           ("A. 300,000 km/s", "B. 150,000 km/s", "C. 30,000 km/s", "D. 3,000 km/s"),
           ("A. Existentialism", "B. Stoicism", "C. Nihilism", "D. Utilitarianism"),
           ("A. Producing energy", "B. Carrying genetic information", "C. Pumping blood", "D. Digesting food"))

answers = ["B","C","C", "D", "B", "A", "B", "B" ]
guesses = []
statuses = []
question_num = 0
score = 0
numbers = ["Question","1", "2", "3", "4", "5", "6", "7", "8"]
print("--------------------------------------------------------")
print("Your QUIZ Starts Now!!!")
print("--------------------------------------------------------")

time.sleep(2)

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    print("--------------------------------------------------------")
    guess = input("Enter Your Answer (A, B, C, D) : ").upper()
    while guess != "A" and guess != "B" and guess != "C" and guess != "D" :
        print("Invalid Guess")
        guess = input("Enter Your Answer (A, B, C, D) : ").upper()
    

    guesses.append(guess)

    if guess == answers[question_num]:
        score +=1
        status = "Correct"
        statuses.append(status)
        print("Correct Answer")
    else:
        status = "Incorrect"
        statuses.append(status)
        print(f"{guess} is incorrect.")
        print(f"Correct Answer is {answers[question_num]}")
    print("--------------------------------------------------------")
    time.sleep(1)

    question_num +=1

print()
print("Summary Of Your Quiz")


answers.insert(0, "Answers")
guesses.insert(0, "Guesses")
statuses.insert(0,"Status")

for y in range (0,9) :
    print(f"{numbers[y]:^7}", end=" ")
    print(f"{guesses[y]:^7}", end=" ")
    print(f"{answers[y]:^7}", end=" ")
    print(f"{statuses[y]:^8}", end=" ")
    print()

print(f"You got {score} questions correct out of 8 questions")

score = score/8 * 100

print(f"Your final score is {score}%")


              