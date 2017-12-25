import cherrypy
import pymysql.cursors
import webapp.database.dbconnect
import webapp.database.calculatorDAO
from jinja2 import Environment, FileSystemLoader
from webapp.web.calculator import Calculator
from webapp.web.register import Register

class MPGCalculator(object):

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.calculator = Calculator()
        self.register = Register()
        self.calculator_dao = webapp.database.calculatorDAO.CalculatorDAO()
        self.connection = webapp.database.dbconnect.DBConfig.connection

    @cherrypy.expose
    def index(self, **kwargs):
        tmpl = self.env.get_template('index.html')
        if kwargs:
            if kwargs.get("fuel_quantity") != "" and kwargs.get("miles_driven") != "":
                fuel_quantity = kwargs.get("fuel_quantity")
                miles_driven = kwargs.get("fuel_quantity")
                mpg = self.calculator.calculate_mpg(fuel_quantity, miles_driven)
                return tmpl.render(mpg = mpg)

            return tmpl.render(mpg = "please enter an MPG")
        else:
            return tmpl.render(result = "")

    @cherrypy.expose
    def database(self):
        tmpl = self.env.get_template('database.html')
        vehicle_name = self.calculator_dao.get_vehicle_id_by_name("Celica")
        return tmpl.render(vehicle_name = vehicle_name)

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
