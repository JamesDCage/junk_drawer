"""
Practicing nested comprehensions
"""

word_list = ["the", "quick", "red", "fox", "jumped", "over", "the", "lazy", "brown", "dog"]

# WITHOUT COMPREHENSIONS

long_list = []

for word in word_list:
    if not len(word)%2:
        for letter in word:
            if letter < 'x':
                long_list += letter


# WITH COMPREHENSION
# Start with what you want, work from outside-in

letter_list = [letter for word in word_list if not len(word)%2 for letter in word if letter < 'x']


print("letter list", letter_list)
print("long list", long_list)

letter_set = set(letter_list)
# If set is the desired output, could create directly as a set comprehension

print("letter set", letter_set)