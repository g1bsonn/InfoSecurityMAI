import collections
import re


def letter_frequency_analysis(text):
    cleaned_text = re.sub(r'[^а-яё]', '', text.lower())
    frequency = collections.Counter(cleaned_text)
    total_count = sum(frequency.values())
    return total_count, frequency


cipher_text = '''
ХЯЪХЭЙОЪЛЙМЛЙБЕЩЛЯОБМАЛЙЧЙОХОЙЭТАЛЙЛЯПУБЙЩЯЙЗЕОХМЭНИФЙЙЕЛЪЛГЭПШЛЕАХФРААЁГЧЙЬХАБЫЧХЧБМЫМЙЗЙАБНБЕЩПЕШХОЙОБМЁХЯЪХЭЙОЫХЛСЙАТЯЙЗШБЧБЕШЭИСЙАБЙЧЩЯЙМЛЕЬЛЗБЭЛЪЁСАЁГЭПШЩЛОЛСАЛЕОБЕОЯЙЭТЪЁБПЪЛГАЛГЕБЭЙАЛШХШЩЯХМБЭЛЛАЕБЭТАЛЩЯЛБЦЯЁМХЭЭПШПЩЛЕШЛЯЛЕОЯЙЭТАЛЕОБЩЛЩПЭНЯАЛЕОБЕЩЛЕЛЪЕОМЛМХЭЛОЛСОЛЗЭНЛЪПСЙАБНЕОЯЙЭТЪЙБЫХЯЪХЭЙОХОЯЙЪЛМХЭЛЕТАХЧАЛЦЛЧЙАТЖЙМЯЙЧЙАБЩЛЕЯХМАЙАБИЕЛЪПСЙАБЙЧБЕШПЕЕОМПЕОЯЙЭТЪЁБЫЭПШХ
'''

total_letters, letter_frequencies = letter_frequency_analysis(cipher_text)

sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)


def find_most_frequent_ngrams(text, n):
    ngrams = []
    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i + n])
    ngram_counts = collections.Counter(ngrams)
    most_frequent = ngram_counts.most_common()
    return most_frequent

bigrams = find_most_frequent_ngrams(cipher_text, 2)
trigrams = find_most_frequent_ngrams(cipher_text, 3)
print("Наиболее часто встречающиеся биграммы:")
for bigram, count in bigrams:
    print(f"{bigram}: {count}")
print("\nНаиболее часто встречающиеся триграммы:")
for trigram, count in trigrams:
    print(f"{trigram}: {count}")

print(f"Общее количество букв: {total_letters}")
print("Частоты встречаемости букв:")
for char, count in sorted_frequencies:
    print(f"{char}: {count}")
print("\nЗашифрованный текст:\n", cipher_text)

substitution = {
    'Л': 'е', 'Й': 'с', 'Б': 'о', 'Е': 'я', 'А': 'т', 'Э': 'в', 'Х': 'а', 'О': 'р',
    'Я': 'п', 'М': 'м', 'Ъ': 'н', 'П': 'г', 'Щ': 'д', 'Ш': 'и', 'Ч': 'у', 'Т': 'ь',
    'Ё': 'ч', 'С': 'к', 'З': 'л', 'Н': 'з', 'Г': 'б', 'Ы': 'ы', 'И': 'й', 'Ф': 'х',
    'Ь': 'ж', 'Ц': 'ш', 'У': 'ю', 'Р': 'ц', 'Ж': 'щ'
}


def decrypt_text(text, substitution_table):
    decrypted_text = ''
    for char in text:
        if char in substitution_table:
            decrypted_text += substitution_table[char]
        else:
            decrypted_text += char
    return decrypted_text


decrypted_message = decrypt_text(cipher_text, substitution)

print("\nРасшифрованный текст:\n")
print(decrypted_message)

#ЕО: 10
#ЛЕ: 10
#АЛ: 9
#ЯЙ: 9
#ЙА: 9
#ЙАБ: 6
#ЙЭТ: 5
#ОЯЙ: 5
#    'Л': 'о', 'Й': 'е', 'Б': 'т', 'Е': 'я', 'А': 'с', 'Э': 'в', 'Х': 'а', 'О': 'р',
#    'Я': 'х', 'М': 'м', 'Ъ': 'н', 'П': 'г', 'Щ': 'д', 'Ш': 'и', 'Ч': 'у', 'Т': 'ь',
#    'Ё': 'ч', 'С': 'к', 'З': 'л', 'Н': 'з', 'Г': 'б', 'Ы': 'ы', 'И': 'й', 'Ф': 'п',
#    'Ь': 'ж', 'Ц': 'ш', 'У': 'ю', 'Р': 'ц', 'Ж': 'щ'