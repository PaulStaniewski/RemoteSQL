import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from prettytable import from_db_cursor


def menu():

    print('Welcome to the Remote SQL Tool by Paul S.\n')  # print the welcome message
    program_running = True  # set the program_running variable to True

    while program_running:  # while the program is running

        host = "127.0.0.1"  # set the host
        port = 3306  # set the port
        user = ""  # set the user
        password = ""  # set the password

        db = MySQLdb.connect(host=host, port=port, user=user, password=password)  # connect to the database
        cur = db.cursor()  # create a cursor

        x = input("What you want to do?"  # menu options
                  "\n(1) Show all databases."  
                  "\n(2) Create a database."
                  "\n(3) Delete a database."
                  "\n(4) Create a table."
                  "\n(5) View a tables."
                  "\n(6) Show fields in table"
                  "\n(7) Insert data into table."                  
                  "\n(8) SELECT (item or *) FROM table."
                  "\n(9) Add column to existing table."
                  "\n(10) Update data in column."
                  "\n(11) Delete column from existing table."
                  "\n(12) Exit."
                  "\n"
                  "\nPlease enter a number: ")
        try:
            match x:  # match the input to the menu options
                case "1":  # Show databases
                    with db:  # with the database
                        cur.execute("SHOW DATABASES")  # execute the SQL query
                        x = from_db_cursor(cur)  # create a table from the query
                    print(x)  # print the table
                case "2":  # Create a database
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"CREATE DATABASE {database_name}")  # execute the SQL query
                    print(f"\nDatabase {database_name} created.\n")   # print the database is created
                case "3":  # Delete a database
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"DROP DATABASE {database_name}")  # execute the SQL query
                    print(f"\nDatabase {database_name} deleted.\n")  # print the database is deleted
                case "4":  # Create a table
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"USE {database_name}")  # execute the SQL query
                    table_name = input("Enter the name of new table: ")  # ask the user for the table name
                    how_many_columns = int(input("How many columns do you want to create? "))  # ask the user how
                    # many columns they want to create
                    column_names = []  # create an empty list for the column names
                    column_types = []  # create an empty list for the column types
                    for i in range(how_many_columns):  # for the number of columns
                        column_name = input(f"Enter the name of column {i + 1}: ")  # ask the user for the column name
                        column_names.append(column_name)  # add the column name to the list
                        column_type = input(f"Enter the type of column {i + 1}: ")  # ask the user for the column type
                        column_types.append(column_type)  # add the column type to the list
                    cur.execute(f"CREATE TABLE {table_name} ({column_names[0]} {column_types[0]} PRIMARY KEY)")
                    # execute the SQL query
                    for i in range(1, how_many_columns):  # for the number of columns
                        cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_names[i]} {column_types[i]}")
                        # execute the SQL query
                    print(f"\nTable {table_name} created.\n")  # print the table is created
                case "5":  # Show a tables in database.
                    with db:  # with the database
                        database_name = input("Enter the database name: ")  # ask the user for the database name
                        cur.execute(f"USE {database_name}")  # execute the SQL query
                        cur.execute(f"SHOW TABLES;")  # execute the SQL query
                        x = from_db_cursor(cur)  # create a table from the query
                    print(x)  # print the table
                case "6":  # Show fields in table.
                    with db:  # with the database
                        database_name = input("Enter the database name: ")  # ask the user for the database name
                        cur.execute(f"USE {database_name}")  # execute the SQL query
                        table_name = input("Enter the table name: ")  # ask the user for the table name
                        cur.execute(f"SHOW fields FROM {table_name}")  # execute the SQL query
                        x = from_db_cursor(cur)  # create a table from the query
                    print(x)  # print the table
                case "7":  # Insert data into table.
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"USE {database_name}")  # execute the SQL query
                    table_name = input("Enter the table name: ")  # ask the user for the table name
                    print("Names of columns must be separated by commas.")  # information how to enter data
                    print("e.g. name, age, city")
                    column_name = input("Enter the names of columns: ")  # ask the user for the column names
                    print("Values must be in the same order as the columns and in quote.")
                    print('e.g. "value1", "value2", "value3"')  # information how to enter data
                    column_value = input("Enter the values u want to entry: ")  # ask the user for the column values
                    cur.execute(f"INSERT INTO {table_name}({column_name}) VALUES ({column_value})")  # execute the SQL
                    print(f"\nData {column_value} inserted into {column_name}.\n")  # print the data is inserted
                    db.commit()  # commit the changes
                case "8":  # SELECT item or * FROM table
                    with db:  # with the database
                        database_name = input("Enter the database name: ")  # ask the user for the database name
                        cur.execute(f"USE {database_name}")  # execute the SQL query
                        table_name = input("Enter the table name: ")  # ask the user for the table name
                        item = input("Enter the item you want to select: ")  # ask the user for the item
                        cur.execute(f"SELECT {item} FROM {table_name}")  # execute the SQL query
                        x = from_db_cursor(cur)  # create a table from the query
                    print(x)  # print the table
                case "9":  # Add column to existing table.
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"USE {database_name}")  # execute the SQL query
                    table_name = input("Enter the table name: ")  # ask the user for the table name
                    column_name = input("Enter the new column name: ")  # ask the user for the new column name
                    column_type = input("Enter the column type: ")  # ask the user for the column type
                    cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")  # execute the SQL
                    print(f"\nColumn {column_name} added to table {table_name}.\n")  # print the column is added
                case "10":  # Update one record in column.
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"USE {database_name}")  # execute the SQL query
                    print("\nSyntax: UPDATE table_name SET column = new_value WHERE primary_key = primary_key_value;\n")
                    # information how look syntax
                    table_name = input("Enter the table name which u want update: ")  # ask the user for the table name
                    column_name = input("Enter the column name which u want update: ")
                    # ask the user for the column name
                    new_value = input("Enter the new value: ")  # ask the user for the new value
                    primary_key = input("Enter the primary key: ")  # ask the user for the primary key
                    primary_key_value = input("Enter the primary key value: ")  # ask the user for the primary key value
                    cur.execute(f"UPDATE {table_name} SET {column_name} = '{new_value}'"  
                                f" WHERE {primary_key} = {primary_key_value};")  # execute the SQL query
                    print(f"\nColumn {column_name} updated with {new_value}"  
                          f" where {primary_key} = {primary_key_value}\n")  # print the column is updated
                    db.commit()  # commit the changes
                case "11":  # Drop column from existing table.
                    database_name = input("Enter the database name: ")  # ask the user for the database name
                    cur.execute(f"USE {database_name}")  # execute the SQL query
                    table_name = input("Enter the table name: ")  # ask the user for the table name
                    column_name = input("Enter the column name: ")  # ask the user for the column name
                    cur.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")  # execute the SQL query
                    print(f"\nColumn {column_name} dropped from table {table_name}.\n")   # print the column is dropped
                case "12":  # Exit
                    print("\nThank you for using this program.")  # print a thank you note for using the program
                    program_running = False  # set the program_running to False
                case _:  # if the user enter something else
                    print("\nPlease enter a valid number.\n")  # print the user enter a wrong value
        except MySQLdb.Error as e:  # if there is an error
            print("\n", e, "\n")  # print the error


def main():  # main function
    menu()  # call the menu function


if __name__ == "__main__":  # if the program is run directly
    main()  # call the main function
