import webapp.database.dbconnect as dbconnect

class UserDAO():

    def __init__(self):
        self.dbconfig = dbconnect.DBConfig()
        self.connection = self.dbconfig.connection

    def create_new_user(self, user_details):

        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
                firstname = user_details['firstname']
                lastname = user_details['lastname']
                email = user_details['email']
                password = user_details['password']
                cursor.execute(sql, (firstname, lastname, email, password))
                self.connection.commit()
        except Exception as e:
            print(e)

    def get_userid_by_email(self, email):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "SELECT user_id  FROM users WHERE email = %s"
                cursor.execute(sql, (email))
                result = cursor.fetchone()
                return result['user_id']
        except Exception as e:
            print(e)


