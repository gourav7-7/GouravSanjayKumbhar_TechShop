from DAO.IProductService import IProductService
from Entity.Products import Products
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

class ProductService(IProductService):
    def get_products(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT * FROM Products")
            rows = stmt.fetchall()

            stmt.close()
            conn.close()
            return rows
            
        except Exception as e:
            raise InvalidDataException("Error fetching products.") from e

    def get_product_by_id(self, product_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Products WHERE ProductID = {product_id}")
            row = stmt.fetchone()
            stmt.close()
            conn.close()

            if row:
                return Products(row[0], row[1], row[2], row[3], row[4])
            else:
                return None
        except Exception as e:
            raise InvalidDataException("Error fetching product by ID.") from e

    def add_product(self, product):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"INSERT INTO Products VALUES ({product.getProductID()}, '{product.getProductName()}', '{product.getProductDescription()}', {product.getProductPrice()}, {product.getAvailableQuantity()})")
            conn.commit()
            print("Products added successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise ConcurrencyException("Concurrency issue detected.") from e

    def update_product(self, product):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Products WHERE ProductID = {product.getProductID()}")
            exists = stmt.fetchone()
            if exists:
                stmt.execute(f"UPDATE Products SET ProductName='{product.getProductName()}', ProductDescription='{product.getProductDescription()}', ProductPrice={product.getProductPrice()}, AvailableQuantity={product.getAvailableQuantity()} WHERE ProductID={product.getProductID()}")
                conn.commit()
                print("Products information updated successfully!")
            else:
                raise InvalidDataException("Products Not Found !!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise DatabaseOfflineException("Database is offline.") from e

    def delete_product(self, product_id):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Products WHERE ProductID = {product_id}")
            existing = stmt.fetchone()
            if existing is None:
                stmt.close()
                conn.close()
                raise InvalidDataException("Products Not Found")
            stmt.execute(f"DELETE FROM Products WHERE ProductID={product_id}")
            conn.commit()
            print("Products deleted successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise FileIOException("Error occurred during file I/O.") from e
