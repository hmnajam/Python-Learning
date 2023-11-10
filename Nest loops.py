import time

startTime = time.time()

# Outer Loop
for i in range (100):
    #print(str(i), end= " ")
    
    # Inner loop
    for j in range(1000):
        print (str(i) + str(j), end = " ")

    print()

print (round((time.time() - startTime), 2))  