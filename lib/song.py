class Song:
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_count()
        Song.add_song_artist(self, self.artist)
        Song.add_song_genre(self, self.genre)
        Song.add_to_artist_count(self, self.artist)
        Song.add_to_genre_count(self, self.genre)

    @classmethod
    def add_to_count(cls):
        cls.count += 1

    def add_song_artist(cls, artist):
        cls.artists.append(artist)

    def add_song_genre(cls,genre):
        cls.genres.append(genre)

    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] = cls.artist_count[artist] + 1
        else: 
            cls.artist_count[artist] = 1
    
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] = cls.genre_count[genre] + 1
        else: 
            cls.genre_count[genre] = 1
