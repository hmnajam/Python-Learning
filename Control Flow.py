num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]


for num in num_list:
    if num > 45: 
        print(num, 'is over 45')

    else :
        print(num, 'in under 45')



    


for index, value in enumerate(num_list):
    if value == 36:
        print(f'Number found at {index}')
    # print(f'Index: {index}, Value: {value}')


count = 0
for number in range(10):
    count +=1
    if number == 8:
        
        print(f'Count is {number}')
        break



for x, num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at', x)

print ('Count is', count)