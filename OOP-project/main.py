from food_item import FoodItem
from menu import Menu
from user import Customer,Admin,Employee 
from restaurant import  Restaurant 
from orders import Order 


mamar_restaurant = Restaurant("mamar restaurant")

def customer_menu():
    name = input("Enter a Name: ")
    email = input("Enter a email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    customer = Customer(name =name , email = email, phone = phone, address = address)

    while True:
        print(f"welcome {customer.name}!!")
        print("1.view Menu: ")
        print("2.Add_to_cart: ")
        print("3.view cart; ")
        print("4.PayBill: ")
        print("5.Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item Name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break 
        else:
            print("Invaild Input")



def admin_menu():
    name = input("Enter a Name: ")
    email = input("Enter a email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    admin = Admin(name=name , email= email, phone= phone, address= address)

    while True:
        print(f"welcome {admin.name}!!")
        print("1.Add new Item ")
        print("2. Add new Employee ")
        print("3. view Employee ")
        print("4. view Items ")
        print("5.Delete Items")
        print("6.exitt")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurant,item)
        elif choice == 2:
           name = input("Enter Employee Name: ")
           phone = input("Enter Employee Phone: ")
           email = input("Enter Employee email: ")
           designation = input("Enter Employee desigantion: ")
           age = input("Enter Employee age: ")
           salary = input("Enter Employee salary: ")
           address = input("Enter Employee address: ")
           employee = Employee(name, email, phone, address, age, designation, salary)
           admin.add_employee(mamar_restaurant,employee)

        elif choice == 3:
            admin.view_employee(mamar_restaurant)

        elif choice == 4:
            admin.view_menu(mamar_restaurant)

        elif choice == 5:
            item_name = input("Enter item name :")
            admin.remove_item(mamar_restaurant,item)

        elif choice == 6:
            break
        else:
            print("Invaild Input")

while True:
    print("welcome")
    print("1.customer")
    print("2.Admin")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("invaild Input")