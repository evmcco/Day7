class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0
        self.greeted_people = []
        self.unique_greeting_count = 0

    def greet(self, other_person): 
        self.greeting_count += 1
        if other_person.name not in self.greeted_people:
            self.greeted_people.append(other_person.name)
            self.unique_greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("%s\'s email address is %s and %s\'s phone number is %s" % (self.name, self.email, self.name, self.phone))
    
    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        print(len(self.friends))
        # return len(self.friends)

    def __str__(self):
        return 'Name: {} | Email: {} | Phone: {}'.format(self.name, self.email, self.phone)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
evan = Person('Evan', 'evan@gmail.com', '234-456-1545')


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_vehicle(self):
        print(self.make, self.model, self.year)

vw_gti = Vehicle('VW', 'GTI', 2017)
# vw_gti.print_vehicle()
