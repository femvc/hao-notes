# coding=utf8
clippings_file = open('My Clippings.txt', 'r')
all_lines = clippings_file.read()
clippings_file.close()

clippings = all_lines.split('==========\r\n')

book_name = ''
book_file = open('temp.txt', 'w')
for clip in clippings:
    lines = clip.split('\r\n')
    if book_name != lines[0]:
        book_file.close()
        book_name = lines[0]
        book_file = open(book_name + '.md', 'w')
        book_file.write("##" + book_name + '\r\n\r\n')
    book_file.write('\r\n'.join(lines[1: ]))
    book_file.write('\r\n')
