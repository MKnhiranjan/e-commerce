import sqlite3

def sqlite_to_sql(input_db, output_sql):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(input_db)
        cursor = connection.cursor()

        # Dump the database contents to a SQL file
        with open(output_sql, 'w') as sql_file:
            for line in connection.iterdump():
                sql_file.write('%s\n' % line)

        print("SQLite database dumped to SQL file successfully!")

    except sqlite3.Error as error:
        print("Error while connecting to SQLite database:", error)
    finally:
        if connection:
            connection.close()

# Provide input and output file paths
input_db = 'db.sqlite3'  # Input SQLite database file
output_sql = 'db_dump.sql'  # Output SQL file

# Convert SQLite to SQL
sqlite_to_sql(input_db, output_sql)
