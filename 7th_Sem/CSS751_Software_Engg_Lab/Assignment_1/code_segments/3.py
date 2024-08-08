# nested-while loop

i = 0
j = 0
while( i < 10):
    while ( j <= i):
        print(j, end = ' ')
        j = j+1
    print('\n')
    j = 0
    i = i+1