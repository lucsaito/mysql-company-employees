from database import database

class Employee(object):
    pass


if __name__ == "__main__":
    config = {
        'host': 'localhost',
        'user': 'root',
        'pass': 'rootpass123',
        'db': 'accounts'  # <-- Connects to database accounts
        }
    db = database(config['host'], config['user'],
                  config['pass'], config['db'])
