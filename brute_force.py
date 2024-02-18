import itertools

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
target_password = 'lalit'

# Brute force attack
for length in range(1, 9):  # Assume maximum password length of 8
    for guess in itertools.product(characters, repeat=length):
        guess = ''.join(guess)
        if guess == target_password:
            print("Password cracked:", guess)
            break
