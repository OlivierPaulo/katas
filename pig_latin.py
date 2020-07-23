def pig_it(text):
    #your code here
    words = text.split(" ")
    new_sent = []
    for word in words:
        if str.isalpha(word): 
            new_word = word[1:]+word[0]+"ay"
            new_sent.append(new_word)
        else:
            new_sent.append(word)
        
    return (" ").join(new_sent)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))