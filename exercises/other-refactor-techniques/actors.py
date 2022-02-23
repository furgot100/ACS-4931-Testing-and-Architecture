# by Kami Bigdely
# Extract class
from errno import EMSGSIZE


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


class Actor: 
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self, email):
        print("email sent to: ", email)

    def birth_year(self):
        if self.birth_year > 1985:
            print(self.first_names, self.last_names)
            print('Movies Played: ', end='')
            for m in movies[i]:
                print(m, end=', ')
            print()
            self.send_hiring_email(self.email))
