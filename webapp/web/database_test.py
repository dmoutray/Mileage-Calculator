from webapp.database.calculatorDAO import CalculatorDAO

calculator_dao = CalculatorDAO()
connection = calculator_dao.connection

def get_vehicle_id_by_name(vehicle_name):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT vehicle_id FROM vehicles WHERE model = %s"
            cursor.execute(sql, (vehicle_name))
            result = cursor.fetchone()
            print vehicle_name, "vehicle ID is ", result['vehicle_id']
    except Exception as e:
        print(e)

def get_vehicle_name_by_id(vehicle_id):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT make, model FROM vehicles WHERE vehicle_id = %s"
            cursor.execute(sql, (vehicle_id))
            result = cursor.fetchone()
            print "Car with ID of", vehicle_id, "is a " + result['make'], result['model']
    except Exception as e:
        print(e)

def get_vehicle_id_by_registration(registration):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT make, model FROM vehicles JOIN vehicle_owners using(vehicle_id) WHERE registration = %s"
            cursor.execute(sql, (registration))
            result = cursor.fetchone()
            print "Car with registration of", registration, "is a " + result['make'], result['model']
    except Exception as e:
        print(e)

def get_vehicle_owner_by_registration(registration):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT user_id FROM vehicle_owners WHERE registration = %s"
            cursor.execute(sql, (registration))
            result = cursor.fetchone()
            return result['user_id']
    except Exception as e:
        print(e)

def get_vehicle_id_by_registration(registration):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT vehicle_id FROM vehicle_owners WHERE registration = %s"
            cursor.execute(sql, (registration))
            result = cursor.fetchone()
            return result['vehicle_id']
    except Exception as e:
        print(e)

def get_vehicle_owner_id_by_registration(registration):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT user_id FROM vehicle_owners WHERE registration = %s"
            cursor.execute(sql, (registration))
            result = cursor.fetchone()
            return result['user_id']
    except Exception as e:
        print(e)

def insert_record(registration, mileage):
    try:
        with connection.cursor() as cursor:
            # Write a single record
            user_id = get_vehicle_owner_id_by_registration(registration)
            vehicle_id = get_vehicle_id_by_registration(registration)
            sql = "INSERT INTO records (user_id, vehicle_id, mileage) VALUES (%s, %s, %s)"
            cursor.execute(sql,(user_id, vehicle_id, mileage))
            connection.commit()
    finally:
        connection.close()

def get_vehicle_list():
    try:
        with connection.cursor() as cursor:
            # Write a single record
            sql = "SELECT make, model, year_of_manufacture FROM vehicles"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

get_vehicle_id_by_name('Celica')
get_vehicle_name_by_id(2)
print get_vehicle_id_by_registration("AFZ6652")
print get_vehicle_owner_id_by_registration("SUI5998")
get_vehicle_list()
insert_record("AFZ6652", 32.5)