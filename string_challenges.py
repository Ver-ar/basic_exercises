print("Задание №1\n")
# Вывести последнюю букву в слове
word = 'Архангельск'
print (word[-1])

print("______________________\n\nЗадание №2\n")


# Вывести количество букв "а" в слове
word = 'Архангельск'
print (len(word))

print("______________________\n\nЗадание №3\n")
# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'Ааиеёоуыэюя'

word_2 = word.lower()
count = 0
string=[]
for letter in vowels:
    if letter in word:
        string.append(letter)
count = len(string)

print (count)

print("______________________\n\nЗадание №4\n")
# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
count = len(sentence.split())

print(count)

print("______________________\n\nЗадание №5\n")
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
string_sentence = sentence.split()
for word in string_sentence:
    print(word[0])


print("______________________\n\nЗадание №6\n")
# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
string_sentence = sentence.split()
count_word = len(sentence.split())

        
sum_count=0    
for word in string_sentence:
    count_words=len(word)
    sum_count+=count_words
sum=sum_count/count_word
sum=int(sum)
    
print(f"Усреднённая длина слова в предложении: {sum}")
