class Song:
    def __init__(self,title,author,lyrics):
        self.title = title
        self.author=author
        self.lyrics=lyrics

    def __str__(self):
        return f"New Song {self.title} made  by {self.author}"

NewSong = Song('shdjkf','sdkd','sdnms')


print(NewSong)

