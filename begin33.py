# Begin33. Известно, что X кг конфет стоит A рублей. 
# Определить, сколько стоит 1 кг и Y кг этих же конфет.
X = float(input())
A = float(input())
Y = float(input())
price = A / X
priceY = price * Y
print(price)
print(priceY)