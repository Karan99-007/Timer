menu ={"piza": 100.0,
       "chowmin": 60.3,
       "momoj": 60.0,
        "samosa": 15.0,
        "chips": 10.5,
        "fries": 40.0}

cart =[]
total =0
print(".........Menu.........")
for key,value in menu.items():
    print(f"{key:10} : {value: .2f}")

print(".......................")
print(" what you wanna buy ? enter no to exit")
while 1:
    ct= input("")
    cart.append(ct)
    if ct == "no":
        break

print("......Your Order...........")    
for cat in cart:
     print(cat)

for food in cart:
    if food!="no":
        total += menu.get(food)
print(total)    