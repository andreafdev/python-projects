print("Welcome to AstroQuiz!")
answer_user = input('Do you want to start now? (Yes/No): ')

if answer_user != "Yes":
    quit('Who knows later, right?')

print('Let\'s begin!')
score = 0  # Inicializa a pontuação

# Pergunta 1
print('What is the largest planet in the Solar System? \n (A) Saturn \n (B) Jupiter \n (C) Neptune \n (D) Uranus \n')
answer_1 = input("Answer: ").upper()
if answer_1 == "B":
    print('Correct. Amazing!')
    score += 1  # Incrementa a pontuação
else:
    print('Wrong answer.')

# Pergunta 2
print('Which planet is known as the "Red Planet"? \n (A) Mars \n (B) Mercury \n (C) Venus \n (D) Earth')
answer_2 = input("Answer: ").upper()
if answer_2 == "A":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 3
print('What is the name of the galaxy where the Solar System is located? \n (A) Andromeda \n (B) Milky Way \n (C) Sombrero Galaxy \n (D) Magellanic Clouds')
answer_3 = input("Answer: ").upper()
if answer_3 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 4
print('What is a black hole? \n (A) A comet \n (B) A region of space where gravity is so strong that nothing can escape \n (C) A star about to explode \n (D) A planet without atmosphere')
answer_4 = input("Answer: ").upper()
if answer_4 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 5
print('What celestial body orbits the Earth and influences tides? \n (A) The Sun \n (B) The Moon \n (C) Mars \n (D) Venus')
answer_5 = input("Answer: ").upper()
if answer_5 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 6
print('How many planets are there in the Solar System? \n (A) 7 \n (B) 8 \n (C) 9 \n (D) 10')
answer_6 = input("Answer: ").upper()
if answer_6 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 7
print('What is the Sun primarily composed of? \n (A) Oxygen and nitrogen \n (B) Helium and hydrogen \n (C) Carbon and helium \n (D) Hydrogen and carbon dioxide')
answer_7 = input("Answer: ").upper()
if answer_7 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 8
print('Which planet is known for its beautiful rings? \n (A) Jupiter \n (B) Neptune \n (C) Saturn \n (D) Uranus')
answer_8 = input("Answer: ").upper()
if answer_8 == "C":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 9
print('What do we call the path a planet takes around the Sun? \n (A) Orbit \n (B) Rotation \n (C) Revolution \n (D) Axis')
answer_9 = input("Answer: ").upper()
if answer_9 == "A":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Pergunta 10
print('Which planet is the hottest in the Solar System? \n (A) Mercury \n (B) Venus \n (C) Mars \n (D) Jupiter')
answer_10 = input("Answer: ").upper()
if answer_10 == "B":
    print('Correct. Amazing!')
    score += 1
else:
    print('Wrong answer.')

# Exibe a pontuação final
print(f"You've completed the AstroQuiz! Your final score is {score}/10.")
