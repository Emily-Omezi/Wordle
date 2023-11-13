import random
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def main():
    # Get a random word.
    answer = getRandomWord()
    player_mode=input('Single or Two-player mode?')
    if player_mode=='Single' or player_mode=='single':
        mode=input('Would you like to play Normal or hard mode?')
        if mode=='normal' or mode=='Normal' or mode=='Easy' or mode=='easy':
            attempts=0
            guess=''
            print('You chose Normal Mode: You have 6 chances to guess the word.')
            while guess.lower()!=answer and attempts<6:
                guess=input('Enter a 5 letter guess?\n')
                while len(guess)<5 or len(guess)>5:
                    print('Please try again')
                    guess=input('Enter a 5 letter guess?\n')
                for i in range(len(answer)): 
                    if answer[i]==guess[i].lower():
                        print (bcolors.OKGREEN+f'{guess[i]}'+ bcolors.ENDC)
                    elif guess[i].lower() not in answer:
                        print(bcolors.FAIL+f'{guess[i]}'+ bcolors.ENDC)
                    else:
                        print(bcolors.WARNING+f'{guess[i]}'+ bcolors.ENDC)
                attempts+=1
            if guess.lower()==answer or guess==answer.upper(): 
                print(f'You Won! That took {attempts} guess(es).')
            else:  
                print(f'You lost. The answer was {answer}.')
        else:
            attempts=0
            guess=''
            print('You chose Hard Mode: You now have 5 chances to get the word.')
            while guess!=answer and attempts<5:
                guess=input('Enter a 5 letter guess?\n')
                while len(guess)<5 or len(guess)>5:
                    print('Please try again')
                    guess=input('Enter a 5 letter guess?\n')
                for i in range(len(answer)): 
                    if answer[i]==guess[i].lower():
                        print (bcolors.OKGREEN+f'{guess[i]}'+ bcolors.ENDC)
                    elif guess[i].lower() not in answer:
                        print(bcolors.FAIL+f'{guess[i]}'+ bcolors.ENDC)
                    else:
                        print(bcolors.WARNING+f'{guess[i]}'+ bcolors.ENDC)
                attempts+=1
            if guess.lower()==answer or guess==answer.upper(): 
                print(f'You Won! That took {attempts} guess(es).')
            else:  
                print(f'You lost. The answer was {answer}.')
                player_1_word=input('Player 1 enter your word:')

    else:
        player_1_word=input('Player 1 enter your word: ')
        print('\n\n\n\n\n\n\n\n\n\n\n\n')
        print('-'*len(player_1_word)+'    <- this is the # of letters')   
        mode=input('Would you like to play Normal or hard mode?')
        if mode=='normal' or mode=='Normal':
            attempts=0
            guess=''
            print('You chose Normal Mode: You have 6 chances to get the word.')
            while guess!=player_1_word and attempts<6:
                guess=input('Enter your guess:\n')
                for i in range(len(player_1_word)): 
                    if player_1_word[i]==guess[i]:
                        print (bcolors.OKGREEN+f'{guess[i]}'+ bcolors.ENDC)
                    elif guess[i] not in player_1_word:
                        print(bcolors.FAIL+f'{guess[i]}'+ bcolors.ENDC)
                    else:
                        print(bcolors.WARNING+f'{guess[i]}'+ bcolors.ENDC)
                attempts+=1
            if guess==player_1_word.upper() or guess.lower()==player_1_word: 
                print(f'You Won! That took {attempts} guess(es).')
            else:  
                print(f'You lost. The answer was {player_1_word}.')
        else:
            attempts=0
            guess=''
            print('You chose Hard Mode: You now have 5 chances to get the word.')
            while guess!=player_1_word and attempts<5:
                guess=input('Enter a guess?\n')
                for i in range(len(player_1_word)): 
                    if player_1_word[i]==guess[i].lower():
                        print (bcolors.OKGREEN+f'{guess[i]}'+ bcolors.ENDC)
                    elif guess[i].lower() not in player_1_word:
                        print(bcolors.FAIL+f'{guess[i]}'+ bcolors.ENDC)
                    else:
                        print(bcolors.WARNING+f'{guess[i]}'+ bcolors.ENDC)
                attempts+=1
            if guess.lower()==player_1_word: 
                print(f'You Won! That took {attempts} guess(es).')
            else:  
                print(f'You lost. The answer was {player_1_word}.')

# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
