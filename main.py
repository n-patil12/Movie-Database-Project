""" 
 Project 2: Movie Database App (N-Tier)

 Student Author: Niharika Patil
 Original author: Ellen Kidane and Prof. Joe Hummel

 Description: With the MovieLens database consists of data for over 45,000 movies, with approximately 100,000
reviews in MovieLens-100K.db and a little more than 26 million reviews in MovieLens-26M.db, the goal of this 
project is to write a console-based database application in Python, this time using an N-tier design, where 
using both SQL and Python, this project will work more with Object Relational Mapping in order to retrieve different
queries that access various fields in the movies database containing information about the movies. 

This file is the Main, which is going to go through all of the command and the functionality of the application,
and will work with both the Object Tier and the Data Tier

"""
import sqlite3
import objecttier

def command_1(dbConn): #this function will retrieve general info about the database
    print()
    print("General Statistics:")
    movie_stats = objecttier.num_movies(dbConn)
    review_stats = objecttier.num_reviews(dbConn)

    print(f" Number of Movies: {movie_stats:,}") #print the number of movies in the database
    print(f" Number of Reviews: {review_stats:,}") #print the number of reviews in the database

def command_2(dbConn): #this will retrieve the number of movies based on user input
    print()
    user_input = input("Enter the name of the movie to find (wildcards _ and % allowed): ")
    movies_returned = objecttier.get_movies(dbConn, user_input) #will take in cursor and the name of the movie

    print()
    print("Number of Movies Found:", len(movies_returned)) #return how many movies are found after the fetch

    if len(movies_returned) > 0: #if the fetch returns something more than 0 movies
        if len(movies_returned) > 100: #if there are too many movies being fetched
            print("There are too many movies to display (more than 100). Please narrow your search and try again.")
        else:
            for mov in movies_returned: #print out the basic info about the movie using properties from the movie class
                print(f"{mov.Movie_ID} : {mov.Title} ({mov.Release_Year})")

def command_3(dbConn): #this function will retrieve details about a certain movie
    print()
    user_input = input("Enter a movie ID: ") #will grab movie id that user wants to see movie details about

    details = objecttier.get_movie_details(dbConn, user_input) #return the results from the query

    if details is None: #if there is an internal error or no match was found from the movie id
        print()
        print("No movie matching that ID was found in the database.")
    else: #will print out the results from the fetch, and let users see movie details
        print()
        print(f"{details.Movie_ID} : {details.Title}") #movie id from user + movie title
        print(f"  Release date: {details.Release_Date}") #release date of movie
        print(f"  Runtime: {details.Runtime} (minutes)") #duration of movie
        print(f"  Original language: {details.Original_Language}") #language the movie is in
        print(f"  Budget: ${details.Budget:,} (USD)") #budget of movie
        print(f"  Revenue: ${details.Revenue:,} (USD)") #how much the movie made
        print(f"  Number of reviews: {details.Num_Reviews}") #number of reviews of the movie
        print(f"  Average rating: {details.Avg_Rating:.2f} (0-10)") #average rating users gave about the movie
        print(f"  Genres: ", end= "")
        if len(details.Genres) > 0:  #since genres is a list structure, will check if genres list contains information   
            for i in range(0, len(details.Genres), 1):
                print(f"{details.Genres[i]}, ", end="")  #prints the different genres the movie is under
        print()
        print(f"  Production companies: ", end="") #will repeat similar process as genres with production companies list
        if len(details.Production_Companies) > 0:
            for i in range(0, len(details.Production_Companies), 1):
                print(f"{details.Production_Companies[i]}, ", end="") #prints out the different production companies

        print()
        print(f"  Tagline: {details.Tagline}") #summarization of a movie's theme/mood

def command_4(dbConn): #will output the top number of movie that recieves at least more than a certain amount of reviews
    print()
    user_input = input("Enter a value for N: ")
    if int(user_input) < 1: #if the limit is 0, then it will produce possibly a large output for minimum reviews, and also N cannot be negative
        print("Please enter a positive value for N.")
        return
        
    second_user_input = input("Enter a value for the minimum number of reviews: ")
    if int(second_user_input) < 1: #checks if minimum number of reviews are negative or are 0
        print("Please enter a positive value for the minimum number of reviews.")
        return

    else:
        n_movies = objecttier.get_top_N_movies(dbConn, int(user_input), int(second_user_input))
        if len(n_movies) == 0: #if the fetch did not return anything
            print()
            print("No movies were found that fit the criteria.")
        elif len(n_movies) > 0: #will go through each index of movie_rating objects, and print info stored in eachh object
            print() 
            for i in range(0, len(n_movies), 1):
                print(f"{n_movies[i].Movie_ID} : {n_movies[i].Title} ({n_movies[i].Release_Year}), Average rating = {n_movies[i].Avg_Rating:.2f} ({n_movies[i].Num_Reviews} reviews)")

def command_5(dbConn): #will add or edit reviews based on movie_id input
    print()
    user_input = input("Enter a value for the new rating (0-10): ")
    if int(user_input) < 0 or int(user_input) > 10: #user will be asked to input a review number from 0-10
        print("Invalid rating. Please enter a value between 0 and 10 (inclusive).")
        return
    
    second_user_input = input("Enter a movie ID: ") #user will be asked to input movie id

    adding_reviews = objecttier.add_review(dbConn, second_user_input, int(user_input)) 

    if adding_reviews == 0: #if fetch returns 0, then no movies were found based on id
        print()
        print("No movie matching that ID was found in the database.")
    elif adding_reviews == 1: #if movie was 1, then ratings were inserted into database
        print()
        print("Rating was successfully inserted into the database.")

def command_6(dbConn): #this function will update/insert a tagline based on an existing movie id
    print()
    user_input = input("Enter a tagline: ") #user will enter tagline of their choice
    second_user_input = input("Enter a movie ID: ") #user will be asked to enter a movie id

    setting_reviews = objecttier.set_tagline(dbConn, second_user_input, user_input)

    if setting_reviews == 0: #if the return is 0, then no movies were found based on the id
        print()
        print("No movie matching that ID was found in the database.")
    elif setting_reviews == 1: #tagline was either successfully updated or inserted
        print()
        print("Tagline was successfully set in the database.")


##################################################################  
#this is the intro section and handles everything in the main

def menu(): #this is the menu for the app
    print()
    print("Select a menu option: ")
    print("  1. Print general statistics about the database")
    print("  2. Find movies matching a pattern for the name")
    print("  3. Find details of a movie by movie ID")
    print("  4. Top N movies by average rating, with a minimum number of reviews")
    print("  5. Add a new review for a movie")
    print("  6. Set the tagline of a movie")
    print("or x to exit the program.")


if __name__ == "__main__": #main

    #prints out the introduction to the application
    print("Project 2: Movie Database App (N-Tier)")
    print("CS 341, Spring 2025")
    print()
    print("This application allows you to analyze various")
    print("aspects of the MovieLens database.")
    print()
    dbName = input("Enter the name of the database you would like to use: ")
    dbConn = sqlite3.connect(dbName) #connects to the database
    print()
    print("Successfully connected to the database!")

    app_cont = True #boolean value that keeps application going
    while (app_cont):
        menu()
        cmd = input("Your choice --> ")
        if (cmd == "1"): #retrieves general statistics about database
            command_1(dbConn)
        elif (cmd == "2"): #retrieves different movies
            command_2(dbConn)
        elif (cmd == "3"): #retrives movie details
            command_3(dbConn)
        elif (cmd == "4"): #retrieves top N movies with minimum movie reviews
            command_4(dbConn)
        elif (cmd == "5"): #adds review based on user input movie id
            command_5(dbConn)
        elif (cmd == "6"): #sets a tagline (update or insert) based on user input movie id
            command_6(dbConn)
        elif (cmd == "x"): #user will exit out of program
            app_cont = False
        else: #commands that are not matching to if statements
            print("Error, unknown command, try again...")

    #user is now exiting the program
    print()
    print("Exiting program.")