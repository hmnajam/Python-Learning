# This function takes products input in dictionary named buyingData.
def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to Add product or Q to Quit:')
        if details == 'A' or details == 'a':
            product = input('Enter product: ')
            quantity = int(input('Enter product quantity: '))
            buyingData.update({product:quantity})
        elif details == 'Q' or details == 'q':
            enterDetails = False
        else:
            print('Please select a correct option')
    return buyingData

# This function calculates the total price of the products added.
def getPrice(product, quantity): 
    priceData = {
        'Rio Biscuits' : 200,
        'Prince Buiscuits' : 200,
        'Chicken' : 500,
        'Eggs' : 340,
        'Bread' : 120,
        }
    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal

# This function calculate discount based on membership status.
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 250:
        if membership == 'Gold':
            billAmount = billAmount *0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + '% off for' + str(billAmount))
    else:
        print('No discount')
    return billAmount


# This function
def makeBill (buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount = billAmount + getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('Total Bill: ' + str(billAmount))


buyingData = enterProducts()
membership = input('Enter membership: ')
makeBill(buyingData, membership)