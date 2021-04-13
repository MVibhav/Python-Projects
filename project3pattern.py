def pattern(n):
    for i in range(0,n,1):
        for j in range(0,i,1):
            print(' ',end='')
        for k in range(i,n,1):
            print('* ',end='')
        print('')
    for i in range(1,n+1,1):
        for j in range(i,n,1):
            print(' ',end='')
        for k in range(0,i,1):
            print('* ',end='')
        print('')
a=int(input("Enter a number"))
pattern(a)
