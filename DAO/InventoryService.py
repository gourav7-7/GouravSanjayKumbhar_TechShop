from DAO.IInventoryService import IInventoryService
from Util.DBPropertyUtil import DBProprtyUtil
from Util.DBConnutil import DBConnutil
from Exceptions.AuthenticationException import AuthenticationException
from Exceptions.ConcurrencyException import ConcurrencyException
from Exceptions.FileIOException import FileIOException
from Exceptions.IncompleteOrderException import IncompleteOrderException
from Exceptions.InsufficientStockException import InsufficientStockException
from Exceptions.InvalidDataException import InvalidDataException
from Exceptions.PaymentFailedException import PaymentFailedException

class InventoryService(IInventoryService):
    def get_product(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("""
                SELECT Products.ProductName
                FROM Inventory
                INNER JOIN Products ON Inventory.ProductID = Products.ProductID
            """)
            product_name = stmt.fetchall()
            stmt.close()
            conn.close()
            return product_name
        except Exception as e:
            raise InvalidDataException("Error fetching product.") from e

    def get_quantity_in_stock(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT p.ProductName, i.QuantityInStock FROM Inventory i JOIN Products p ON i.ProductID = p.ProductID")
            quantity_in_stock = stmt.fetchall()
            stmt.close()
            conn.close()
            return quantity_in_stock
        except Exception as e:
            raise InvalidDataException("Error fetching quantity in stock.") from e

    def add_to_inventory(self, quantity):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"UPDATE Inventory SET QuantityInStock = QuantityInStock + {quantity}")
            conn.commit()
            print(f"{quantity} units added to inventory successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise ConcurrencyException("Concurrency issue detected.") from e

    def remove_from_inventory(self, quantity):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"UPDATE Inventory SET QuantityInStock = QuantityInStock - {quantity} WHERE QuantityInStock >= {quantity}")
            conn.commit()
            print(f"{quantity} units removed from inventory successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise InsufficientStockException("Insufficient stock to fulfill the order.") from e

    def update_stock_quantity(self, new_quantity):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"UPDATE Inventory SET QuantityInStock = {new_quantity}")
            conn.commit()
            print("Stock quantity updated successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise FileIOException("Error occurred during file I/O.") from e

    def is_product_available(self, quantity_to_check):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT CASE WHEN SUM(QuantityInStock) >= {quantity_to_check} THEN 'True' ELSE 'False' END FROM Inventory")
            result = stmt.fetchone()[0]
            return result == 'True'
        except Exception as e:
            raise InvalidDataException("Error checking product availability.") from e

    def get_inventory_value(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT SUM(QuantityInStock * Price) FROM Inventory INNER JOIN Products ON Inventory.ProductID = Products.ProductID")
            inventory_value = stmt.fetchone()[0]
            return inventory_value
        except Exception as e:
            raise PaymentFailedException("Payment for the order failed.") from e

    def list_low_stock_products(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT Products.ProductName, Inventory.QuantityInStock FROM Inventory INNER JOIN Products ON Inventory.ProductID = Products.ProductID WHERE QuantityInStock <= 5")
            low_stock_products = stmt.fetchall()
            return low_stock_products
        except Exception as e:
            raise IncompleteOrderException("Order detail lacks a product reference.") from e

    def list_out_of_stock_products(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT Products.ProductName FROM Inventory INNER JOIN Products ON Inventory.ProductID = Products.ProductID WHERE QuantityInStock <= 0")
            out_of_stock_products = stmt.fetchall()
            return out_of_stock_products
        except Exception as e:
            raise InvalidDataException("Error listing out-of-stock products.") from e
        
    def list_all_products(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT Products.ProductName FROM Inventory INNER JOIN Products ON Inventory.ProductID = Products.ProductID")
            listProd = stmt.fetchall()
            return listProd
        except Exception as e:
            raise InvalidDataException("Error listing out-of-stock products.") from e
        
            
