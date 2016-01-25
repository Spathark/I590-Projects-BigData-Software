prompt = 'Enter a number: '
while True:
    data = input(prompt)

    if data:
        try:
            number = float(data)
        except ValueError:
            print ('Invalid input...')
            
        else:
            for n in range(1,int(data)):
                if number % 2 == 0 and number % 3 == 0:
                    print ('fizzbuzz')
                    break
                if number % 2 == 0:
                    print ('fizz')
                    break
                if number % 3 == 0:
                    print ('buzz')
                    break
        #prompt = 'Please try again: '
                print ('not a multiple of 2 or 3')
                break   
    else:
        # allow the user to exit by entering nothing
        print ('Goodbye!')
        break
