from sqlite3 import connect,Row

def getall_users()->list:
    sql:str = f"SELECT * FROM `users`"
    db:object = connect("users.db")
    cursor:object = db.cursor()
    cursor.row_factory = Row
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    return data
    
def validate_user(username:str,password:str)->list:
    sql:str = f"SELECT * FROM `users` WHERE `username` = '{username}' AND `password` = '{password}'"
    db:object = connect("users.db")
    cursor:object = db.cursor()
    cursor.row_factory = Row
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    return data