def createEnglishLatinDictionary(englishLatinDictionary):
    latinEnglishDictionary = {}

    for englishWord, latinWords in englishLatinDictionary.items():
        for latinWord in latinWords:
            if latinWord not in latinEnglishDictionary:
                latinEnglishDictionary[latinWord] = []

            latinEnglishDictionary[latinWord].append(englishWord)

    return latinEnglishDictionary

numberEnglishWords = int(input('Number of English words >> '))
englishLatinDictionary = {}

for i in range(numberEnglishWords):
    line = input('English - Latin1, Latin2... words >> ').split(' - ')
    englishWord = line[0]
    latinWords = line[1].split(", ")
    englishLatinDictionary[englishWord] = latinWords

latinEnglishDictionary = createEnglishLatinDictionary(englishLatinDictionary)

sortedLatinWords = sorted(latinEnglishDictionary.keys())
print(len(sortedLatinWords))

for latinWord in sortedLatinWords:
    englishTranslations = sorted(latinEnglishDictionary[latinWord])
    print(latinWord, '-', ', '.join(englishTranslations))