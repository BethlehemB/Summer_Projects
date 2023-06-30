def replace_word():
    str = "hey guys its Beth"
    word_to_replace = input("what word would you like to replace: ")
    word_replacement = input("What word would like to replace it with: ")
    print(str.replace(word_to_replace,word_replacement))

replace_word()