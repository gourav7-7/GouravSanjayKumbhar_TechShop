from DAO.IOrderService import IOrderService
from Util.DBPropertyUtil import DBProprtyUtil
from Util.DBConnutil import DBConnutil
from Exceptions.AuthenticationException import AuthenticationException
from Exceptions.ConcurrencyException import ConcurrencyException
from Exceptions.DatabaseOfflineException import DatabaseOfflineException
from Exceptions.FileIOException import FileIOException
from Exceptions.IncompleteOrderException import IncompleteOrderException
from Exceptions.InsufficientStockException import InsufficientStockException
from Exceptions.InvalidDataException import InvalidDataException
from Exceptions.PaymentFailedException import PaymentFailedException

class OrderService(IOrderService):
    def calculate_total_amount(self, order_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT SUM(Quantity * Price) FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderID = {order_id}")
            total_amount = stmt.fetchone()[0]
            stmt.close()
            conn.close()
            return total_amount
        except Exception as e:
            raise InvalidDataException("Error calculating total amount.") from e

    def get_order_details(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT Customers.FirstName, Products.ProductName, Orders.TotalAmonut, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID")
            order_details = stmt.fetchall()
            stmt.close()
            conn.close()
            return order_details
        except Exception as e:
            raise InvalidDataException("Error fetching order details.") from e


    def get_order_details_by_OrderID(self, order_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT Customers.FirstName, Products.ProductName, Orders.TotalAmonut, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE Orders.OrderID = {order_id}")
            order_details = stmt.fetchall()
            stmt.close()
            conn.close()
            return order_details
        except Exception as e:
            raise InvalidDataException("Error fetching order details.") from e


    def cancel_order(self, order_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"DELETE FROM Orders WHERE OrderID = {order_id}")
            conn.commit()
            stmt.close()
            conn.close()
            print("Order canceled successfully!")
        except Exception as e:
            raise DatabaseOfflineException("Database is offline.") from e

    def create_order(self, order_details):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            # Insert into Orders table
            stmt.execute(f"INSERT INTO Orders (CustomerID, OrderDate, TotalAmonut) VALUES (?, ?, ?)",
                         (order_details['CustomerID'], order_details['OrderDate'], order_details['TotalAmount']))
            conn.commit()
            order_id = stmt.lastrowid

            # Insert into OrderDetails table
            for item in order_details['Items']:
                stmt.execute(f"INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (?, ?, ?)",
                             (order_id, item['ProductID'], item['Quantity']))
            conn.commit()
            print("Order created successfully!")
        except Exception as e:
            conn.rollback()
            raise FileIOException("Error occurred during file I/O.") from e
        finally:
            stmt.close()
            conn.close()

    def update_order(self, order_id, new_order_details):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            # Update Orders table
            stmt.execute(f"UPDATE Orders SET CustomerID=?, OrderDate=?, TotalAmonut=? WHERE OrderID=?",
                         (new_order_details['CustomerID'], new_order_details['OrderDate'], new_order_details['TotalAmount'], order_id))
            conn.commit()

            
            print("Order updated successfully!")
        except Exception as e:
            conn.rollback()
            raise ConcurrencyException("Concurrency issue detected.") from e
        finally:
            stmt.close()
            conn.close()

    def calculate_subtotal(self, order_detail_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT Quantity * Price FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderDetailID = {order_detail_id}")
            subtotal = stmt.fetchone()[0]
            stmt.close()
            conn.close()
            return subtotal
        except Exception as e:
            raise InvalidDataException("Error calculating subtotal.") from e

    def get_order_detail_info(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("""
                SELECT Orders.OrderID, Customers.FirstName AS CustomerName, Products.ProductName, OrderDetails.Quantity, Orders.TotalAmonut, Orders.OrderDate
                FROM Orders
                INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
                INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
                INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
            """)
            rows = stmt.fetchall()

            order_details = []
            for row in rows:
                order_detail = {
                    "OrderID": row[0],
                    "CustomerName": row[1],
                    "ProductName": row[2],
                    "Quantity": row[3],
                    "TotalAmount": row[4],
                    "OrderDate": row[5]
                }
                order_details.append(order_detail)

            return order_details
        except Exception as e:
            raise IncompleteOrderException("Order detail lacks a product reference.") from e
        finally:
            stmt.close()
            conn.close()

    def update_quantity_by_order_id(self, order_detail_id, new_quantity):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"UPDATE OrderDetails SET Quantity = {new_quantity} WHERE OrderDetailID = {order_detail_id}")
            conn.commit()
            stmt.close()
            conn.close()
            print("Quantity updated successfully!")
        except Exception as e:
            raise InsufficientStockException("Insufficient stock to fulfill the order.") from e

    def add_discount(self, order_detail_id, discount_amount):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"UPDATE OrderDetails SET Price = Price - {discount_amount} WHERE OrderDetailID = {order_detail_id}")
            conn.commit()
            stmt.close()
            conn.close()
            print("Discount applied successfully!")
        except Exception as e:
            raise PaymentFailedException("Payment for the order failed.") from e
