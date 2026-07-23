import sqlite3
import os



DB_FILE = os.getenv("DB_FILE", "enquiries.db")


def get_connection():
    """
    Establishes a connection the database.
    """
    return sqlite3.connect(DB_FILE)


def create_enquiry_table():

    """
   Creates the enquiries table if it does not already exist.
   The table stores customer details, shipment information,
   pricing and enquiry status.
    """

    """"""
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


def save_enquiry(sender_info, receiver_info, quote_info, promo):

    """
    Responsible for saving an enquiry and its necessary attributes.
    """
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


def load_enquiries():
    """
    Loads every enquiry stored in the database and returns
    them ordered from newest to oldest based on their ID.
    """
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
    """
    Modifies the status of a quote in the database based on its ID.
    """
    connection = get_connection()

    query = """
    UPDATE enquiries
    SET status = ?
    WHERE id =?
    """

    connection.execute(query,(new_status, enquiry_id))
    connection.commit()
    connection.close()





def create_statistics_table():
    connection = sqlite3.connect(DB_FILE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS statistics (
            quote_calculations INTEGER
        )
    """)

    connection.execute("""
        INSERT INTO statistics (quote_calculations)
        SELECT 0
        WHERE NOT EXISTS (SELECT * FROM statistics)
    """)
    connection.commit()
    connection.close()
    


def increment_quote_calculations():
    connection = sqlite3.connect(DB_FILE)

    connection.execute(
            "UPDATE statistics SET quote_calculations = quote_calculations + 1"
        )

    connection.commit()
    connection.close()



def get_quote_calculations():
    connection = sqlite3.connect(DB_FILE)

    result = connection.execute(
        "SELECT quote_calculations FROM statistics"
    ).fetchone()

    connection.close()

   

    return result[0]