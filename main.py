"Simple musical Python program"

import locale


class Music:
    def __init__(self, id, name, composer):
        self._id = id
        self._name = name
        self._composer = composer

        @property
        def id(self):
            return self._id
        @id.setter
        def id(self, id):
            self._id = id

        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, name):
            self._name = name

        @property
        def composer(self):
            return self._composer
        @composer.setter
        def composer(self, composer):
            self._composer = composer

def main():

    locale.setlocale(locale.LC_ALL, 'US')

    songs = []


    while True:


        id = int(input("Enter id song or -1 to end:"))

        if id == -1:
            break

        name = input("Enter name song:")

        composer = input("Enter composer of this song:")

        music = Music(id, name, composer)

        songs.append(music)


    for song in songs:

        print(f"Id: {song._id}\nName: {song._name}\nComposer: {song._composer}\n")

if __name__:
    main()


