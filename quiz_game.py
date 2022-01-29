# Validate user want to play or not?
play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()

print("\n\tOk let's start!!\n")

# Quiz questions stored in Dictionary
questions = {
    "Q1":"What does stand for RAM",
    "Q2":"What does stand for CPU"
    }

# Answer is stored in List
Q1_options = ["a) Random Access Memory", "b) Read Access Memory"]
Q2_options = ["a) Central Process Unit", "b) Central Processing Unit"]

# Score counter
score = 0

# Questions show to user through loop
for x in questions:
    if x == "Q1":
        print("Q-1 " + questions[x] + "\n")
        for y in Q1_options:
            print("\t" + y)
        answer = input("\nEnter your option: ")
        if answer.lower() == "a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    if x == "Q2":
            print("\nQ-2 " + questions[x] + "\n")
            for y in Q2_options:
                print("\t" + y)
            answer = input("\nEnter your option: ")
            if answer.lower() == "b":
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

# How many questions are answered
print("\nYou got " + str(score) + " queations correct")

# Score in percentage
print("You got " + str((score / len(questions)) * 100) + "%.")      
