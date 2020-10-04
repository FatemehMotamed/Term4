from pymysql import connect

class Database():
    def my_db(self):

        try:
            conn = connect(
                'localhost',
                'poulstar',
                'poulstar',
                'Shop',
            )
            cursor = conn.cursor()
            print("connected :)")

        except:
            print("Error!")

        return conn, cursor
