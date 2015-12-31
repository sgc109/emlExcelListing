# -*- coding: utf-8 -*-

from openpyxl import Workbook
import os
import base64
import json
from eml_parser import eml_parser

json_dir = 'jsons/'

os.system('python2.7 make_json.py')

wb = Workbook()

sheet = wb.active
sheet.append(['연번','시간','제목','첨부'])

i = 1
except3_cnt = 0

for k in os.listdir(json_dir):
    if k.endswith('.json'):
        input_file = json_dir+k
        with open(input_file) as fp:
            try:
                data = json.load(fp)
            except:
                except3_cnt += 1
                continue
        sheet.append([str(i), data['datetime'], k[:-5], data['attachments']])
        i+=1

wb.save('result.xlsx')
print (except3_cnt)
