
class Calculator():

    def calculate_mpg(self, fuel_quantity, miles_driven):
        fuel_quantity = float(fuel_quantity)
        miles_driven = float(miles_driven)
        mpg = (miles_driven / fuel_quantity) * 4.54
        return mpg

