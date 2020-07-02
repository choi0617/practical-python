# pcost.py
#
# Exercise 1.27


total = 0
with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        print('# of shares:', row[1], end='')
        
        p = row[2].split('\n')
        print(' price per share:', p[0])

        total += int(row[1]) * float(p[0])
        
print("Total:", total)       

        
        