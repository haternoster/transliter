def transform_letter(letter):
    # Словарь для соответствия клавиш
    key_mapping = {
        'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у',
        'f': 'а', 'g': 'п', 'h': 'р', 'i': 'ш', 'j': 'о',
        'k': 'л', 'l': 'д', 'm': 'ь', 'n': 'т', 'o': 'щ',
        'p': 'з', 'q': 'й', 'r': 'к', 's': 'ы', 't': 'е',
        'u': 'г', 'v': 'м', 'w': 'ц', 'x': 'ч', 'y': 'н',
        'z': 'я', '@': '"', '#': '№', '$': ';', '^': ':',
        '&': '?'
    }
    lower_cased = letter.lower()

    # Преобразование буквы с учетом регистра
    if lower_cased in key_mapping:
        transformed = key_mapping[lower_cased]
        return transformed.upper() if letter.isupper() else transformed
    else:
        return letter

def transform_word(word):
    # Преобразование каждой буквы в слове
    transformed_word = ""
    for letter in word:
        transformed_word += transform_letter(letter)
    return transformed_word

def word_counter(text):
    number_of_words = len(text.split(" "))
    return number_of_words



def main():
    input_word = input("Введите слово: ")
    result = transform_word(input_word)
    print(result)


if __name__ == "__main__":
    main()
