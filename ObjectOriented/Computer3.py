class Computer:

    def __init__(self, processor, ram):
        self.process = processor
        self.ram1 = ram

    def config(self):
        print(self.process, self.ram1)


com1 = Computer("i5", 16)
com2 = Computer("i7", 8)

com1.config()
com2.config()