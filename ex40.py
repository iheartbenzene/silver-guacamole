"""
1. Classes are like blueprints or definitions for creating mini modules.
2. Instantiation is how you make one of these mini-modules and import it at the same time.
    'Instantiate' just means to create an object from the class.
3. The resulting created mini-module is called an object, and then you assign
    it to a cariable to work with it.
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around this family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
