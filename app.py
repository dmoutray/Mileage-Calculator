import cherrypy
import webapp.database.calculatorDAO
import webapp.database.vehiclesDAO
from jinja2 import Environment, FileSystemLoader
from webapp.web.calculator import Calculator

class MPGCalculator(object):

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.calculator = Calculator()
        self.calculator_dao = webapp.database.calculatorDAO.CalculatorDAO()
        self.vehicle_dao = webapp.database.vehiclesDAO.VehiclesDAO()

    @cherrypy.expose
    def index(self, **kwargs):
        tmpl = self.env.get_template('index.html')
        if kwargs:
            if kwargs.get("fuel_quantity") != "" and kwargs.get("miles_driven") != "":
                result = {}
                fuel_quantity = kwargs.get("fuel_quantity")
                miles_driven = kwargs.get("miles_driven")
                result['calculated_mpg'] = self.calculator.calculate_mpg(fuel_quantity, miles_driven)
                vehicle_id = self.vehicle_dao.get_vehicle_id_by_registration(kwargs.get("registration"))
                if vehicle_id:
                    result['average_mpg'] = self.calculator_dao.get_average_mpg_by_vehicle_id(vehicle_id)
                    result['historic_mpg'] = self.vehicle_dao.get_all_mpgs_by_vehicle_id(vehicle_id)
                    return tmpl.render(result=result)
                else:
                    return tmpl.render(result = "", notification = "No car found with that registration")
            return tmpl.render(result = "", notification = "Please fill in all fields")
        else:
            return tmpl.render(result = "")

    @cherrypy.expose
    def database(self):
        tmpl = self.env.get_template('database.html')
        result = self.calculator_dao.get_all_mpgs_by_vehicle_id(1)
        return tmpl.render(result = result)

    @cherrypy.expose
    def login(self, **kwargs):
        tmpl = self.env.get_template('login.html')
        return tmpl.render()

    @cherrypy.expose
    def register(self, **kwargs):
        if kwargs:
           self.register.register(**kwargs)
           raise cherrypy.HTTPRedirect('/')
        else:
            tmpl = self.env.get_template('register.html')
            return tmpl.render()


    index.exposed = True

cherrypy.quickstart(MPGCalculator(), '/', "server.conf")
