s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
letters = dict()


for letter in s:
    letters[letter] = letters.get(letter, 0) + 1

for key, value in letters.items():
    print(f'{key} - {value}')