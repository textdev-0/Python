start_sum = float(input('Current sum >> '))
target_sum = float(input('Target sum >> '))
intrest = float(input('Monthly intrest rate >> '))
final_sum = 0

print()
print('Testing...')

while start_sum < target_sum:
    final_sum += 1
    start_sum += start_sum/100*intrest
    print(f'Months: {final_sum}\nCurrent sum: {start_sum:0.2f}')

print()
print(f'Months taken: {final_sum}\nFinal sum: {start_sum:0.2f}')
#