print('Number of primes:')
amountOfPrimes = int(input('>> '))
print()
print('Finding primes...')

def isItPrime(number=1):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

currentNumber = 1
primesFound = 0
whatPrimes = ''
while primesFound != amountOfPrimes:
    currentNumber += 1
    if isItPrime(currentNumber):
        primesFound += 1
        whatPrimes += str(f'{currentNumber} ')
print('Done!')

print()
print('Writing primes to file primes.txt...')
with open('primes.txt', 'w') as file:
    file.write(whatPrimes)
print('Finished!')