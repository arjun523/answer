
name = input("Enter our name: ")
budget = float(input("Enter our budget: "))
dictionary = {'Product':[],'Quantity':[],'Price':[]}
bgt = budget
list1 = list(dictionary.values())
prod = list1[0]
quant = list1[1]
pri = list1[2]
while (bgt>0):

    choice = int(input('''
    1. Add an item
    2. Exit
    Enter your choice: '''))

    if (choice == 1 and bgt>0):
        product = input("Enter Product:")
        quantity = input("Enter quantity:")
        price = float(input("Enter Price:"))

        if(bgt>=price):
            if (product in prod):
                index = prod.index(product)
                quant[index] = str(int(quant[index][:-2]) + int(quantity[:-2])) + 'kg'
                pri[index]= pri[index] + price

                bgt -= price
                print("Amount left: ",bgt,end="\n")
            

            else:
                prod.append(product)
                quant.append(quantity)
                pri.append(price)
                bgt -= price
                print("Amount left: ",bgt,end='\n')
            
    elif(bgt<0):
        print("No Budget")

    elif(choice==2):
        break

    else:
        print("Invalid Input")
        continue

print("Amount left: ",bgt)

print("\n\nGROCERY LIST ")
print("Product \tQuantity \tPrice")
for i in range(len(prod)):
    print(prod[i].upper(),' \t\t ',quant[i],' \t\t ',pri[i])
