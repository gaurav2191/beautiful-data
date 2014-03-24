# Add new tags to tag.txt

import os
import csv

tags = []
with open('tag.txt', 'w') as fout:
    for file in os.listdir('SO_data'):
        if file.endswith('.json'):
            tags.append(file[:file.find('.json')])
    tags = [tag.lower() for tag in tags]
    fout.write(str(sorted(tags)).replace("'",'"'))
    fout.close()