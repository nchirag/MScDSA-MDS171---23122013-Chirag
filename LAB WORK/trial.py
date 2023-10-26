class sport_mart :
    def __init__(self):
            self.details = {"product_details": [], "order_details": []}

    def product_details(self):
            for i in open("D:/GIT/MScDSA-MDS171---23122013-Chirag/LAB WORK/product_details.csv", "r").readlines():  
                data0 = i.strip().split(',')
                
                if data0[2] != "Quantity":
                    product_details = {
                        "Product ID": int(data0[0]),
                        "Product Name": data0[1],
                        "Quantity": int(data0[2]),
                        "Price": eval(data0[3])
                    }
                    self.details["product_details"].append(product_details)

    def order_details(self):
            for j in open("D:/GIT/MScDSA-MDS171---23122013-Chirag/LAB WORK/order_details.csv", "r").readlines():
                data1 = j.strip().split(',')
                if data1[2] != "Quantity":#remove the headers
                    order_details = {     
                        "Order ID": int(data1[0]),
                        "Product ID": int(data1[1]),
                        "Quantity": int(data1[2]),
                        "Order Date": data1[3]
                    }
                    self.details["order_details"].append(order_details)