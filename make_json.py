import os
import base64
import json
from eml_parser import eml_parser

json_dir = 'jsons/'

try:
    os.stat(json_dir)
except:
    os.mkdir(json_dir)

except_cnt = 0

for k in os.listdir('.'):
    if k.endswith('.eml'):

        try:
            m = eml_parser.decode_email(k, include_attachment_data=True)
        except:
            except_cnt += 1
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
            json.dump(data, fp)

print except_cnt
