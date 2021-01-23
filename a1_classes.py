"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from moviecollection import MovieCollection

def main():
    movies = MovieCollection()
    movies.load_movies('movies.csv')
    # input_file = open("movies.csv", "r")
    # movies = input_file.readlines()
    print("Movies To Watch 1.0 - by <Shen Zhaozhe>")
    print('{} movies loaded'.format(len(movies)))

    # print the menu for choosing
    while True:
        print("Menu:\nL - List movies\nA - Add new movies\nW - Watch movies\nQ - Quit")

        enter = input(">>> ").upper()
        if enter == "L":
            List(movies)
        elif enter == "A":
            Add(movies)
        elif enter == "W":
            if all_watched:
                print("You have watched all movies")
            else:
                Watch(movies)
        elif enter == "Q":
            print("{} movies saved to movies.csv\nHave a nice day :)".format(len(movies)))
            return False
        else:
            print("Invalid choice")
            print("Menu:\nL - List movies\nA - Add new movies\nW - Watch movies\nQ - Quit")
            enter = input(">>> ").upper()
        input_file.close()


# display the movies list
def List(movies):
    index = 1
    num_of_watched = 0
    num_of_unwatched = 0
    for movie in movies:
        elements = movie.split(",")
        print(index, end=".")
        if "u" in elements[3]:
            num_of_unwatched += 1
            print("* ", end=".")
        elif "w" in elements[3]:
            num_of_watched += 1
            print("  ", end=".")
        print(elements[0], end=algin(movies, elements[0]))
        print(" - {0} ({1})".format(elements[1], elements[2]))
        index += 1
        print('{0} movies watched, {1} movies still to watch'.format(num_of_watched, num_of_unwatched))


def algin(movies, name_of_movie):
    max_length = 0
    space = ''
    for movie in movies:
        elements = movie.split(",")
        for element in elements:
            if max_length < len(element):
                max_length = len(element)
            else:
                continue
    for i in range(max_length - len(name_of_movie)):
        space += " "
    return space


# add the new movie
def Add(movies):
    title = input("Title: ")
    while title == "":
        print("Input can not be blank")
        title = input("Title: ")
    year = int(input("Year: "))
    while year < 0:
        print("Number must be >= 0")
        year = int(input("Year: "))
    category = input("Category: ")
    while category == "":
        print("Input can not be blank")
        category = input("Category: ")
    added_movie = ("{}, {}, {}, u".format(title, year, category))
    movies.append(added_movie)
    print("{}({} from {}) added to movie list".format(title, category, year))


# mark the movie that already watched
def Watch(movies):
    global elements
    while True:
        try:
            enter_movie_num = int(input("Enter the number of a movie to mark as watched\n>>> "))
            if enter_movie_num not in range(1, len(movies) + 1):
                KeyError()
            elements = movies[enter_movie_num - 1].split(",")
            if "u" in elements[3]:
                elements[3] = elements[3].replace("u", "w")
                movies[enter_movie_num - 1] = ",".join(elements)
                print("{} watched".format(elements[0]))
            else:
                Exception()
        except KeyError:
            print("Invalid movie number")
        except ValueError:
            print("Invalid input; enter a valid number")
        except Exception:
            print("You have already watched {}".format(elements[0]))


# check if all the movies are watched
def all_watched(movies):
    check_all_watched = True
    count = 0
    for movie in movies:
        elements = movie.split(",")
        if "u" in elements[3]:
            count += 1
    if count > 0:
        check_all_watched = False
    else:
        pass
    return check_all_watched


main()
