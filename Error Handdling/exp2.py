try:
    with open('write.text', 'r') as myFile:
        content = myFile.read()
        print(content)
except:
    print('The file does not exist.')

print('hello!!')