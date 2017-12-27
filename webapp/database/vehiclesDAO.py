import webapp.database.dbconnect as dbconnect
import webapp.database.userDAO as userDAO

class VehiclesDAO():

    def __init__(self):
        self.dbconfig = dbconnect.DBConfig()
        self.connection = self.dbconfig.connection
        self.user_dao = userDAO.UserDAO()

    def get_vehicle_id_by_name(self, vehicle_name):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT vehicle_id FROM vehicles WHERE model = %s"
                cursor.execute(sql, (vehicle_name))
                result = cursor.fetchone()
                return result['vehicle_id']
        except Exception as e:
            print(e)

    def get_vehicle_name_by_id(self, vehicle_id):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT year_of_manufacture, make, model FROM vehicles WHERE vehicle_id = %s"
                cursor.execute(sql, (vehicle_id))
                result = cursor.fetchone()
                year_of_manufacture = str(result['year_of_manufacture'])
                make = result['make']
                model = result['model']
                result_string = year_of_manufacture + " " + make + " " + model
                return result_string
        except Exception as e:
            print(e)

    def get_vehicle_id_by_registration(self, registration):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT make, model FROM vehicles JOIN vehicle_owners using(vehicle_id) WHERE registration = %s"
                cursor.execute(sql, (registration))
                result = cursor.fetchone()
                print "Car with registration of", registration, "is a " + result['make'], result['model']
        except Exception as e:
            print(e)

    def get_vehicle_owner_by_registration(self, registration):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT user_id FROM vehicle_owners WHERE registration = %s"
                cursor.execute(sql, (registration))
                result = cursor.fetchone()
                return result['user_id']
        except Exception as e:
            print(e)

    def get_vehicle_id_by_registration(self, registration):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT vehicle_id FROM vehicle_owners WHERE registration = %s"
                cursor.execute(sql, (registration))
                result = cursor.fetchone()
                return result['vehicle_id']
        except Exception as e:
            print(e)

    def get_vehicle_owner_id_by_registration(self, registration):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT user_id FROM vehicle_owners WHERE registration = %s"
                cursor.execute(sql, (registration))
                result = cursor.fetchone()
                return result['user_id']
        except Exception as e:
            print(e)

    def insert_record(self, registration, mileage):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                user_id = self.get_vehicle_owner_id_by_registration(registration)
                vehicle_id = self.get_vehicle_id_by_registration(registration)
                sql = "INSERT INTO records (user_id, vehicle_id, mileage) VALUES (%s, %s, %s)"
                cursor.execute(sql,(user_id, vehicle_id, mileage))
                self.connection.commit()
        except Exception as e:
            print(e)

    def get_vehicle_list(self):
        try:
            with self.connection as cursor:
                # Read multiple records
                sql = "SELECT make, model, year_of_manufacture FROM vehicles"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def get_all_mpgs_by_vehicle_id(self, vehicle_id):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "SELECT mileage FROM records WHERE vehicle_id = %s"
                cursor.execute(sql, (vehicle_id))
                result = cursor.fetchall()
                return result
        except Exception as e:
            print e

    def add_vehicle(self, vehicle_details):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "INSERT INTO vehicles (make, model, year_of_manufacture, fuel) VALUES (%s, %s, %s, %s)"
                make = vehicle_details['make']
                model = vehicle_details['model']
                year_of_manufacture = vehicle_details['year_of_manufacture']
                fuel_type = vehicle_details['fuel_type']
                cursor.execute(sql, (make, model, year_of_manufacture, fuel_type))
                self.connection.commit()
        except Exception as e:
            print(e)

    def get_last_vehicle_added(self):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "SELECT MAX(vehicle_id) FROM vehicles"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['MAX(vehicle_id)']
        except Exception as e:
            print(e)

    def claim_ownership_of_vehicle(self, owner_details):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "INSERT INTO vehicle_owners (user_id, vehicle_id, registration) VALUES (%s, %s, %s)"
                email = owner_details['email']
                user_id = self.user_dao.get_userid_by_email(email)
                registration = owner_details['registration']
                vehicle_id = self.get_last_vehicle_added()
                cursor.execute(sql, (user_id, vehicle_id, registration))
                self.connection.commit()
        except Exception as e:
            print(e)



