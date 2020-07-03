import mysql.connector as mysql
from mysql.connector import errorcode

#rootpass123


class database(object):
    def __init__(self, host, user, user_pass, database_name):
        self.host, self.database_name = host, database_name
        self.user, self.user_pass = user, user_pass
        try:
            self.connect = mysql.connect(
                host= host, user= user,
                passwd= user_pass, database= database_name
            )
            print("Successfully connected to database: {}.".format(database_name))
            self.cursor = self.connect.cursor()
            self.tables = {}
        except mysql.Error as err:
            print(err)

    def create_table(self, table_name, columns):  #<-- expects a string and a list of tuples
        command = ['{} {}'.format(col[0], col[1]) for col in columns]
        command = ', '.join(command)
        try:
            self.cursor.execute("CREATE TABLE {} ({});".format(table_name, command))
            print("Table \"{}\" successfully created.".format(table_name))
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table \"{}\" already exists.".format(table_name))
            else:
                print(err)

    def remove_table(self):
        pass
    def show_tables(self):
        pass




if __name__ == "__main__":
    print("File to configure the database.")