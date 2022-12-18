import datetime

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        #Extract 1st and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
    def age(self):
        """Return the age of user in years"""
        today = datetime.date(2022, 5, 14)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("Dave Bowman", "19990102")

print(user.age())



'''
class User:
    pass

us1 = User()
us1.first = "Jim"
us1.sec = "Jones"
us2 = User()
us2.first = "Dave"
us2.sec = "Smith"

print(us1.first)
'''