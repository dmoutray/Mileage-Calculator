from webapp.database.dbconnect import DBConfig

class Calculator():

    def calculate_mpg(self, fuel_quantity, miles_driven):
        fuel_quantity = float(fuel_quantity)
        miles_driven = float(miles_driven)
        mpg = (miles_driven / fuel_quantity) * 4.54
        return mpg

    def calculate_average_mpg(self, **kwargs):
        car = kwargs.get("car")
        total_mpg = 0
        count = 0
        for result in self.db.testing.find({'car': car}):
            total_mpg += result['mpg']
            count += 1
        return (total_mpg / count)

    def display_historic_mpg(self, **kwargs):
        car = kwargs.get("car")
        historic_mpg = []
        for result in self.db.testing.find({'car': car}):
            historic_mpg.append(result)
        return (historic_mpg)
