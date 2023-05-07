list=[1,2,3,4,5,6]
evenList=[]
oddList=[]
sum=0
s=0
for x in list:
    if(x%2==0):
        evenList.append(x)
    else:
        oddList.append(x)
    s+=x
print('Total Average :' ,s/(len(list)))
for x in evenList:
    sum+=x
print('Even Average :' ,(sum)/(len(evenList)))
sum=0
for x in oddList:
    sum+=x
print('Odd Average :' ,(sum)/(len(evenList)))

