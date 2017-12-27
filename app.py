# import other classes and libraries
import cherrypy
import webapp.database.calculatorDAO
import webapp.database.vehiclesDAO
import webapp.database.userDAO
from jinja2 import Environment, FileSystemLoader
from webapp.web.calculator import Calculator

# Create main module
class MPGCalculator(object):

    # initialise objects and variables needed for the app
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.calculator = Calculator()
        self.calculator_dao = webapp.database.calculatorDAO.CalculatorDAO()
        self.user_dao = webapp.database.userDAO.UserDAO()
        self.vehicle_dao = webapp.database.vehiclesDAO.VehiclesDAO()

    # define the method which runs when the user requests the home page
    # kwargs are keyword arguments such as "name = David"
    @cherrypy.expose
    def index(self, **kwargs):
        # set the html template
        tmpl = self.env.get_template('index.html')
        notification_string = ""
        # check if a user has passed any keyword arguments to the homepage
        if kwargs:
            # check for empty keyword arguments
            if kwargs.get("fuel_quantity") != "" and kwargs.get("miles_driven") != "":
                # initialise result dictionary - this is like a key:value array
                result = {}
                # kwargs.get retrieves the value assocatiated with a given key
                registration = kwargs.get("registration")
                fuel_quantity = kwargs.get("fuel_quantity")
                miles_driven = kwargs.get("miles_driven")
                result['calculated_mpg'] = self.calculator.calculate_mpg(fuel_quantity, miles_driven)
                vehicle_id = self.vehicle_dao.get_vehicle_id_by_registration(registration)
                # check for empty vehicle ID
                if vehicle_id:
                    self.vehicle_dao.insert_record(registration,result['calculated_mpg'])
                    result['average_mpg'] = self.calculator_dao.get_average_mpg_by_vehicle_id(vehicle_id)
                    result['historic_mpg'] = self.vehicle_dao.get_all_mpgs_by_vehicle_id(vehicle_id)
                    vehicle_name = self.vehicle_dao.get_vehicle_name_by_id(vehicle_id)
                    notification_string = "You are currently viewing records for " + registration + " (" + vehicle_name + ")"
                    # tmpl.render tells the system which html file to use and injects variables into it
                    return tmpl.render(result=result, notification = notification_string)
                else:
                    notification_string = "No car found with that registration"
                    return tmpl.render(result = "", notification = notification_string)
            notification_string = "Please fill in all fields"
            return tmpl.render(result = "", notification = notification_string)
        else:
            return tmpl.render(result = "")

    # Not yet used
    @cherrypy.expose
    def login(self, **kwargs):
        tmpl = self.env.get_template('login.html')
        return tmpl.render()

    # Registers a new user on the database
    @cherrypy.expose
    def register(self, **kwargs):
        if kwargs:
           self.user_dao.create_new_user(kwargs)
           raise cherrypy.HTTPRedirect('/')
        else:
            tmpl = self.env.get_template('register.html')
            return tmpl.render()

    @cherrypy.expose
    def add_vehicle(self, **kwargs):
        if kwargs:
            self.vehicle_dao.add_vehicle(kwargs)
            self.vehicle_dao.claim_ownership_of_vehicle(kwargs)
            raise cherrypy.HTTPRedirect('/')
        else:
            tmpl = self.env.get_template('add_vehicle.html')
            return tmpl.render()


    index.exposed = True

# Tells the python web server to start and gives it a config file
cherrypy.quickstart(MPGCalculator(), '/', "server.conf")
