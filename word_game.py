word = list(input("Enter the word: "))
print(word)
a = len(word)
n = ["_" for x in word]
print(n)

for x in range(a + 2):
    letter = input("Guess the letter: ")
    print("Letter entered:", letter)
    if letter in word:
        print("Letter is present")
        for i in range(a):
            if word[i] == letter:
                n[i] = letter
                print(n)
        if n == word:
            print("You won!")
            break
    else:
        print("Not present")
else:
    if n != word:
        print("You lost")



    

