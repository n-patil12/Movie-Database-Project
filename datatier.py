""" 
 Project 2: Movie Database App (N-Tier)

 Student Author: Niharika Patil
 Original author: Ellen Kidane and Prof. Joe Hummel

 Description: With the MovieLens database consists of data for over 45,000 movies, with approximately 100,000
reviews in MovieLens-100K.db and a little more than 26 million reviews in MovieLens-26M.db, the goal of this 
project is to write a console-based database application in Python, this time using an N-tier design, where 
using both SQL and Python, this project will work more with Object Relational Mapping in order to retrieve different
queries that access various fields in the movies database containing information about the movies. 

This file is the Data Tier, which is responsible for handling interactions between an application and its database,
and acts as a bridge between the object-oriented code and the relational database.

"""
# datatier.py
# Executes SQL queries against the given database.
import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL SELECT query,
# executes this query against the database and returns
# the first row retrieved by the query. If no data was 
# retrieved, the empty tuple () is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: - first row retrieved by the given query, or
#          - () if no data was retrieved, or
#          - None if an error occurs (with a message printed).
#
def select_one_row(dbConn, sql, parameters = None): #will retrieve only the first row
   if (parameters == None): #sets up an empty list to load SQL results
      parameters = []
   
   dbCursor = dbConn.cursor() #sets up the cursor for database

   try: 
      dbCursor.execute(sql, parameters) #executes the SQL + puts result into the list
      single_row = dbCursor.fetchone() #fetches a single row

      if single_row is None: #checks if anything is returned from the query
         return ()
      else:
         return single_row #returns the row that was fetched

   except Exception as err: #returns None when there is an error in the query
      print("select_one_row failed:", err)
      return None

   finally: #closes the cursor
      dbCursor.close()


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL SELECT query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: - a list of 0 or more rows, or
#          - None if an error occurs (with a message printed).
#
def select_n_rows(dbConn, sql, parameters = None): #will retrieve all the rows from the query
   if (parameters == None): #sets up an empty list to load SQL results
      parameters = []
   
   dbCursor = dbConn.cursor() #sets up the cursor for database

   try: 
      dbCursor.execute(sql, parameters) #executes the SQL + puts result into the list
      rows = dbCursor.fetchall() #fetches all of the rows
      return rows

   except Exception as err: #returns None when there is an error in the query
      print("select_n_rows failed:", err)
      return None

   finally: #closes the cursor
      dbCursor.close()



##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the number of rows
# modified. A return value of 0 means no rows were
# updated.
# Action queries are typically "insert", "update", 
# and "delete".
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: - the number of rows modified by the query, or
#          - -1 if an error occurs (with a message printed).
#          A return value of 0 is not considered an error.
#          It simply means that the query did not change
#          the database.
#
def perform_action(dbConn, sql, parameters = None): #will retrieve the number of rows from the action queries
   if (parameters == None):
      parameters = []
   
   dbCursor = dbConn.cursor() #create a cursor to the database connection

   try:
      dbCursor.execute(sql, parameters) #execute the action query
      dbConn.commit() #commits the changes to data
      return dbCursor.rowcount #returns the number of rows that were modified
   except Exception as err:
      print("perform_action failed:", err) #prints error message if query fails
      return -1
   finally: #close cursor connection
      dbCursor.close()