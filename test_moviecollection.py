"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)
    # TODO: Add more sorting tests
    print("Test sorting - category:")
    movie_collection.sort("category")
    print(movie_collection)
    
    print("Test sorting - is_watched:")
    movie_collection.sort("is_watched")
    print(movie_collection)
    # TODO: Test saving movies (check CSV file manually to see results)
    print("Test saving movies:")
    movie_collection.save_movies('movies_new.csv')
    
    # TODO: Add more tests, as appropriate, for each method
    print("Test get number of watched movies")
    num = movie_collection.get_num_watched()
    assert num == 2
    
    print("Test get number of unwatched movies")
    num = movie_collection.get_num_unwatched()
    assert num == 4
        

run_tests()
