class Hotel:
    def __init__(self):
        self.details = {"inventory_details": [], "Order_details": []}

    def info(self):
        print("CHOPSTICKS IS A GOOD RESTAURANT")

    def inventory_details(self):
        for i in open("D:\GIT\MScDSA-MDS171---23122013-Chirag\LAB WORK\INVENTORY_DETAILS.csv", "w+").readlines():
            det0 = i.strip().split(",")
            if det0[2] != "Quantity":
                inventory_entry = {
                    "Product ID": int(input("Enter your product ID - ")),
                    "Product Name": input("Enter the name of the product - "),
                    "Quantity": int(input("Enter the number of quantity - ")),
                    "Price": float(input("Enter the price of the product - "))
                }
                self.details["inventory_details"].append(inventory_entry)

    def order_details(self):
        for j in open("D:\GIT\MScDSA-MDS171---23122013-Chirag\LAB WORK\DETAILS_OF_THE_ORDER.csv", "w+").readlines():
            det1 = j.strip().split(",")
            if det1[2] != "Quantity":
                order_entry = {
                    "Order ID": int(input("Enter the order ID - ")),
                    "Product ID": int(input("Enter your product ID - ")),
                    "Quantity": int(input("Enter the quantity - ")),
                    "Order Date": input("Enter the date of the order - ")
                }
                self.details["Order_details"].append(order_entry)

    def menu(self):
        print("\nCHOPSTICKS")
        print("1. About the Restaurant")
        print("2. View what's in the inventory")
        print("3. Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            self.info()
        elif choice == 2:
            self.inventory_details()
        elif choice == 3:
            print("Thank you!")

if __name__ == "__main__":
    restaurant = Hotel()
    restaurant.menu()
