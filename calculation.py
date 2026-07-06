import sqlite3

#initialising database
def get_connection(enquiries):
    try:
        return sqlite3.connect(enquiries)
    except Exception as e:
        print(f"error:{e}")
        raise



# creating a table in the database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
    """
    try:
        with connection:
            connection.execute(query)
        print ("table was createed")
    except Exception as e:
        print (e)

   
# Main function
def main():
    connection = get_connection("Enquiries.db")
    try:
        create_table(connection)
        
        x = int(input ("1, 2"))
        while x != 2:
             start = input("Enter option(Add, Delete, Update, Search, Add Many):").lower()
             if start == 'add':
                name = input("Name:")
                age= int(input("Enter age:"))
                email = input("Enter email: ")
                insert_user(connection, name, age, email)
             elif start == 'search':
                print("ALL users:")
                for user in fetch_user(connection):
                    print(f"user:{user}")
             elif start == 'delete':
                 user_id= int(input("Enter User ID:"))
                 delete_user(connection,user_id)

             elif start == 'update':
                 user_id = int(input("Enter user ID:"))
                 new_email = input("Enter a new email:")
                 update_user(connection, user_id, new_email)
        

             elif start == "add many":
                 users = [("chan", 29, "friend@gmail.com"),
                        ("truman", 27, "show@gmail.com"),
                        ]
                 insert_users(connection, users)


    finally:
        connection.close()



#Add user ot the database
def insert_user(connection, name:str, age:int, email:str):
  query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
  try:
     with connection:
            connection.execute(query, (name, age, email))
     print (f"user {name} was added to the data base!")

  except Exception as e:
      print(e)

# Query on all users in the database
def fetch_user(connection, condition: str=None) -> list[tuple]:

    query = "SELECT * from users"
    if condition:
        query == f" WHERE {condition}"

    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)


#Delete user from database
def delete_user(connection, user_id: int):
    query ="DELETE FROM users WHERE id =?"

    try:
      with connection:
        connection.execute(query,(user_id,))
      print(f"USER id {user_id} was deleted!")
    except Exception as e:
        print(e)


#updating status of an existing user
def update_user(connection, user_id:int, email:str):
    query ="UPDATE users SET email =? WHERE id = ?"

    try:
        with connection:
            connection.execute(query,(email,user_id))
        print(f"USERID {user_id} has a new email of {email}")

    except Exception as e:
        print(e)


#Adding multiple Users to the same table
def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"

    try:
        with connection:
            connection.executemany(query, users)
        print(f"len{users} were added to the database")
    except Exception as e:
        print(e)






if __name__ == "__main__":
    main()
