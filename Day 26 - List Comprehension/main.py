import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dic_data = {row.letter:row.code for (index, row) in data.iterrows()}
user_input = input("Enter a word: ").upper()
output = [dic_data[letter] for letter in user_input]
print(output)

