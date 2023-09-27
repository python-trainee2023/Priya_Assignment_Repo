def count_words():
    try:
        with open("words.txt", "r") as file:
            text = file.read()
            all_words_in_file = text.split()
            word_count = 0

            for word in all_words_in_file:
                clean_word = word.strip('')
                if clean_word.endswith('e'):
                    word_count += 1
                    print("Number of words ending with 'e' :", word_count)

    except FileNotFoundError:
        print("The specified file is not found")

count_words()


