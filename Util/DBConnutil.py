import mysql.connector as sql

class DBConnutil:
    @staticmethod
    def getConnection(connection_string):
        try:
            conn = sql.connect(**connection_string)
            if conn.is_connected():
                print("Database is Connected")
            else:
                print("Database is NOT Connected !!!")
            return conn
        except sql.Error as e:
            print("Error connecting to MySQL:", e)
            return None

    @staticmethod
    def closeDB(conn):
        conn.close()
        print("Database disconnected")