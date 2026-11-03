for i in range(1,31):
    print(i)
    if i % 3 == 0:
        print("fizz")
    elif i % 4 == 0:
            print("buzz")
    elif i % 3 == 0,i % 4 == 0:
        print ("fizzbuzz")