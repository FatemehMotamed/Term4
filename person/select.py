from person.connect import Database


class Select():

    def select_date(self):
        try:
            Database().my_db()
        except:
            print("select ok")