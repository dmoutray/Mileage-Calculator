import webapp.database.dbconnect as dbconnect

class CalculatorDAO():
    def __init__(self):
        self.dbconfig = dbconnect.DBConfig()
        self.connection = self.dbconfig.connection

    def insert_record(self, user_id, vehicle_id, mileage):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "INSERT INTO records (user_id, vehicle_id, mileage) VALUES (%d, %d, %d)"
                cursor.execute(sql,(user_id, vehicle_id, mileage))
        finally:
            self.connection.close()

    def get_vehicle_id_by_name(self, vehicle_name):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT vehicle_id FROM vehicles WHERE model = %s"
                cursor.execute(sql,(vehicle_name))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)

    def get_vehicle_id_by_registration(self, registration):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT vehicle_id FROM users WHERE registration = %s"
                cursor.execute(sql, (registration))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)

