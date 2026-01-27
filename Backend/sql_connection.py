import psycopg2

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = psycopg2.connect(
                database ="Grocery Store",
                user ="postgres",
                password ="12345",
                host ="localhost",
                port ="5432"
            )
    return __cnx