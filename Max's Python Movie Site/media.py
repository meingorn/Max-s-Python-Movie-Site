import webbrowser #making sure code runs through the web

#a function that will re-run for all of my favorite movies
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#a function that will show the trailer for the movies
def show_trailer(self):
    webbroswer.open(self.trailer_youtube_url)
