""" 
 Project 2: Movie Database App (N-Tier)

 Student Author: Niharika Patil
 Original author: Ellen Kidane and Prof. Joe Hummel

 Description: With the MovieLens database consists of data for over 45,000 movies, with approximately 100,000
reviews in MovieLens-100K.db and a little more than 26 million reviews in MovieLens-26M.db, the goal of this 
project is to write a console-based database application in Python, this time using an N-tier design, where 
using both SQL and Python, this project will work more with Object Relational Mapping in order to retrieve different
queries that access various fields in the movies database containing information about the movies. 

This file is the Object Tier, which is the layer within a database that encompasses all the database objects
like tables, views, stored procedures, functions, and user-defined data types. 

"""
import datatier

##################################################################
#
# Movie class:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:

   #this will set the constructor for the properties in the commments above for the Movie class
   def __init__(self, movie_id, title, release_year): 
      self._Movie_ID = movie_id
      self._Title = title
      self._Release_Year = release_year
   
   @property #this will set the movie_id property to be read only
   def Movie_ID(self):
      return self._Movie_ID

   @property #this will set the title property to be read only
   def Title(self):
      return self._Title
   
   @property #this will set the release_year property to be read only
   def Release_Year(self):
      return self._Release_Year

##################################################################
#
# MovieRating class:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:

   #this will set the constructor for the properties in the commments above for the MovieRating class
   def __init__(self, movie_id, title, release_year, num_reviews, avg_rating):
      self._Movie_ID = movie_id
      self._Title = title
      self._Release_Year = release_year
      self._Num_Reviews = num_reviews
      self._Avg_Rating = avg_rating
   
   @property #this will set the movie_id property to be read only
   def Movie_ID(self):
      return self._Movie_ID

   @property #this will set the title property to be read only
   def Title(self):
      return self._Title
   
   @property #this will set the release year property to be read only
   def Release_Year(self):
      return self._Release_Year

   @property #this will set the num_reviews property to be read only
   def Num_Reviews(self):
      return self._Num_Reviews
   
   @property
   def Avg_Rating(self): #this will set the avg_rating property to be read only
      return self._Avg_Rating

##################################################################
#
# MovieDetails class:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#
class MovieDetails:

   #this will set the constructor for the properties in the commments above for the MovieDetails class
   def __init__(self, movie_id, title, release_date, runtime, original_language, budget, revenue, num_reviews, avg_rating, tagline, genres, production_companies):
      self._Movie_ID = movie_id
      self._Title = title
      self._Release_Date = release_date
      self._Runtime = runtime
      self._Original_Language = original_language
      self._Budget = budget
      self._Revenue = revenue
      self._Num_Reviews = num_reviews
      self._Avg_Rating = avg_rating
      self._Tagline = tagline
      self._Genres = genres
      self._Production_Companies = production_companies
   
   @property #this will set the movie_id property to be read only
   def Movie_ID(self):
      return self._Movie_ID

   @property #this will set the title property to be read only
   def Title(self):
      return self._Title
   
   @property #this will set the release_date property to be read only
   def Release_Date(self):
      return self._Release_Date

   @property
   def Runtime(self): #this will set the runtime property to be read only
      return self._Runtime
   
   @property
   def Original_Language(self): #this will set the original_language property to be read only
      return self._Original_Language
   
   @property
   def Budget(self): #this will set the budget property to be read only
      return self._Budget
   
   @property
   def Revenue(self): #this will set the revenue property to be read only
      return self._Revenue
   
   @property
   def Num_Reviews(self): #this will set the num_reviews property to be read only
      return self._Num_Reviews

   @property
   def Avg_Rating(self): #this will set the avg_rating property to be read only
      return self._Avg_Rating
   
   @property
   def Tagline(self): #this will set the tagline property to be read only
      return self._Tagline

   @property
   def Genres(self): #this will set the genres property to be read only
      return self._Genres
   
   @property
   def Production_Companies(self): #this will set the production_companies property to be read only
      return self._Production_Companies

##################################################################
# 
# num_movies:
#
# Returns: the number of movies in the database, or
#          -1 if an error occurs
# 
def num_movies(dbConn):
   dbCursor = dbConn.cursor() #this will set up the cursor, connected to the database
   movies_sql = """SELECT COUNT(*) FROM Movies;""" #will retrieve the number of rows from Movies table
   row = datatier.select_one_row(dbConn, movies_sql) #catches the query from data tier

   if row is None: # failed at fetching single row
      return -1
   else:
      return row[0] #returns the first row from the tuple

##################################################################
# 
# num_reviews:
#
# Returns: the number of reviews in the database, or
#          -1 if an error occurs
#
def num_reviews(dbConn):
   dbCursor = dbConn.cursor() #this will set up the cursor, connected to the database
   movies_sql = """SELECT COUNT(*) FROM Ratings;""" #will retrieve the number of reviews from Ratings table
   row = datatier.select_one_row(dbConn, movies_sql) #catches the query from the data tier

   if row is None: # failed at fetching single row
      return -1
   else:
      return row[0] #returns the first row from the tuple


##################################################################
#
# get_movies:
#
# Finds and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all movies.
#
# Returns: list of movies in ascending order by name, or
#          an empty list, which means that the query did 
#          not retrieve any data
#          (or an internal error occurred, in which case 
#          an error message is already output).
#
def get_movies(dbConn, pattern):
   dbCursor = dbConn.cursor() #this will set up the cursor, connected to the database

   #this query wll fetch movies and their titles along with the year of release based on the title
   movies_sql = """SELECT Movie_ID, Title, strftime('%Y', Release_Date)
FROM Movies
WHERE Title LIKE ?
ORDER BY Movie_ID ASC;"""
   rows = datatier.select_n_rows(dbConn, movies_sql, (pattern,)) #catches the query from the data tier with the pattern as input

   if rows is None: #if rows fetched is empty, return an empty list
        return []

   else: #return a list of Movie objects
      movie_list = []
      for row in rows:
         one = Movie(row[0], row[1], row[2]) #creates an instance of the Movie class
         movie_list.append(one) #appends each object into the list
      return movie_list

##################################################################
#
# get_movie_details:
#
# Finds and returns details about the given movie.
# The movie ID is passed as a parameter (originally from the user)
# and the function returns a MovieDetails object.
# If no movie was found matching that ID, the function returns
# None.
#
# Returns: a MovieDetails object if the search was successful, or
#          None if the search did not find a matching movie
#          (or an internal error occurred, in which case 
#          an error message is already output).
#


def get_movie_details(dbConn, movie_id):

   #this query will retrieve the movie_id, title, date, runtime, original language, budget, revenue, number of reviews,
   #average ratings, and taglines based on the movie_id
   #the query will also join the Movies table (main table) along with the ratings and movie_taglines
   movie_sql = """
   SELECT Movies.Movie_ID, Movies.Title, strftime('%Y-%m-%d', Movies.Release_Date), 
         Movies.Runtime, Movies.Original_Language,
         Movies.Budget, Movies.Revenue,
         COUNT(Ratings.Rating) AS Num_Reviews,
         AVG(Ratings.Rating) AS Avg_Rating,
         Movie_Taglines.Tagline
   FROM Movies
   LEFT JOIN Ratings ON Movies.Movie_ID = Ratings.Movie_ID
   LEFT JOIN Movie_Taglines ON Movies.Movie_ID = Movie_Taglines.Movie_ID
   WHERE Movies.Movie_ID = ?
   GROUP BY Movies.Movie_ID;
   """
   row = datatier.select_one_row(dbConn, movie_sql, (movie_id,)) #catches the sql query

   if row is None: #if the row has an internal error
      return None

   if row == (): #if the row returns an empty tuple
      return None
   
   else: #will go through each and every element from the first sql query and check if they are Nonetype

      new_list = list(row) #first changes everything into a list to be mutable
      if row[0] is None: #for movie_id
         new_list[0] = 0
      if row[1] is None: #for title
         new_list[1] = ""
      if row[2] is None: #for release_date
         new_list[2] = ""
      if row[3] is None: #for runtime
         new_list[3] = 0
      if row[4] is None: #for original_language
         new_list[4] = ""
      if row[5] is None: #for budget
         new_list[5] = 0
      if row[6] is None: #for revenue
         new_list[6] = 0
      if row[7] is None: #for num_reviews
         new_list[7] = 0
      if row[8] is None: #for average ratings
         new_list[8] = 0.00
      if row[9] is None: #for taglines
         new_list[9] = ""

      row = tuple(new_list) #changes the list back into a tuple

   #this query will join the names of the genres with the genre_ids that are connected to a specific movie_id
   genre_sql = """
   SELECT Genres.Genre_Name
   FROM Genres
   JOIN Movie_Genres ON Genres.Genre_ID = Movie_Genres.Genre_ID
   WHERE Movie_Genres.Movie_ID = ?
   ORDER BY Genre_Name ASC;
   """
   genres = datatier.select_n_rows(dbConn, genre_sql, (movie_id,)) #will fetch the query for the genres

   if genres is None: #checks if internal error occurred
      return None

   if genres == (): #checks if thhere is an empty tuple
      return None

   if genres is not None: #returns a list with populated genre tuple objects, or it will just return an empty list
    genre_list = [] 
    for genre in genres:
        genre_list.append(genre[0]) 
   else:
      genre_list = []

   #this query will join the names of the companies with the company_ids that are connected to a specific movie_id
   company_sql = """
   SELECT Companies.Company_Name
   FROM Companies
   JOIN Movie_Production_Companies ON Companies.Company_ID = Movie_Production_Companies.Company_ID
   WHERE Movie_Production_Companies.Movie_ID = ?
   ORDER BY Company_Name ASC;
   """
   companies = datatier.select_n_rows(dbConn, company_sql, (movie_id,)) #catch the company query
   if companies is None: #checks for internal error
      return None

   if companies == (): #checks if this is an empty tuple
      return None

   if companies is not None: #returns a list with populated company tuple objects, or it will just return an empty list
      company_list = []
      for company in companies:
         company_list.append(company[0])
   else:
      company_list = []

   #populates everything above from the queries into one MovieDetails object and returns that object
   movie_details = MovieDetails(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], genre_list, company_list)

   return movie_details

##################################################################
#
# get_top_N_movies:
#
# Finds and returns the top N movies based on their average 
# rating, where each movie has at least the specified number of
# reviews.
# Example: get_top_N_movies(10, 100) will return the top 10 movies
#          with at least 100 reviews.
#
# Returns: a list of 0 or more MovieRating objects
#          note that if the list is empty, it may be because the 
#          minimum number of reviews was too high
#          (or an internal error occurred, in which case 
#          an error message is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
    dbCursor = dbConn.cursor() #sets up the cursor to the database

   #this will return the top N number of movies based on if the movies exceed a minimum number of reviews
    top_movies_sql = """
    SELECT M.Movie_ID, M.Title, strftime('%Y', M.Release_Date), 
           COUNT(R.Rating) AS Num_Reviews, 
           AVG(R.Rating) AS Avg_Rating
    FROM Movies M
    JOIN Ratings R ON M.Movie_ID = R.Movie_ID
    GROUP BY M.Movie_ID
    HAVING Num_Reviews >= ?
    ORDER BY Avg_Rating DESC, Num_Reviews DESC
    LIMIT ?;
    """

    rows = datatier.select_n_rows(dbConn, top_movies_sql, (min_num_reviews, N)) #returns the query and passes in the arguements from the user

    if rows is None: #if an internal error occurred, return an empty list
        return [] 

    else: #parse through the tuple, create a MovieRating object, and append the object(s) into a empty list
      movie_ratings = []
      for row in rows:
        one = MovieRating(row[0], row[1], row[2], row[3], row[4])
        movie_ratings.append(one)
      return movie_ratings #return the list of movie rating collected

##################################################################
#
# add_review:
#
# Inserts the given review (a rating value between 0 and 10) into
# the database for the given movie.
# It is considered an error if the movie does not exist, and 
# the review is not inserted.
#
# Returns: 1 if the review was successfully added, or
#          0 if not (e.g. if the movie does not exist, or
#                    if an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
   dbCursor = dbConn.cursor()

   #firstly checks if the movie_id existed
   check_sql = """SELECT * FROM Movies WHERE Movie_ID = ?;"""
   check_row = datatier.select_one_row(dbConn, check_sql, (movie_id,))

   if check_row is None: #if an internal error occurs after catching the query in the above line
      return 0
   if check_row == (): #if the catch returns an empty tuple
      return 0

   #if the movie_id exists, proceed by inserting a given review for the movie_id
   movies_sql = """INSERT INTO Ratings(Movie_ID, Rating)
                  VALUES(?, ?);"""
   rows = datatier.perform_action(dbConn, movies_sql, (movie_id, rating)) #use the action query function in the data tier

   if rows > 0: #if the row count returns greater than 0, then it is successfully inserted
      return 1
   else: #not successful
      return 0

##################################################################
#
# set_tagline:
#
# Sets the tagline, i.e. summary, for the given movie.
# If the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively 
# deletes the existing tagline.
# It is considered an error if the movie does not exist, and 
# the tagline is not set.
#
# Returns: 1 if the tagline was successfully set, or
#          0 if not (e.g. if the movie does not exist, or
#                    if an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
   dbCursor = dbConn.cursor()

   #first grabs the query to check if the movie_id exists
   check_sql = "SELECT * FROM Movies WHERE Movie_ID = ?;"
   check_row = datatier.select_one_row(dbConn, check_sql, [movie_id,])

   #will make an attempt to update the query first
   update_sql = "UPDATE Movie_Taglines SET Tagline = ? WHERE Movie_ID = ?;"
   rows_affected = datatier.perform_action(dbConn, update_sql, [tagline, movie_id])

   if rows_affected == 0: #if the number of rows that are update returns 0
      if len(check_row) == 0: #check if the movie_id even exists by checking length of the tuple
         return 0
      else: #if the movie id exists, but there is no tagline that exists, then insert a new entry
         insert_sql = "INSERT INTO Movie_Taglines (Movie_ID, Tagline) VALUES (?, ?);"
         rows_affected2 = datatier.perform_action(dbConn, insert_sql, [movie_id, tagline])

         if rows_affected2 == 0: #if it does not update, then it is not successful
            return 0
         else: #insertion was successful
            return 1
   else: #update was successful
      return 1

     