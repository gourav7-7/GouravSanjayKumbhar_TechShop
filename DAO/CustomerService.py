from DAO.ICustomerService import ICustomerService
from Entity.Customers import Customers
from Util.DBPropertyUtil import DBProprtyUtil
from Util.DBConnutil import DBConnutil
from Exceptions.InvalidDataException import InvalidDataException
from Exceptions.AuthenticationException import AuthenticationException

class CustomerService(ICustomerService):
    def GetCustomerById(self, customerId):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Customers WHERE CustomerID = {customerId}")
            row = stmt.fetchall()
            stmt.close()
            conn.close()
            return row
        except Exception as e:
            raise InvalidDataException("Customer Not Found.") from e

    def GetCustomers(self):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute("SELECT * FROM Customers")
            rows = stmt.fetchall()
            stmt.close()
            conn.close()

            customers = []
            for row in rows:
                customer = {
                    "CustomerID": row[0],
                    "FirstName": row[1],
                    "LastName": row[2],
                    "Email": row[3],
                    "Phone": row[4],
                    "Address": row[5]
                }
                customers.append(customer)

            return customers
        except Exception as e:
            raise InvalidDataException("Error fetching customers.") from e

    def RegisterCustomer(self, custData):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"INSERT INTO Customers VALUES ({custData.getCustomerID()}, '{custData.getFirstName()}', '{custData.getLastName()}', '{custData.getEmail()}', '{custData.getPhoneNumber()}', '{custData.getAddress()}')")
            conn.commit()
            print("Customer registered successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise InvalidDataException("Error registering customer.") from e

    def UpdateCustomer(self, customerData):

            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Customers WHERE CustomerID = {customerData.getCustomerID()}")
            exists = stmt.fetchone()
            if exists:
                stmt.execute(f"UPDATE Customers SET FirstName='{customerData.getFirstName()}', LastName='{customerData.getLastName()}', Email='{customerData.getEmail()}', Phone='{customerData.getPhoneNumber()}', Address='{customerData.getAddress()}' WHERE CustomerID={customerData.getCustomerID()}")
                conn.commit()
                print("Customer information updated successfully!")
            else:
                stmt.close()
                conn.close()
                raise InvalidDataException("Customer Not Found !!")
            stmt.close()
            conn.close()


    def DeleteCustomer(self, customerId):
        try:
            conn = DBConnutil.getConnection(DBProprtyUtil.getConnectionString('TechShop'))
            stmt = conn.cursor()
            stmt.execute(f"SELECT * FROM Customers WHERE CustomerID = {customerId}")
            existing = stmt.fetchone()
            if existing is None:
                stmt.close()
                conn.close()
                raise InvalidDataException("Customer Not Found")
            stmt.execute(f"DELETE FROM Customers WHERE CustomerID={customerId}")
            conn.commit()
            print("Customer deleted successfully!")
            stmt.close()
            conn.close()
        except Exception as e:
            raise InvalidDataException("Error deleting customer.") from e
