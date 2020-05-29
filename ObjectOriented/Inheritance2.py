class Music:

    def classical(self):
        print("Classical music is the Pride of India")


class Composer(Music):

    def comp(self):
        print("Composer creates Music")


class Singer(Composer):

    def sing(self):
        print("Singer sings song")


S = Singer()
S.classical()
S.comp()
S.sing()