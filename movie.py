"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """Movie Class"""
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched
        
    def __str__(self):
        watched = 'w' if self.is_watched else 'u'
        msg = f"{self.title},{self.category},{self.year},{watched}"
        return msg
    
    def mark_watched(self):
        self.is_watched = True
        
    def mark_unwatched(self):
        self.is_watched = False
