

userword= input("Enter a word:")
userword=userword.upper()
Vowels=['A','E','I','O','U']
for letter in userword:
    #if letter==['A' or 'E' or 'I' or 'O' or 'U']:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter)


