# a - запись новых данных в конец файла
# w - только запись новых данных с удалением старых данных
# r - только чтение
# r+ - чтение, и запись в файл, НО курсор в файле стоит в самом начале,
# поэтому перезапись идёт поверх уже существующих данных в начале файла.
# Чтобы переместиться в конец файла и записать туда данные,
# нужно сначала сделать read(), затем write()

fr1 = open('doc/file3.txt', 'w')
fr1.write('w - writing only!\n')
fr1.close()

fr2 = open('doc/file3.txt', 'a')
fr2. write('a - append in the end!\n')
fr2.close()

fr3 = open('doc/file3.txt', 'r')
text = fr3.read()
fr3.close()
print(text)

fr4 = open('doc/file3.txt', 'r+')
fr4.read()
fr4.write('r+ - reading AND writing!')
fr4.close()

