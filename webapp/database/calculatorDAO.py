import webapp.database.dbconnect as dbconnect

class CalculatorDAO():
    def __init__(self):
        self.dbconfig = dbconnect.DBConfig()
        self.connection = self.dbconfig.connection

    def get_average_mpg_by_vehicle_id(self, vehicle_id):
        try:
            with self.connection.cursor() as cursor:
                # Write a single record
                sql = "SELECT AVG(mileage) FROM records WHERE vehicle_id = %s"
                cursor.execute(sql, (vehicle_id))
                result = cursor.fetchone()
                return result['AVG(mileage)']

        except Exception as e:
            print e

