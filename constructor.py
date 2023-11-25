class Person:
    def __init__(self, name, occupation):
        # print("Automatically called")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}.")


a = Person("Ram", "Developer")
b = Person("Hari", "Businessman")
a.info()
b.info()
