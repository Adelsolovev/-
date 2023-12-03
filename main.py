def find_most_frequent_and_longest_word(text):
    # Разделение текста на слова
    words = text.split()

    # Создание словаря для подсчета встречаемости слов
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Поиск наиболее часто встречаемого слова
    most_frequent_word = max(word_counts, key=word_counts.get)

    # Поиск самого длинного слова
    longest_word = max(words, key=len)

    return most_frequent_word, longest_word


# Ввод текста от пользователя
text = input("Введите текст: ")

# Поиск наиболее часто встречаемого слова и самого длинного слова
most_frequent_word, longest_word = find_most_frequent_and_longest_word(text)

# Вывод результатов
print("Наиболее часто встречаемое слово:", most_frequent_word)
print("Самое длинное слово:", longest_word)
