"""Utility script to condense big CSV files columnwise.

I split up comments and suggestions into one column per topic by cutting and
pasting across in the spreadsheet. This leaves long columns with a lot of blank
space. To collapse the columns, I saved as a CSV file and ran this script on it.
"""

import csv
import itertools
from collections import defaultdict

fi = open("ipython_user_survey_comments.csv", "r")
dr = csv.DictReader(fi)

fo = open("ipython_user_survey_comments_collapsed.csv", "w")
cw = csv.writer(fo)

cw.writerow(dr.fieldnames)

columns = defaultdict(list)
for row in dr:
    for field, val in row.items():
        if val:
            columns[field].append(val)

cw.writerows(itertools.zip_longest(*[columns[field] for field in dr.fieldnames]))

fi.close()
fo.close()