"""
this module contains the movie class that will be used in the
entertain.py file
"""
class movie():                                                              #class movie
    def __init__(self,titlemovie,story,poster,trailer):                     #init is a constructor
        self.title=titlemovie
        self.storyline=story
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer
    
