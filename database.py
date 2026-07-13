import sqlite3

DB_FILE = "enquiries.db"

#creating a connection to the SQlite database
def get_connection():
    return sqlite3.connect(DB_FILE)

#creating the enquiry table
def create_enquiry_table():
    connection = get_connection()

    query = """
    CREATE TABLE IF NOT EXISTS enquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sender_name TEXT,
        sender_email TEXT,
        sender_phone TEXT,
        

        receiver_name TEXT,
        receiver_email TEXT,
        receiver_phone TEXT,
        receiver_address TEXT,

        insurance_price INTEGER,

        weight INTEGER,
        value INTEGER,
        medications INTEGER,
        makeups INTEGER, 
        electronics INTEGER,


        total_price REAL,
        promo INTEGER,
        status TEXT DEFAULT 'new'
    );
    """

    connection.execute(query)
    connection.commit()
    connection.close()

# saving enquiries
def save_enquiry(sender_info, receiver_info, quote_info, promo):
    connection = get_connection()

    query = """
    INSERT INTO enquiries (
        sender_name, sender_email, sender_phone,
        receiver_name, receiver_email, receiver_phone, receiver_address,
        weight, value, medications, makeups, electronics, insurance_price, total_price, promo
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    values = (
        sender_info["name"],
        sender_info["email"],
        sender_info["phone"],
       

        receiver_info["name"],
        receiver_info["email"],
        receiver_info["phone"],
        receiver_info["address"],

        quote_info["weight"],
        quote_info["value"],
        quote_info["medications"],
        quote_info["makeup"],
        quote_info["electronics"],
       
        quote_info["insurance_price"],

        quote_info["total_price"],
        promo

        
    )

    connection.execute(query, values)
    connection.commit()
    connection.close()

#Loading enquiries
def load_enquiries():
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    query = """     
    SELECT *
    FROM enquiries
    ORDER BY id DESC
    """

    rows = connection.execute(query).fetchall()
    connection.close()

    return [dict(row) for row in rows]



def update_enquiry_status(enquiry_id, new_status):
    connection = get_connection()

    query = """
    UPDATE enquiries
    SET status = ?
    WHERE id =?
    """

    connection.execute(query,(new_status, enquiry_id))
    connection.commit()
    connection.close()
    