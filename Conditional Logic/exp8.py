print('input the character: ')
character = input()

if character >= 'a' and character <= 'z':
    print('lowercase')
elif character >= 'A' and character <= 'Z':
    print('uppercase')
else:
    print('invalid')