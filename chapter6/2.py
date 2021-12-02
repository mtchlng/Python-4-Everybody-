def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)


x=input('Enter word: ')
y=input('Enter letter to search: ')
count(x, y)
