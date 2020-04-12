class Name:
    person_type = 'teenager'
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        print(self.name)
        print(self.age)

    def checkName(self):
        if sum(c.isalpha() for c in self.name) < 4:
            if any(i.isdigit() for i in self.name):
                return ValueError('Your name has a number in it')
            return f'your name is too short'
        else:
            return f'your name is fine'

    def checkAge(self):
        if self.age < 13:
            return f'you are too young'
        elif self.age < 0:
            self.age = 0
            return f'You set an age less than 0. Setting age to zero.'
        else:
            return f'You are fine'


def main():
    person_name = str(input('What is your name: '))
    person_age = int(input('What is your age: '))
    person = Name(person_name, person_age)
    print(person.checkName())
    print(person.checkAge())
    print(person.person_type)

if __name__ == '__main__':
    main()