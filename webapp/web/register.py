from webapp.database.dbconnect import DBConfig
import cherrypy

class Register():

    def register(self, **kwargs):
        firstname = kwargs.get('firstname')
        surname = kwargs.get('surname')
        email = kwargs.get('email')
        password = kwargs.get('password')
        self.db.users.insert(
            {'firstname': firstname,
             'surname': surname,
             'email':email,
             'password': password
             }
        )

