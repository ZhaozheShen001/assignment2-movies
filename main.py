"""
Name: Shen Zhaozhe
Date:23/01/2021
GitHub URL:https://github.com/JCUS-CP1404/assignment-2---movies-2-ZhaozheShen001
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
from movie import Movie
from moviecollection import MovieCollection

KEYS = ['year', 'category', 'title', 'is_watched']
CATEGORIES = ['Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller']


class MoviesToWatchApp(App):
    """..."""
    status_text = StringProperty()
    head_right = StringProperty()
    state_codes = ListProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        # self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies('movies.csv')

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies To Watch 2.0"
        self.head_left = "Sort by:"
        self.head_right = f"To watch: {self.movie_collection.get_num_unwatched()}. Watched: {self.movie_collection.get_num_watched()}"
        self.content_add = "Add new movie"
        self.content_title = "Title: "
        self.content_category = "Category: "
        self.content_year = "Year: "
        self.state_codes = KEYS
        self.key = self.state_codes[0]
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        self.movie_collection.sort(self.key)
        for movie in self.movie_collection.movies:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            watched = "watched" if movie.is_watched else ""
            name = f"{movie.title} ({movie.category} from {movie.year}) {watched}"
            temp_button = Button(text=name)
            temp_button.background_color = (0, 1, 0, 1) if watched == "watched" else (1, 0, 0, 1)
            temp_button.bind(on_release=self.press_entry)
            temp_button.movie = movie
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)
        self.head_right = f"To watch: {self.movie_collection.get_num_unwatched()}. Watched: {self.movie_collection.get_num_watched()}"

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked
        """
        # get name (dictionary key) from the id of Button we clicked on
        movie = instance.movie
        # update status text
        watched = movie.is_watched
        if watched:
            movie.mark_unwatched()
            instance.text = f"{movie.title} ({movie.category} from {movie.year})"
            instance.background_color = (1, 0, 0, 1)
            self.status_text = f"You have not watched {movie.title}"
        else:
            movie.mark_watched()
            instance.text = f"{movie.title} ({movie.category} from {movie.year}) watched"
            instance.background_color = (0, 1, 0, 1)
            self.status_text = f"You have watched {movie.title}"
        self.head_right = f"To watch: {self.movie_collection.get_num_unwatched()}. Watched: {self.movie_collection.get_num_watched()}"

    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()

    def change_state(self, state_code):
        """ handle change of spinner selection, output result to label widget """
        self.key = state_code
        self.clear_all()
        self.create_widgets()

    def press_add(self, added_title, added_category, added_year):
        """
        Handler for pressing the add button
        :return: None
        """
        if added_title and added_category and added_year:
            if added_year.isdigit():
                if added_category in CATEGORIES:
                    self.movie_collection.add_movie(Movie(added_title, int(added_year), added_category))
                    self.clear_all()
                    self.create_widgets()
                else:
                    self.status_text = "The category must be one of the following: Action, Comedy, Documentary, " \
                                       "Drama, Fantasy, Thriller "
            else:
                self.status_text = "Please enter a valid number"
        else:
            self.status_text = "All fields must be completed"

    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        If we don't do this, the popup will still have text in it when opened again
        :return: None
        """
        self.root.ids.added_title.text = ""
        self.root.ids.added_category.text = ""
        self.root.ids.added_year.text = ""


if __name__ == '__main__':
    MoviesToWatchApp().run()
