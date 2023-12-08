class Human:
    # built-in
    # constructor
    # initialize
    def __init__(self, name):
        self.name = name
        print("bir human instance'i üretildi")
    def __str__(self):
        return f"str fonksiyoundan dönen değer : {self.name}"
    def talk(self, sentence):
        name = "ercan"
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")