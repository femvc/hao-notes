# coding=utf8

import sys
import os
import datetime


# whether show the time detail like: Added on Wednesday, February 22, 2012, 08:44 PM
# if time_detail is False, then the .md output will be: Added on Wednesday, February 22, 2012, PM
# exactly no hour details.
show_time_detail = False

print "Show the time detail like '08:20 AM' ? (y/n): "
show_time_detail = True if raw_input() == 'y' else False

print "Type your Send_To_Kindle email address to hide it: "
SEND_TO_KINDLE_EMAIL = raw_input().strip()
hide_SendToKindle_email = True

if SEND_TO_KINDLE_EMAIL == '' \
        or not SEND_TO_KINDLE_EMAIL.endswith('.com'):
    hide_SendToKindle_email = False

clippings_path = sys.argv[1]
clippings = []
with open(clippings_path, 'r') as clippings_file:
    clippings = clippings_file.read().split('==========\r\n')[:-1] # the last one is '', so...

dir_path = str(datetime.date.today())
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

book_name = ''
book_file = open('tmp', 'w')
for clip in clippings:
    lines = clip.split('\r\n')
    if hide_SendToKindle_email and lines[0].find(SEND_TO_KINDLE_EMAIL) > -1:
        lines[0] = lines[0].replace(SEND_TO_KINDLE_EMAIL, 'Personal_Document')

    if book_name != lines[0]:
        book_file.close()
        book_name = lines[0]
        print book_name
        book_file = open('%s/%s.md' % (dir_path, book_name), 'a')
        book_file.write("##" + book_name + '\n\n')

    clip_info = lines[1]
    if not show_time_detail:
        clip_info = clip_info[:-8] + clip_info[-2:]
    book_file.write('\n%s\n' % clip_info)
    book_file.write('\n'.join(lines[2:]))
    book_file.write('\n\n')
book_file.close()
if os.path.exists('tmp'):
    os.remove('tmp')
