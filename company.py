from database import database
import datetime

"""
| NAME | SURNAME | EMAIL | CELLNUMB | CREATED |

db.showtables()
db.create_table(name, [(col, type)])

"""

class Company(object):
    def __init__(self):
        pass
    def add_employee(self):
        pass
    def last_employees_created(self):
        pass
class Employee(object):
    def __init__(self):
        pass
        #self.name, self.surname = name, surname
        #cself.email, self.cellnumb = email, cellnumb





if __name__ == "__main__":
    DATABASE_NAME = 'company_employees'

    config = {
        'host': 'localhost',
        'user': 'root',
        'pass': 'rootpass123',
        'db': DATABASE_NAME  # <-- Connects to database accounts
        }
    db = database(config['host'], config['user'],
                  config['pass'], config['db'])

    a = datetime.datetime.now()
    x = a - datetime.timedelta(microseconds=a.microsecond)
    db.show_head()
    """"
    db.add_to_table('USERS', ['NAME', 'SURNAME', 'EMAIL', 'CELLNUMB', 'CREATED'],
                    ['rtnrt', 'cnfgnrt', 'erthb', 'etgwr', str(x)])"""





    """
    Creating table "USERS":
    table_name = "USERS"
    columns = [('NAME', 'TEXT'), ('SURNAME', 'TEXT'),
               ('EMAIL', 'TEXT'), ('CELLNUMB', 'TEXT'),
               ('CREATED', 'DATETIME')]
    db.create_table(table_name, columns)
    ####### create a new table ########
    db.create_table("teste", columns)     <-- (String, [Tuples])
    
    
    
    # DATETIME = '0000-00-00 00:00:00'  , YYYY-MM-DD
    # DATETIME FORMAT
    a = datetime.datetime.now()
    x = a - datetime.timedelta(microseconds=a.microsecond)
    print(x)"""




