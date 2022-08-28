"""Homework 2 -part A. Carlos Rodriguez 201841IVSB"""

import sqlite3


def open_db():
    """open SQLite database diners.db. if it doesn't exist it is created"""

    global conn
    conn = sqlite3.connect('diners.db')
    print("Database diners.db opened successfully!")



def create_table_provider():
    """create a table PROVIDER in the previously created database"""

    conn.execute('''CREATE TABLE `PROVIDER`
        (ID                     INT NOT NULL,
        PROVIDER_NAME           CHAR(50) NOT NULL,
        PRIMARY KEY (ID)
        );''')

    print ("Table PROVIDER created successfully")


def create_records_provider():
    """create some records in the PROVIDER table"""

    conn.execute("INSERT INTO 'PROVIDER' ('ID', PROVIDER_NAME) VALUES \
        (1,'bitStop Kohvik OÜ'), (2, 'Rahva Toit'), (3, 'Baltic Restaurants Estonia AS'), (4, 'TTÜ Sport OÜ')")

    conn.commit()
    print("Records in the table PROVIDER created successfully")

def create_table_canteen():
    """create a table CANTEEN in the previously created database"""

    conn.execute('''CREATE TABLE CANTEEN
        (ID                     INT NOT NULL,
        PROVIDER_ID             INT NOT NULL, 
        `NAME`                  CHAR(50) NOT NULL,
        `LOCATION`              CHAR(50) NOT NULL,
        TIME_OPEN               TIME NOT NULL,
        TIME_CLOSED             TIME NOT NULL,
        PRIMARY KEY (ID),
        FOREIGN KEY (PROVIDER_ID) REFERENCES `PROVIDER`(ID)
        );''')

    print("Table CANTEEN created successfully")


def create_records_canteen():
    """create some records in the CANTEEN table"""

    conn.execute("INSERT INTO CANTEEN ('ID', PROVIDER_ID,`NAME`,`LOCATION`,TIME_OPEN,TIME_CLOSED) \
        VALUES (1, 1, 'bitStop Kohvik OÜ', 'IT College, Raja 4c', 9.30, 16.00)")

    conn.execute("INSERT INTO CANTEEN ('ID',PROVIDER_ID,`NAME`,`LOCATION`,TIME_OPEN,TIME_CLOSED) VALUES \
        (2, 2, 'Economics- and social science building canteen', 'Akadeemia tee 3 SOC- building', 8.30, 18.30),\
        (3, 2, 'Library canteen', 'Akadeemia tee 1/Ehitajate tee 7', 8.30, 19.00),\
        (4, 3, 'Main building Deli cafe', 'Ehitajate tee 5 U01 building', 9.00, 16.30),\
        (5, 3, 'Main building Daily lunch restaurant', 'Ehitajate tee 5 U01 building', 9.00, 16.30),\
        (6, 2, 'U06 building canteen', 'U06 building', 9.00, 16.00),\
        (7, 3, 'Natural Science building canteen', 'Akadeemia tee 15 SCI building', 9.00, 16.00),\
        (8, 3, 'ICT building canteen', 'Raja 15/Mäepealse 1', 9.00, 16.00),\
        (9, 4, 'Sports building canteen', 'Männiliiva 7 S01 building', 11.00, 20.00)")

    conn.commit()
    print("Records in the table CANTEEN created successfully")


def select_opening():
    """
    fetch and display records from the CANTEEN table,
    showing the canteens open continuosly between 16.15 and 18.00."""

    cursor = conn.execute("SELECT `NAME` FROM CANTEEN WHERE TIME_OPEN<=16.15 AND TIME_CLOSED>=18.00")

    print("\n\n", "The canteens that keep open from 16.15 to 18.00 are:", "\n")

    for row in cursor:
        print("-", row[0], "\n")


def select_rahva_toit():
    """
    fetch and display records of canteen namess from the CANTEEN table join with the PROVIDER table,
    so that those cantines are the ones managed by Rahva Toit.
    """

    cursor = conn.execute("SELECT `NAME` FROM CANTEEN JOIN `PROVIDER`\
        ON  PROVIDER_ID=`PROVIDER`.ID WHERE PROVIDER_NAME='Rahva Toit'")

    print("\n\n", "The canteens which are serviced by Rahva Toit are: ", "\n")

    for row in cursor:
        print("-",row[0], "\n")


def close_conn():
    """close connection"""

    conn.close()
    print ("\n\n", "Connection closed")


if __name__ == "__main__":
    open_db()
    #create_table_canteen()
    #create_table_provider()
    #create_records_canteen()
    #create_records_provider()
    select_opening()
    select_rahva_toit()
    close_conn()