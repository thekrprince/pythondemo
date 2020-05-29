
def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(" ")
    print(words)
    new_sentence = reversed(words)

    #First method
    #for word in new_sentence:
        #print(word.swapcase(), end=" ")

    #Second Method
    str = ""
    for word in new_sentence:
        if len(str)==0:
            str = word
        else:
            str = str + " " + word

    print(str.swapcase())


sentences = "aWESOME is cODING"
reverse_words_order_and_swap_cases(sentences)