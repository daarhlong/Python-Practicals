#get input
fahrenheit = float(input("Input fahrenheit: "))

#convert fahrenheit to celsius
celsius = (5/9) * (fahrenheit - 32)

#display result
print("{0:.2f} degree fahrenheit is {1:.1f} degree celsius".format(fahrenheit, celsius)) 
