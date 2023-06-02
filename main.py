def game(x):
    r1=x%10
    r2=int(x/10)
    if r2 >= r1:
        return (r2 - r1)
    else:
        return (r1 - r2)
    
x =int(input('Enter number : [10 , 99]'))
if x>=10 and x<=99:
    print(game(x))
else :
    print('Enter number between 10-99 ')

