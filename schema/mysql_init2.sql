DROP TABLE IF EXISTS vehicle_owners;
DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS vehicles;

CREATE TABLE vehicles(
vehicle_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
make VARCHAR(30) NOT NULL,
model VARCHAR(30) NOT NULL,
year_of_manufacture INT(4) NOT NULL,
fuel VARCHAR(10) NOT NULL
);

CREATE TABLE users(
user_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(30) NOT NULL,
password VARCHAR(30) NOT NULL
);

CREATE TABLE records(
record_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
user_id INT(10),
vehicle_id INT(10),
mileage DECIMAL(6,2) DEFAULT 0.00,
FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE vehicle_owners(
registration VARCHAR(7) PRIMARY KEY,
user_id INT(10),
vehicle_id INT(10),
FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT into users (firstname,lastname,email,password) VALUES
("David","Jason","djason@example.co.uk","pass1234"),
("John","Gardner","j-gardner@example.gov.uk","pass4321"),
("Helen","Anderson","handerson2003@live.com","pass5678");

INSERT into vehicles (make,model,year_of_manufacture,fuel) VALUES
 ("Toyota","Celica","2005","petrol"),
 ("Nissan","Skyline","2014","petrol"),
 ("Land Rover","Evoque","2015","petrol");

INSERT INTO vehicle_owners (registration,user_id, vehicle_id) VALUES
("GFZ2003",1,1),
("XFZ6128",2,2),
("FEZ5998",3,3);

INSERT into records (user_id, vehicle_id, mileage) VALUES (1,1,34.20);
