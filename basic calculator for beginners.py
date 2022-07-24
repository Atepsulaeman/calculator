"""basic calculator for beginners by Atep Sulaeman"""
# Membuat Inputan User # Creating User Input
print('='* 25)
print('math operations')
print('1. amount \t [+]')
print('2. subtract \t [-]')
print('3. multiplication   \t [*]')
print('4. distribution  \t [/]')
print('='* 25)

operation = input ('select operation (1/2/3/4):')
number_1 = eval(input('enter first value:'))
number_2 = eval(input('enter second value:'))


# Membuat percabangan dasar # Make basic branch
print('=' * 25)

if operation == '1':
  print('User selects sum')
elif operation == '2':
  print('User selects subtraction')
elif operation == '3':
  print('User selects multiplication')
elif operation == '4':
  print('User chooses share')
else:
  print('Tidak valid')

  # Menghitung dan Menampilkan Hasil Operasi  # Calculating and Displaying Operation Results

if operation == '1':
  results = number_1 + number_2
  print(f'Result of operation from {number_1} + {number_2} = {results}')
elif operation == '2':
  results = number_1 - number_2
  print(f'Result of operation from {number_1} - {number_2} = {results}')
elif operation == '3':
  results = number_1 * number_2
  print(f'Result of operation from {number_1} * {number_2} = {results}')
elif operation == '4':
  results = number_1 / number_2
  print(f'Result of operation from {number_1} / {number_2} = {results}')
else:
  print('no valid')

