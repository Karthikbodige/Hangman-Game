import random 

words=["cat","dog"]

word= random.choice(words)

guessed_word =['_']* len(word)

attempts = 6

while attempts > 0:
    print(' '.join(guessed_word))
    guess =input("guess a letter:").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] =guess
    else:
        attempts -= 1
        print(f"incorrect! attempts left:{attempts}")
    if '_'not in guessed_word:
        print(f"congratulations! you guessed the wor'{word}'!")
if attempts == 0:
    print(f"game over! the word was'{word}'.")