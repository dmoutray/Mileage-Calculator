import webapp.database.dbconnect as dbconnect

class CalculatorDAO():
    def __init__(self):
        self.dbconfig = dbconnect.DBConfig()
        self.connection = self.dbconfig.connection
        calculator_dao = CalculatorDAO()
        connection = calculator_dao.connection

    def get_vehicle_id_by_name(self, vehicle_name):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT vehicle_id FROM vehicles WHERE model = %s"
                cursor.execute(sql, (vehicle_name))
                result = cursor.fetchone()
                print vehicle_name, "vehicle ID is ", result['vehicle_id']
        except Exception as e:
            print(e)

    def get_vehicle_name_by_id(self, vehicle_id):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT make, model FROM vehicles WHERE vehicle_id = %s"
                cursor.execute(sql, (vehicle_id))
                result = cursor.fetchone()
                print "Car with ID of", vehicle_id, "is a " + result['make'], result['model']
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
        finally:
            self.connection.close()

    def get_vehicle_list(self):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "SELECT make, model, year_of_manufacture FROM vehicles"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            self.connection.close()
