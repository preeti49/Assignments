import csv

with open(r'C:\Users\DELL\OneDrive\Documents\GitHub\Assignments\17th_sep_assignmt.py\marks.csv', 'r') as f:
    r = csv.reader(f)
    for row in r:
        print(row)


        