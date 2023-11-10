httpRequest = 404

match httpRequest:
    case 200 | 201:
        print ('statement 1')

    case 400:
        print ('statement 2')

    case 404:
        print ('statement 4')

    case 500 | 501:
        print ('statement 3')



