import random

#enumerate ㄷㄷ

file = open('listofprogramminglanguage.txt', 'r')
wordlist = list(map(lambda x: x.rstrip(), file))
file.close()

selected = random.choice(wordlist).lower()
guess = ['_' for _ in range(len(selected))]
life = 8
history = set()

print('*'*50)
print('''
   H    H   A   N   N GGGGG M   M   A   N   N
   H    H  A A  NN  N G     MM MM  A A  NN  N
   HHHHHH A   A N N N G GGG M M M A   A N N N
   H    H AAAAA N  NN G   G M   M AAAAA N  NN
   H    H A   A N   N GGGGG M   M A   A N   N
''')
print('*'*50)


def ending_message(text: str):
    print('*'*50)
    print()
    print(text)
    print()
    print('*'*50)


while life > 0:
    print()
    print(' '.join(guess))
    print("Your life left:",life)
    _input = input('> ')

    if len(_input) != 1:
        print("Just one Letter required..")
        continue
    
    if not _input.isalpha():
        print("Better use alphabetical word..")
        continue

    _input = _input.lower()

    if _input in history:
        print("You already tried that letter..")
        print("What you tried:", " ".join(history))
        continue

    history.add(_input)

    if _input in selected:
        for i in range(len(guess)):
            if selected[i] == _input:
                guess[i] = _input
        
        flag = True
        for i in range(len(selected)):
            if guess[i] != selected[i]:
                flag = False
                break

        if flag:
            ending_message(f'{selected} !\nYou won!')
            exit()

    else:
        life -= 1

ending_message(f'Game Over!\nThe word was: {selected}')