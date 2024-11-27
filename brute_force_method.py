import itertools
from collections import Counter

ciphertext = "ХЯЪХЭЙОЪЛЙМЛЙБЕЩЛЯОБМАЛЙЧЙОХОЙЭТАЛЙЛЯПУБЙЩЯЙЗЕОХМЭНИФЙЙЕЛЪЛГЭПШЛЕАХФРААЁГЧЙЬХАБЫЧХЧБМЫМЙЗЙАБНБЕЩПЕШХОЙОБМЁХЯЪХЭЙОЫХЛСЙАТЯЙЗШБЧБЕШЭИСЙАБЙЧЩЯЙМЛЕЬЛЗБЭЛЪЁСАЁГЭПШЩЛОЛСАЛЕОБЕОЯЙЭТЪЁБПЪЛГАЛГЕБЭЙАЛШХШЩЯХМБЭЛЛАЕБЭТАЛЩЯЛБЦЯЁМХЭЭПШПЩЛЕШЛЯЛЕОЯЙЭТАЛЕОБЩЛЩПЭНЯАЛЕОБЕЩЛЕЛЪЕОМЛМХЭЛОЛСОЛЗЭНЛЪПСЙАБНЕОЯЙЭТЪЙБЫХЯЪХЭЙОХОЯЙЪЛМХЭЛЕТАХЧАЛЦЛЧЙАТЖЙМЯЙЧЙАБЩЛЕЯХМАЙАБИЕЛЪПСЙАБЙЧБЕШПЕЕОМПЕОЯЙЭТЪЁБЫЭПШХ"

letter_frequency = Counter(ciphertext)

# Сортировка букв по частоте
sorted_letters = [letter for letter, _ in letter_frequency.most_common()]

# Для простоты, берем только 10 самых частых букв
common_russian_letters = 'оеиаытнсрвлк'

for perm in itertools.permutations(common_russian_letters[:len(sorted_letters)]):
    substitution_dict = dict(zip(sorted_letters, perm))
    decrypted_text = ''.join(substitution_dict.get(char, char) for char in ciphertext)
    print(decrypted_text)
