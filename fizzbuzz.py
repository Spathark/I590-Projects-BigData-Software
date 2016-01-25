def fizzbuzz(x):
 	for i in range (1,x):
  		if i%3==0 and x%2==0:
   		print("fizzbuzz")
  	elif i%2==0:
   		print('fizz')
 	elif i%3==0:
   		print('buzz')
  	else:
   		print (i) 
x = input("Enter a number: ")
fizzbuzz(x)
