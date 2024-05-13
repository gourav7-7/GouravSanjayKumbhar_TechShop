class DBProprtyUtil:
    @staticmethod
    def getConnectionString(db):
        host = 'localhost'
        database = db
        user = 'root'
        password = 'root'
        connection_string = {
            'host': host,
            'database': database,
            'user': user,
            'password': password
        }
        return connection_string

    