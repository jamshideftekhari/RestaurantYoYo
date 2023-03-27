import mysql.connector

class MySqlConnector():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def connect(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.connection.cursor()
        
    def close(self):
        self.connection.close()
        
    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        self.cursor.close()

    def queryDB(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
             
if __name__ == "__main__":
    localHost = "localhost"
    user = "root"
    pw = "jam2003eft" 
    db = "resturantyoyosimple"                   
    dbconnection=MySqlConnector(localHost, user, pw, db)
    dbconnection.connect()
    query = "SELECT * FROM resturantyoyosimple.resturant"
    print(dbconnection.queryDB(query))