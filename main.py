import random
import words
import states_list 

words_list = words.word_list
states_list = states_list.stages

def printList(l):
    for i in l:
        print(i, end=' ')
    print()


class Hangman:

    state = None
    tries = None
    guessed = False
    query_word = None
    answerWord = None

    def __init__(self, tries=6):        
        self.state = 6
        self.tries = tries
        #self.query_word = 'connection'
        self.query_word = random.choice(words_list)
        self.answerWord = list('_'*len(self.query_word))

    def display(self):
        #print(f'Your current state is {self.state}')
        #print(f'No. of tries left is: {self.tries}')
        print(states_list[self.state])
        print('\tThe answer Word is: ', end='')
        printList(self.answerWord)
        print()     


    def play(self):
        
        guessed_letters = []
        guessed_words = []

        while not self.guessed and self.tries >0 :
            print(f'\n==========================TRIES LEFT:{self.tries}===========================')
            print('guessed letters:', end='')
            printList(guessed_letters)
            print('guessed words:', end='')
            printList(guessed_words)

            self.display()
            inputString = input('Enter the letter:').lower()
            if len(inputString)==1 and inputString.isalpha():
                if inputString in guessed_letters:
                    print('You have already guessed this letter')
                elif inputString in self.query_word:
                    for i in range(len(self.query_word)):
                        if inputString==self.query_word[i]:
                            self.answerWord[i]=inputString
                    guessed_letters.append(inputString)
                else:
                    self.state -= 1
                    guessed_letters.append(inputString)

                if self.query_word == ''.join(self.answerWord):
                    self.guessed = True

                self.tries -= 1
            elif len(inputString)>1 and inputString.isalpha():
                if inputString in guessed_words:
                    print('You have already guessed this word')
                elif inputString == self.query_word:
                    self.guessed = True
                else:
                    self.state -= 1

                self.tries -= 1
            else:
                print('Enter a valid letter!!')
        #print(f'!!!!{self.query_word} {self.answerWord}')
        if self.guessed :
            print(f'Hooray, You solved the puzzle.')
        else:
            print(states_list[0])
            print(f'You couldnt save the man. You Lost!\nThe word is {self.query_word}')


if __name__ == "__main__":
    
    game = Hangman()
    game.play()

    while input('Press Y to Play Again, Press Any other key to Quit:').lower()=='y':
        game = Hangman()
        game.play()
    