purchase_amount=int(input("enter purchase_amount:$"))
if purchase_amount>=5000:
  print("discount:",20)
  print(purchase_amount-20)
elif purchase_amount>=3000:
  print("discount:",10)
  print(purchase_amount-10)
elif purchase_amount>=1000:
  print("discount:",5)
  print(purchase_amount-5)
else:
  print(purchase_amount-0)



order_amount=int(input("enter order_amount:$"))
if order_amount>=2000:
  print("free delivery")
#   print("order_amount:150)
elif order_amount>=1000:
  print("delivery charge:50")
  print(order_amount+50)
else:
  print(order_amount+100)




units = int(input("Enter the number of units consumed: "))
if units <= 100:
    print(units * 2)
elif units <= 200:
    print( units * 3)
elif units <= 300:
    print( units * 5)
else:
    print( units * 7)

