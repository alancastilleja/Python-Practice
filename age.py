

class Person:
    def __init__(self, initialAge):
        self.age = initialAge
        print(self.age)
    def ageCheck(self):
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager")
        else:
            print("You are old")
    def yearPasses(self):
            self.age += 1
            print(self.age)

def main():
    new = Person(10)
    new.ageCheck()
    new.yearPasses()
    new.ageCheck()
if __name__ == '__main__':
    main()