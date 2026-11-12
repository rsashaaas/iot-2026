class Clip:
    def __init__(self, artist="", song="", duration=0, views=0):
        self.__artist = artist
        self.__song = song
        self.__duration = duration
        self.__views = views
        self.name = song
        self.number = views

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_song(self):
        return self.__song

    def set_song(self, song):
        self.__song = song
        self.name = song

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_views(self):
        return self.__views

    def set_views(self, views):
        self.__views = views
        self.number = views

    def __str__(self):
        return ( f"Artist: {self.__artist}, Song: {self.__song}, Duration: {self.__duration} sec, Views: {self.__views}, Name: {self.name}, Number: {self.number}")

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        print("Music video deleting")


def main():
    clip1 = Clip("Lana Del Rey", "Dealer", 275, 63000000)
    clip2 = Clip("Yung Lean", "Kyoto", 270, 76000000)
    clip3 = Clip("Charli XCX", "Club classics", 154, 16000000)

    print(clip1)
    print(clip2)
    print(clip3)


if __name__ == "__main__":
    main()