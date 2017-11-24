
class Movie:

    def __init__(self,title,story,trailer,poster):
        self.title = title
        self.story_line = story
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster

    def  show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

