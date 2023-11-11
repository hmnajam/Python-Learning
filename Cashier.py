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
        'Rio' : 200,
        'Prince' : 200,
        'Chicken' : 500,
        'Egg' : 30,
        'Bread' : 120,
        'Biscuit': 3,
        'Fish': 600,
        'Coke': 200,
        'Apple': 30,
        'Onion': 130
        }
    subtotal = priceData[product] * quantity
    print(product + ' Rs: ' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal


# This function calculate discount based on membership status.
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 250:
        if membership == 'Gold' or membership == 'gold':
            billAmount = billAmount *0.80
            discount = 20
        elif membership == 'Silver' or membership == 'silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze' or membership == 'bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + "% off for " + membership + ' ' + 'membership on total amount: Rs' + str(billAmount))
    else:
        print('No discount on amount less than Rs: 250')
    return billAmount


# This function makes bill after taking buyingData and membership as input.
def makeBill (buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is Rs: ' + str(billAmount))

try:
    buyingData = enterProducts()
    membership = input('Enter membership: ')
    makeBill(buyingData, membership)

except Exception as e:
    print('Please enter correct input. Input data is case sensitive.')
    print(e)