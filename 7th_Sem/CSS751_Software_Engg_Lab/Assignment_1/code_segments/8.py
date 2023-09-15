# all in one

from goto import label, goto

label .lab
for i in range(20):
    c = 1
    while(c < 2):
        while(c < 3):
            c += 1
    if(i == 9):
        continue
    if(i == 11):
        break
    goto .lab
