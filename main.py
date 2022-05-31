# Quiz Game by Pierre Van Monckhoven

print("1. General Culture")
print("2. Math")
print("3. Grammar")

choice = input('Select a category: ')


# Define a choice input by player

if choice == "General Culture":
    def quiz_for_general_culture():

        # First quiz

        print('What is the capital of South Korea?')
        choose = input("1. Seoul; 2. Tokyo; 3. Hong Kong; 4. Bangkok: ")

        if choose == 'Seoul':
            print('Pass')

        elif choose == 'Tokyo':
            print('Fail')
        
        elif choose == 'Hong Kong':
            print('Fail')
        
        elif choose == 'Bangkok':
            print('Fail')


        # Second quiz

        print('What is the Lasagna?')
        choose1 = input("1. A Italian pasta; 2. A Russian drink; 3. A Korean breakfast: ")

        if choose1 == 'A Italian pasta':
            print('Pass')
        elif choose1 == 'A Russian drink':
            print('Fail')

        elif choose1 == 'A Korean breakfast':
            print('Fail')

        
        # Third Quiz

        print('What is the "La Divina Commedia"?')
        choose2 = input('1. A popular italian book; 2. A book of french literature; 3. A program for PC: ')

        if choose2 == 'A popular italian book':
            print('Pass')
        
        elif choose2 == 'A book of french literature':
            print('Fail')

        elif choose2 == 'A program for PC':
            print('Fail')


        # Fourth Quiz

        print('What is the largest ocean in the world?')
        choose3 = input('1. The Pacific ocean; 2. A famous American sea; 3. A international team of basket: ')

        if choose3 == 'The Pacific ocean':
            print('Pass')

        elif choose3 =='A famous American sea':
            print('Fail')

        elif choose3 == 'A international team of basket':
            print('Fail')


        # Fifth Quiz

        print('What is the most spoken language?')
        choose4 = input('1. Mandarin chinese; 2. English language; 3. The Arabic language: ')

        if choose4 == 'Mandarin chinese':
            print('Pass')

        elif choose4 == 'English language':
            print('Fail')

        elif choose4 == 'The Arabic language':
            print('Fail')

        print('The quiz for General Culture is finished.')

            
    quiz_for_general_culture()



if choice == 'Math':
    def math_quiz():

        # First math quiz

        print('How much is 8 X 9?')
        choose = int(input('1. 72; 2. 99; 3. 45: '))

        if choose == 72:
            print('Pass')

        elif choose == 99:
            print('Fail')

        elif choose == 45:
            print('Fail')


        # Second quiz

        print('How much is 7 raised to 2?')
        choose1 = int(input('1. 32; 2. 49; 3. 56: '))

        if choose1 == 49:
            print('Pass')

        elif choose1 == 32:
            print('Fail')

        elif choose1 == 56:
            print('Fail')

        # Third Quiz

        print('How much is 5 * 2 - 4?')
        choose2 = int(input('1. 9; 2. 0; 3. 6: '))

        if choose2 == 6:
            print('Pass')

        elif choose2 == 0:
            print('Fail')

        elif choose2 == 9:
            print('Fail')


        print('The quiz for math is complete')



    math_quiz()



if choice == "Grammar":
    def grammar_quiz():
        
        # First Grammar Quiz

        print("What is ' Il ' in italian language?")
        choose = input('1. The definite article; 2. The indefinite article; 3. An adjective: ')

        if choose == 'The definite article':
            print("Pass")

        elif choose == 'The indefinite article':
            print("Fail")

        elif choose == 'An adjective':
            print("Fail")


        # Second Grammar Quiz

        print("What is ' Un ' in italian language?")
        choose = input('1. A verb; 2. An adjective; 3. The indefinite article: ')

        if choose == 'The indefinite article':
            print("Pass")

        elif choose == 'An adjective':
            print("Fail")

        elif choose == 'A verb':
            print("Fail")


        # Third Grammar Quiz

        print("What is ' A ' in italian language?")
        choose = input('1. A simple preposition; 2. A verb; 3. A unfined verb: ')

        if choose == 'A simple preposition':
            print("Pass")

        elif choose == 'A verb':
            print("Fail")

        elif choose == 'A unfined verb':
            print("Fail")



    grammar_quiz()

print("Thank you for playing this quiz game")
