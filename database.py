import mysql.connector as mysql
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
            print("Sucessfully connected to database: {}".format(database_name))
            self.cursor = self.connect.cursor()
        except mysql.Error as err:
            print(err)




if __name__ == "__main__":
    print("File to configure the database.")