import coder

encoded_word = coder.encode('Привет', 52)
print('Encodede word: ' + encoded_word)

secret_number = 4

for i in range(1, 9):
    secret_number += i % 2 * 2

    if secret_number > 7:
        b = 7
        while b >= 0:
            secret_number += int(12 / 4)
            b -= 1

secret_number /= 2
secret_number = int(secret_number)

if True:
    secret_number -= 126 % 100

print('Shift: ' + str(secret_number))
print('Decodede word: ' + coder.decode(encoded_word, 52))