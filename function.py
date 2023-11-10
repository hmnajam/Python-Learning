def sum (x, y):

    z= x+y
    print(z)
    return (z)
sum(5, 5)




order = [2.5, 5, 5, 7.5]
def calcuate_subtotal(order):

    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE

    subtotal = 0.0
    for item in order:
        subtotal += float(item)
        
    print (subtotal)
    return subtotal


calcuate_subtotal(order)
