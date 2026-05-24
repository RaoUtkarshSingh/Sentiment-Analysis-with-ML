import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kundan123*",   
        database="sentiment_db"
    )

def insert_prediction(review, cleaned, prediction, confidence):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO predictions (review, cleaned, prediction, confidence)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (review, cleaned, prediction, confidence))
    conn.commit()

    cursor.close()
    conn.close()