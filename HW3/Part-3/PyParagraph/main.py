import csv

filepath = 'raw_data/paragraph_1.txt'

sentence_count = 0
word_count = 0
letter_count = 0

with open(filepath) as csvfile:
    reader = csv.reader(csvfile, delimiter = '.')
    for row in reader:
        for sentence in row:
            sentence_count += 1
            w = sentence.split()
            for word in w:
                word_count += 1
                for letter in word:
                    letter_count += 1
                
sentence_length = round(word_count/sentence_count, 1)
word_length = round(letter_count/word_count, 1)


print('Paragraph Analysis')
print('-----------------')
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'Average Letter Count: {word_length}')
print(f'Average Sentence Length: {sentence_length}')
