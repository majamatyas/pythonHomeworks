import os
from datetime import date,timedelta
import random

#Exercise 5.1
def find_pdf_size(path):
    pdfSizes = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.lower().endswith(".pdf"):
                pdfSizes += os.path.getsize(os.path.join(root, name))
    print(pdfSizes)

# find_pdf_size(".")

#Exercise 5.2
def print_working_days(date1, date2):
    dateFormat1 = date.fromisoformat(date1)
    dateFormat2 = date.fromisoformat(date2)
    daygenerator = (dateFormat1 + timedelta(x) for x in range((dateFormat2 - dateFormat1).days))
    print(sum(1 for day in daygenerator if day.weekday() < 5))

print_working_days('2004-04-01', '2024-04-14')

#Exercise 5.2
def random_walk(start):
    i = 0
    currPos = start
    while i < 100:
        randomDirection = random.randrange(2)
        if randomDirection == 0:
            currPos +=1
            yield currPos
        else:
            currPos -=1
            yield currPos 
            
        i += 1

for i in random_walk(0):
    print(i)