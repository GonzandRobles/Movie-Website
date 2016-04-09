import webbrowser

class Video ():
    """ This fuction is the parent, and it is going to allow class Movie to inheret the parameters of director and screenwriter"""
    def __init__(self, director, screenwriter):
        self.director = director
        self.screenwriter = screenwriter
    
class Movie(Video):
    """This class provides a way to store movie related information."""
    def __init__(self, director, screenwriter, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, director, screenwriter)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer (self):
        """This function opens the web browser and shows the youtube trailer of the movie."""
        webbrowser.open (self.trailer_youtube_url)


    


