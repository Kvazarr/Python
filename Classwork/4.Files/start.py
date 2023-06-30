file1 = open('4.Files/file1.txt', 'w')
file1.write(f'Load up on guns, bring your friends, Its fun to lose and to pretend')
file1.close()

file1 = open('4.Files/file1.txt','r')
text = file1.read()
text=text.split()
file1.close()

file2 = open('4.Files/file2.txt','w')
file2.write(f'Load guns your')
file2.close()

file2 = open('4.Files/file2.txt','r')
text2 = file2.read()
text2 = text2.split()
file2.close()

file3 = open('4.Files/file3.txt','r')
text3 = file3.read()
file3.close()

text = []
text3 = []

for text2 in text:
    check = 0
    if text2 == text:
        check ==1
    if check == 0:
        text3.append(text)