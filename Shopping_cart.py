cart = ["Apple"]#,"banana","orange","Milk","Coffee","carrot"]
cart_count=len(cart)
if cart_count < 3:
    print ("Buy More!")
elif cart_count == 3:
    print ("Thanks for your purchase")
elif cart_count > 5:
    print ("You have 10% discount")