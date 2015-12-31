# -*- coding: utf-8 -*-

import os
import base64
import json
from eml_parser import eml_parser

json_dir = 'jsons/'

try:
    os.stat(json_dir)
except:
    os.mkdir(json_dir)

except1_cnt = 0
except2_cnt = 0

for k in os.listdir('.'):
    if k.endswith('.eml'):

        try:
            m = eml_parser.decode_email(k, include_attachment_data=True)
        except:
            except1_cnt += 1
            continue

        output_file = json_dir+k[:-4]+'.json'
        datetime = m['header']['date'].strftime('%y-%m-%d %H:%M')
        attachments = ''
        for a_id, a in m['attachments'].items():
            if a['filename'] == '':
                filename = a_id
            else:
                filename = a['filename']

            attachments += filename
            attachments += ' '

        data = {'datetime':datetime,'attachments':attachments}
        with open(output_file, 'w') as fp:
            try:
                json.dump(data, fp)
            except:
                except2_cnt += 1

print except1_cnt
print except2_cnt
