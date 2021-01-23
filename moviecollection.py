"""..."""


# TODO: Create your MovieCollection class in this file
from movie import Movie

class MovieCollection:
    """Movie Collection Class"""
    def __init__(self, movies=[]):
        self.movies = movies
    
    def __str__(self):
        msg = [str(movie) for movie in self.movies]
        return '\n'.join(msg)
    
    def add_movie(self, movie):
        """add a single Movie object to the movies attribute"""
        self.movies.append(movie)
        
    def get_num_unwatched(self):
        """get number of unwatched movies"""
        num = 0
        for movie in self.movies:
            if not movie.is_watched:
                num += 1
        return num
    
    def get_num_watched(self):
        """get number of watched movies"""
        num = 0
        for movie in self.movies:
            if movie.is_watched:
                num += 1
        return num
    
    def load_movies(self, file):
        """load movies (from csv file into Movie objects in the list)"""
        with open(file ,'r') as f:
            for line in f.readlines():
                data = line.strip().split(',')
                title, year, category = data[0], int(data[1]), data[2]
                is_watched = True if data[3] == 'w' else False
                movie = Movie(title, year, category, is_watched)
                self.add_movie(movie)
    
    def save_movies(self, file):
        """save movies (from movie list into csv file)"""
        with open(file ,'w') as f:
            for movie in self.movies:
                f.write(str(movie)+'\n')
    
    def sort(self, key):
        """sort (by the key passed in, then by title)"""
        if key == 'title':
            self.movies.sort(key=lambda x: x.title)
        elif key == 'year':
            self.movies.sort(key=lambda x: [x.year, x.title])
        elif key == 'category':
            self.movies.sort(key=lambda x: [x.category, x.title])
        elif key == 'is_watched':
            self.movies.sort(key=lambda x: [x.is_watched, x.title])
            