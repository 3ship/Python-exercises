# Test
newFile = open('output.txt', 'w')
addText = input('Text eingeben: ')
if addText == 'exit':
    exit()
newFile.write(addText)
newFile.close()