import sqlite3
import bcrypt

'''
    Will initialize the different fields that are required & create the users.db file that will 
    be loaded into the rest of the code
'''

conn = sqlite3.connect('users.db')
print("Opened users database successfully")

conn.execute('''CREATE TABLE USERS
         (ID            INTEGER    PRIMARY KEY     NOT NULL,
         USERNAME      VARCHAR(20)                 NOT NULL,
         FULLNAME       VARCHAR(255)                NOT NULL,
         PASSWORD       TEXT                        ,
         SEARCHENGINE   VARCHAR(60)                 NOT NULL);''')
print("Table created successfully")


passwd = b'Thats Sir Terry to you!'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
print(str(hashed))


conn.execute(f"INSERT INTO USERS (USERNAME,FULLNAME,PASSWORD,SEARCHENGINE) \
      VALUES ('tpratchett', 'Terry Pratchett', '{str(hashed)}','Google')");
print("added user Terry")

conn.close()