from person.connect import Database


class Select():

    def __init__(self,phone):
        self.phone=phone

    def select_info(self):
        try:
            conn,cursor=Database().my_db()
            query="select * from user where phone=%s"%self.phone
            cursor.execute(query)
            r=cursor.fetchall()
            print(r)



        except:
            print("select ok")



s=Select("11")
s.select_info()