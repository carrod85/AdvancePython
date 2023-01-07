# Homework 2

Databases and Python. Deadline 24.04.2022
There are 8 diners* in different buildings of TalTech:

| Location                                                                     | Service provider              | Open                                                                   |
|------------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------|
| Economics- and social science building canteen Akadeemia tee 3 SOC- building | Rahva Toit                    | 8.30-18.30 Saturday: 8.30-15.30 Sunday: closed                         |
| Library canteen Akadeemia tee 1/Ehitajate tee 7                              |  Rahva Toit                   | 8.30-19.00 Saturday/Sunday: closed                                     |
| Main building Deli cafe Ehitajate tee 5 U01 building                         | Baltic Restaurants Estonia AS | Monday-Thursday: 9.00-16.30 Friday: 9.00-16.00 Saturday/Sunday: closed |
| Main building Daily lunch restaurant Ehitajate tee 5 U01 building            | Baltic Restaurants Estonia AS | 9.00-16.30 Friday: 9.00-16.00 Saturday/Sunday: closed                  |
| U06 building canteen                                                         | Rahva toit                    | 9.00-16.00 Saturday/Sunday: closed                                     |
| Natural Science building canteen Akadeemia tee 15 SCI building               | Baltic Restaurants Estonia AS | 9.00-16.00 Saturday/Sunday: closed                                     |
| ICT building canteen Raja 15/Mäepealse 1                                     | Baltic Restaurants Estonia AS | 9.00-16.00 Saturday/Sunday: closed                                     |
| Sports building canteen Männiliiva 7 S01 building                            | TTÜ Sport OÜ                  | 11.00-20.00 Saturday/Sunday: By agreement                              |


There are 4 service providers in total: Rahva Toit, Baltic Restaurants Estonia AS, TTÜ Sport and Bitstop Kohvik OÜ.

There are different opening hours for every canteen.

Task:
A) Use plain SQL language

1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER

Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter).

Table Provider fields: ID, ProviderName.

If you want, you may add some additional fields, but not necessary.

2) Insert IT College canteen data by separate statement, other canteens as one list.

3) Create query for canteens which are open 16.15-18.00

4) Create query for canteens which are serviced by Rahva Toit. NB! Create query by string "Rahva Toit" not by direct ID!.

B) Use SqlAlchemy or any other ORM and solve p 1-4 again! Please create different database.



Additional Information:
Tests and GUI are not necessary.

Add documentation and comments.

Hints: SQLite datatypes: https://www.sqlite.org/datatype3.html

How to join and query data from related tables using SQLAlchemy: https://community.snowflake.com/s/article/How-to-Join-2-tables-using-SQL-Alchemy

Questions are welcome: einar.kivisalu@taltech.ee

