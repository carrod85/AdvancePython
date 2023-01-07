"""Homework 2 -part B. """

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

meta = MetaData()


def _fk_pragma_on_connect(dbapi_con, con_record):
    """enable foreign key constraint in database"""
    dbapi_con.execute('pragma foreign_keys=ON')


def create_db():
    """Create database + connect to database"""

    global engine
    engine = create_engine('sqlite:///dinersORM.db', echo=False)
    event.listen(engine, 'connect', _fk_pragma_on_connect)
    global conn
    conn = engine.connect()
    print("Database dinersORM.db opened successfully!")


def create_table_provider():
    """create a table PROVIDER in the previously created database"""
    global provider
    provider = Table(
        'PROVIDER', meta,
        Column('ID', Integer, primary_key=True),
        Column('PROVIDER_NAME', String),
    )
    meta.create_all(engine)
    print("Table PROVIDER created successfully")


def create_records_provider():
    """create some records in the PROVIDER table"""

    conn.execute(provider.insert(), [
        {'ID': 1, 'PROVIDER_NAME': 'bitStop Kohvik OÜ'},
        {'ID': 2, 'PROVIDER_NAME': 'Rahva Toit'},
        {'ID': 3, 'PROVIDER_NAME': 'Baltic Restaurants Estonia AS'},
        {'ID': 4, 'PROVIDER_NAME': 'TTÜ Sport OÜ'},
    ])

    print("Records in the table PROVIDER created successfully")


def create_table_canteen():
    """create a table CANTEEN in the previously created database"""

    global canteen
    canteen = Table(
        'CANTEEN', meta,
        Column('ID', Integer, primary_key=True),
        Column('PROVIDER_ID', Integer, ForeignKey("PROVIDER.ID"), nullable=False),
        Column('NAME', String),
        Column('LOCATION', String),
        Column('TIME_OPEN', Integer),
        Column('TIME_CLOSED', Integer),
    )
    meta.create_all(engine)
    print("Table CANTEEN created successfully")


def create_records_canteen():
    """create some records in the CANTEEN table"""

    conn.execute(canteen.insert(), [
        {'PROVIDER_ID': 1, 'NAME': 'bitStop Kohvik OÜ', 'LOCATION': 'IT College, Raja 4c', 'TIME_OPEN': 9.30,
         'TIME_CLOSED': 16.00},
        {'PROVIDER_ID': 2, 'NAME': 'Economics- and social science building canteen',
         'LOCATION': 'Akadeemia tee 3 SOC- building', 'TIME_OPEN': 8.30, 'TIME_CLOSED': 18.30},
        {'PROVIDER_ID': 2, 'NAME': 'Library canteen', 'LOCATION': 'Akadeemia tee 1/Ehitajate tee 7', 'TIME_OPEN': 8.30,
         'TIME_CLOSED': 19.00},
        {'PROVIDER_ID': 3, 'NAME': 'Main building Deli cafe', 'LOCATION': 'Ehitajate tee 5 U01 building',
         'TIME_OPEN': 9.00, 'TIME_CLOSED': 16.30},
        {'PROVIDER_ID': 3, 'NAME': 'Main building Daily lunch restaurant', 'LOCATION': 'Ehitajate tee 5 U01 building',
         'TIME_OPEN': 9.00, 'TIME_CLOSED': 16.30},
        {'PROVIDER_ID': 2, 'NAME': 'U06 building canteen', 'LOCATION': 'U06 building',
         'TIME_OPEN': 9.00, 'TIME_CLOSED': 16.00},
        {'PROVIDER_ID': 3, 'NAME': 'Natural Science building canteen', 'LOCATION': 'Akadeemia tee 15 SCI building',
         'TIME_OPEN': 9.00, 'TIME_CLOSED': 16.00},
        {'PROVIDER_ID': 3, 'NAME': 'ICT building canteen', 'LOCATION': 'Raja 15/Mäepealse 1',
         'TIME_OPEN': 9.00, 'TIME_CLOSED': 16.00},
        {'PROVIDER_ID': 4, 'NAME': 'Sports building canteen', 'LOCATION': 'Männiliiva 7 S01 building',
         'TIME_OPEN': 11.00, 'TIME_CLOSED': 20.00},
    ])


def select_opening():
    """
       fetch and display records from the CANTEEN table,
       showing the canteens open continuosly between 16.15 and 18.00."""

    print("\n\n", "The canteens that keep open from 16.15 to 18.00 are:", "\n")

    result = conn.execute('SELECT * FROM CANTEEN WHERE TIME_OPEN<=16.15 AND TIME_CLOSED>=18.00;')
    for row in result:
        print("-", row['NAME'], "\n")


def select_rahva_toit():
    """
    fetch and display records of canteen namess from the CANTEEN table join with the PROVIDER table,
    so that those cantines are the ones managed by Rahva Toit.
    """
    result = conn.execute("SELECT NAME FROM CANTEEN JOIN PROVIDER\
        ON  PROVIDER_ID=PROVIDER.ID WHERE PROVIDER_NAME='Rahva Toit'")

    print("\n\n", "The canteens which are serviced by Rahva Toit are: ", "\n")

    for row in result:
        print("-", row['NAME'], "\n")


def test_error():
    conn.execute("INSERT INTO CANTEEN VALUES (13, 6, 'CS', 'TALLIN', 12.0, 2312)")


def close_conn():
    """close connection"""

    conn.close()
    print("\n\n", "Connection closed")


if __name__ == "__main__":
    create_db()
    # create_table_provider()
    # create_records_provider()
    # create_table_canteen()
    # create_records_canteen()
    # test_error()
    select_opening()
    select_rahva_toit()
    close_conn()
