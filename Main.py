from DAO.CustomerService import CustomerService
from DAO.InventoryService import InventoryService
from DAO.OrderService import OrderService
from DAO.ProductService import ProductService
from Entity.Customers import Customers
from Entity.Inventory import Inventory
from Entity.OrderDetails import OrderDetails
from Entity.Orders import Orders
from Entity.Products import Products
from Exceptions.AuthenticationException import AuthenticationException
from Exceptions.ConcurrencyException import ConcurrencyException
from Exceptions.DatabaseOfflineException import DatabaseOfflineException
from Exceptions.FileIOException import FileIOException
from Exceptions.IncompleteOrderException import IncompleteOrderException
from Exceptions.InsufficientStockException import InsufficientStockException
from Exceptions.InvalidDataException import InvalidDataException
from Exceptions.PaymentFailedException import PaymentFailedException
from Util.DBConnutil import DBConnutil
from Util.DBPropertyUtil import DBProprtyUtil


class MainMenu:
    def __init__(self):
        
        self.custServ = CustomerService()
        self.InvServ = InventoryService()
        self.OrdServ = OrderService()
        self.ProdServ = ProductService()


    def CustomerMenu(self):
        print("\nCustomer Menu: ")
        print("1. Get Customer by ID")
        print("2. Get All Customers")
        print("3. Register New Customer")
        print("4. Update Existing Customer")
        print("5. Delete Customer")
        print("6. Exit")

    def OrderMenu(self):
        print("\nOrders Menu: ")
        print("1. Get All Order Details")
        print("2.  Get All Order Details by OrderID")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Update Order")
        print("6. Calculate SubTotal")
        print("7. Update Quantity")
        print("8. Add Discount")
        print("9. Exit")

    def ProductMenu(self):
        print("\nProduct Menu: ")
        print("1. Get All Products")
        print("2. Get Products by Product ID")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

    def InventoryMenu(self):
        print("\nAdmin Menu: ")
        print("1. Get All Products")
        print("2. Get Quantity in Stock")
        print("3. Add to Inventory")
        print("4. Remove from Inventory")
        print("5. Update Stock Quantity")
        print("6. Check Product Availability")
        print("7. Get Inventory value")
        print("8. List Products Which are Low on Stock")
        print("9. List Out of Stock Products")

    def Menu(self):
        print("\nMain Menu:")
        print("1. Customer")
        print("2. Order")
        print("3. Product")
        print("4. Inventory")
        print("5. Exit")



    def getCustomerByID(self):
        custID = int(input("Enter Customer ID : "))
        try:
           res = self.custServ.GetCustomerById(custID)
           if res == []:
               raise InvalidDataException
           else:
               print(res)
        except InvalidDataException as e:
            print(e)



    def getAllCustomers(self):
        try:
            res = self.custServ.GetCustomers()
            if res == []:
               raise InvalidDataException
            else:
               print(res)
        except InvalidDataException as e:
            print(e)



    def regCustomer(self):
        try:
            cust = Customers()
            cust.setCustomerID(int(input("Enter Customer ID : ")))
            cust.setFirstName(input("Enter First Nmae : "))
            cust.setLastName(input("Enter Last Name : "))
            cust.setEmail(input("Enter Customer Email : "))
            cust.setPhoneNumber(input("Enter Phone number : "))
            cust.setAddress(input("Enter Address : "))
        except ValueError:
            print("Invalid Input Data. Try Again.")
        try:
            self.custServ.RegisterCustomer(cust)
            print("Customer Registered Successfully")
        except InvalidDataException as e:
            print(e)  



    def updateCustomer(self):
        cust = Customers()
        cust.setCustomerID(int(input("Enter Customer ID to Update : ")))
        cust.setFirstName(input("Enter First Name : "))
        cust.setLastName(input("Enter Last Name : "))
        cust.setEmail(input("Enter Customer Email : "))
        cust.setPhoneNumber(input("Enter Phone number : "))
        cust.setAddress(input("Enter Address : ")) 
        try:
            self.custServ.UpdateCustomer(cust)
            print("Customer updated successfully!")
        except InvalidDataException as e:
            print(e)

    def deleteCust(self):
        custID = int(input("Enter Customer ID to Delete : "))
        try:
            self.custServ.DeleteCustomer(custID)
        except InvalidDataException as e:
            print(e)



    def getAllOrders(self):
        try:
            res = self.OrdServ.get_order_details()
            if res == []:
               raise InvalidDataException
            else:
               print(res)
        except InvalidDataException as e:
            print(e)

    def getOrderDetailsByOrderID(self):
        ordID = int(input("Enter OrderID : "))
        try:
            res = self.OrdServ.get_order_details_by_OrderID(ordID)
            if res == []:
               raise InvalidDataException
            else:
               print(res)
        except InvalidDataException as e:
            print(e)


    def createOrder(self):
        ord = Orders()
        ord.set_order_id(int(input("Enter OrderID : ")))
        ord.setCustomerID(int(input("Enter CustomerID : ")))
        ord.setOrderDate(input("Enter Order Date (YYYY-MM-DD) : "))
        ord.setTotalAmount(int(input("Enter total amount : ")))
        try:
            self.OrdServ.create_order(ord)
            print("Order Created Successfully")
        except InvalidDataException as e:
            print(e)


    def cancelOrder(self):
        ordID = int(input("Enter OrderID to Delete : "))
        try:
            self.OrdServ.cancel_order(ordID)
            print("Order Canceled")
        except IncompleteOrderException as e:
            print(e)

    def updateOrder(self):
        ord = Orders()
        ord.set_order_id(int(input("Enter OrderID : ")))
        ord.setCustomerID(int(input("Enter CustomerID : ")))
        ord.setOrderDate(input("Enter Order Date (YYYY-MM-DD) : "))
        ord.setTotalAmount(int(input("Enter total amount : ")))
        try:
            self.OrdServ.update_order(ord)
            print("Order Updated Successfully")
        except IncompleteOrderException as e:
            print(e)


    def calculateSubtotal(self):
        ordDetailID = int(input("Enter Order Detail ID : "))
        try:
            res = self.OrdServ.calculate_subtotal(ordDetailID)
            if res == []:
               raise InvalidDataException
            else:
               print(res)
        except InvalidDataException as e:
            print(e)

    def updateQuantity(self):
        ordDetailID = int(input("Enter Order Detail ID to update : "))
        quant = int(input("Enter Updated Quantity : "))
        try:
            self.OrdServ.update_quantity_by_order_id(ordDetailID,quant)
            print("Order Detail Updated")
        except InvalidDataException as e:
            print(e)

    def addDiscount(self):
        ordDetailID = int(input("Enter Order Detail ID to add Discount : "))
        discAmt = int(input("Add Discount Amount : "))
        try:
            self.OrdServ.add_discount(ordDetailID,discAmt)
        except InvalidDataException as e:
            print(e)

    def getAllProducts(self):
        try:
            res = self.ProdServ.get_products()
            if res == []:
                raise InvalidDataException
            else:
                print(res)
        except InvalidDataException as e:
            print(e)

    def getProductByID(self):
        prodID = int(input("Enter Product ID : "))
        try:
            res = self.ProdServ.get_product_by_id(prodID)
            if res == []:
                raise InvalidDataException
            else:
                print(res)
        except InvalidDataException as e:
            print(e)

    def addProduct(self):
        prod = Products()
        prod.set_product_id(int(input("Enter Product ID : ")))
        prod.set_product_name(input("Enter Product Name : "))
        prod.set_price(float(input("Enter Price : ")))
        prod.set_description(input("Enter Description : "))
        prod.set_quantity(int(input("Enter Quantity : ")))
        try:
            self.ProdServ.add_product(prod)
            print("Product Added Successfully")
        except InvalidDataException as e:
            print(e)

    def updateProduct(self):
        prod = Products()
        prod.set_product_id(int(input("Enter Product ID to Update : ")))
        prod.set_product_name(input("Enter Product Name : "))
        prod.set_price(float(input("Enter Price : ")))
        prod.set_description(input("Enter Description : "))
        prod.set_quantity(int(input("Enter Quantity : ")))
        try:
            self.ProdServ.update_product(prod)
            print("Product Updated Successfully")
        except InvalidDataException as e:
            print(e)

    def deleteProduct(self):
        prodID = int(input("Enter Product ID to Delete : "))
        try:
            self.ProdServ.delete_product(prodID)
            print("Product Deleted Successfully")
        except InvalidDataException as e:
            print(e)


    def getAllInventory(self):
        try:
            res = self.InvServ.get_product()
            if res == []:
                raise InvalidDataException
            else:
                print(res)
        except InvalidDataException as e:
            print(e)

    def getQuantityInStock(self):
        try:
            res = self.InvServ.get_quantity_in_stock()
            if res == []:
                raise InvalidDataException
            else:
                print("Quantity in Stock:", res)
        except InvalidDataException as e:
            print(e)

    def addToInventory(self):
        prodID = int(input("Enter Product ID to Add to Inventory : "))
        quantity = int(input("Enter Quantity to Add : "))
        try:
            self.InvServ.add_to_inventory(prodID, quantity)
            print("Added to Inventory Successfully")
        except InvalidDataException as e:
            print(e)

    def removeFromInventory(self):
        prodID = int(input("Enter Product ID to Remove from Inventory : "))
        quantity = int(input("Enter Quantity to Remove : "))
        try:
            self.InvServ.remove_from_inventory(prodID, quantity)
            print("Removed from Inventory Successfully")
        except InvalidDataException as e:
            print(e)

    def updateStockQuantity(self):
        prodID = int(input("Enter Product ID to Update Stock Quantity : "))
        quantity = int(input("Enter Updated Quantity : "))
        try:
            self.InvServ.update_stock_quantity(prodID, quantity)
            print("Stock Quantity Updated Successfully")
        except InvalidDataException as e:
            print(e)

    def checkProductAvailability(self):
        prodID = int(input("Enter Product ID to Check Availability : "))
        try:
            res = self.InvServ.is_product_available(prodID)
            if res:
                print("Product is available.")
            else:
                print("Product is not available.")
        except InvalidDataException as e:
            print(e)

    def getInventoryValue(self):
        try:
            res = self.InvServ.get_inventory_value()
            print("Inventory Value:", res)
        except InvalidDataException as e:
            print(e)

    def listProductsLowOnStock(self):
        try:
            res = self.InvServ.list_low_stock_products()
            print("Products Low on Stock:")
            for product in res:
                print(product)
        except InvalidDataException as e:
            print(e)

    def listOutOfStockProducts(self):
        try:
            res = self.InvServ.list_out_of_stock_products()
            if res == []:
                print("Out of Stock Producs : 0")
            else:
                print("Out of Stock Products:")
                for product in res:
                    print(product)
        except InvalidDataException as e:
            print(e)

    def Exit(self):
        print("Exiting ...")
        print("Exited")


    def run(self):
            while True:
                self.Menu()
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.CustomerMenu()
                    customer_choice = input("Enter your choice: ")
                    if customer_choice == "1":
                        self.getCustomerByID()
                    elif customer_choice == "2":
                        self.getAllCustomers()
                    elif customer_choice == "3":
                        self.regCustomer()
                    elif customer_choice == "4":
                        self.updateCustomer()
                    elif customer_choice == "5":
                        self.deleteCust()
                    elif customer_choice == "6":
                        continue
                    else:
                        print("Invalid choice. Please enter a number from 1 to 6.")
                elif choice == "2":
                    self.OrderMenu()
                    order_choice = input("Enter your choice: ")
                    if order_choice == "1":
                        self.getAllOrders()
                    elif order_choice == "2":
                        self.getOrderDetailsByOrderID()
                    elif order_choice == "3":
                        self.createOrder()
                    elif order_choice == "4":
                        self.cancelOrder()
                    elif order_choice == "5":
                        self.updateOrder()
                    elif order_choice == "6":
                        self.calculateSubtotal()
                    elif order_choice == "7":
                        self.updateQuantity()
                    elif order_choice == "8":
                        self.addDiscount()
                    elif order_choice == "9":
                        continue
                    else:
                        print("Invalid choice. Please enter a number from 1 to 9.")
                elif choice == "3":
                    self.ProductMenu()
                    product_choice = input("Enter your choice: ")
                    if product_choice == "1":
                        self.getAllProducts()
                    elif product_choice == "2":
                        self.getProductByID()
                    elif product_choice == "3":
                        self.addProduct()
                    elif product_choice == "4":
                        self.updateProduct()
                    elif product_choice == "5":
                        self.deleteProduct()
                    elif product_choice == "6":
                        continue
                    else:
                        print("Invalid choice. Please enter a number from 1 to 6.")
                elif choice == "4":
                    self.InventoryMenu()
                    inventory_choice = input("Enter your choice: ")
                    if inventory_choice == "1":
                        self.getAllInventory()
                    elif inventory_choice == "2":
                        self.getQuantityInStock()
                    elif inventory_choice == "3":
                        self.addToInventory()
                    elif inventory_choice == "4":
                        self.removeFromInventory()
                    elif inventory_choice == "5":
                        self.updateStockQuantity()
                    elif inventory_choice == "6":
                        self.checkProductAvailability()
                    elif inventory_choice == "7":
                        self.getInventoryValue()
                    elif inventory_choice == "8":
                        self.listProductsLowOnStock()
                    elif inventory_choice == "9":
                        self.listOutOfStockProducts()
                    else:
                        print("Invalid choice. Please enter a number from 1 to 9.")
                elif choice == "5":
                    self.Exit()
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            
                option = input("Do you want to continue (Y/N)? ")
                if option.upper() != 'Y':
                    self.Exit()
                    break


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()


