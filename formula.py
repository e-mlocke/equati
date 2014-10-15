from sympy import *
from math import ceil
import dimcon

class Formula(object):
    # number of instances of the Equation class
    no_inst = 0
    # dimcon.dimcon_dict items convert keys to base units when multiplied
    in_dict = {}
    def __init__(self, equation, eq_dict):
        self.equation = equation
        self.eq_dict = eq_dict
        #for key in self.eq_dict:
        #    self.eq_dict[key][0] = symbols(str(self.eq_dict[key][0]))
        #    print('i made a symbol')
        Formula.no_inst = Formula.no_inst + 1

    @classmethod
    def get_no_equations(cls):
        # number of instances of the Equation class
        return cls.no_inst

    @staticmethod
    def round_to_thousandth(num):
        num = ceil(num*1000)/1000
        return num

    def check_dimcon(self, key):
        # pass a key to to method and it checks the dimcon.dimcon_dict to see if it exists
        # a class method?
        pass

    def clear_inputs(self):
        # makes in_dict = {}
        self.in_dict = {}
        return self.in_dict

    def input_vars(self, get):
        # input all known_data but data for get
        # prompts user the keys of eq_dict
        # user inputs go in as in_dict
        get = str(get)
        for key in self.eq_dict:
            if key is not get:
                known_val = float(input("Value of {}: ".format(key)))
                known_units = input("Units of {}: ".format(key))
                known_data = [known_val, known_units]
                self.in_dict[key]= known_data
        return self.in_dict

    def get_vars(self, get):
        # retreives info for all vars except the get var
        # builds in_dict like input_vars
        # use on a website
        pass

    def dimcon(self):
        # all units made dimensionally consistent
        # checks if unit is in dimcon.dimcon_dict. if not prints "Conversion not Stored"
        # compares in_dict[key][0] to dimcon.dimcon_dict[key]
        for key in self.in_dict:
            if self.in_dict[key][1] in dimcon.dimconlib:
                self.in_dict[key][0] = self.in_dict[key][0]*dimcon.dimconlib[self.in_dict[key][1]]
                self.in_dict[key][1] = self.eq_dict[key][1]
            else:
                print('Conversion not stored')
        return self.in_dict

    def solvefor(self, get, get_units):
        # substitute in_dict values. converts to desired dimensions
        # make get_units a str (to use on a website make get & _units attached
        # to dropdown tabs that show only keys stored in dimcon.dimcon_dict)
        # clear_inputs --> input_vars --> dimcon --> arrange
        if get_units not in dimcon.dimconlib:
            print('Equati does not currently support the dimension: {}'.format(get_units))
        else:
            self.clear_inputs()
            self.input_vars(get)
            self.dimcon()
            get = Symbol(get)
            # get_units = str(get_units)
            # solve for get
            arrange = solve(self.equation, get)
            get = str(get)
            # sympy sub to substitute dimcon.dimcon_dict into symfor's eq
            sub_vals = []
            for key in self.eq_dict:
                if key is not get:
                    sub_vals.append((self.eq_dict[key][0], self.in_dict[key][0]))
            subd_eq = self.equation.subs(sub_vals)
            base_sol = solve(subd_eq, get)
            # need to convert base_sol's list output to correct units
            # make it a float accurate up to the thousands place
            answer = ceil(1000*base_sol[0]/dimcon.dimconlib[get_units])/1000
            #answer = base_sol[0]/self.dimcon.dimcon_dict[get_units]
            print(answer)
            return answer
