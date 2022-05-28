class Student:
    # [assignment] Skeleton class. Add your code here
    tracks = []
    def __init__(self, name, age, t1, t2, t3 , score):
        self.name = name
        self.age = int(age)
        self.tracks.append(t1)
        self.tracks.append(t2)
        self.tracks.append(t3)
        self.score = float(score)

#    methods
    def change_name(self, name):
        self.name= name
        print("this is the change function", self.name)

    def change_age(self, age):
        self.age= age
        print("this is the change function", self.age)

    def add_track(self, track):
        self.track = track
        print("this is the change function", self.track)

    def get_score(self, score):
        self.score = score
        print("this is the change function", self.score)

Bob = Student(name="Bob", age=26, tracks="FE","BE",score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(30))
