from sympy import *
import math
from conversions.dimensions import acceleration, angle, area, energy, force, \
    length, mass, pressure, time, velocity, volume, density

class Formula(object):
    no_inst = 0     # number of instances of the Equation class
    in_dict = {}    # in_dict starts empty
    def __init__(self, streq, strdict):
        self.equation = self.mkeq(streq)
        self.eq_dict = self.mkdict(strdict)
        self.libs = self.mklibs()
        self.baselist = self.mkbaselist()
        Formula.no_inst = Formula.no_inst + 1

    def mkeq(self, astr):
        expr = sympify(astr)    # turns streq into Sympy Eq()
        return expr

    def mkdict(self, adict):
        for i in adict:         # turns the first string of each dict value into a Symbol
            adict[i][0] = Symbol(adict[i][0])
        return adict

    def show_eq(self):
        print(self.equation)

    def mklibs(self):
        # this method takes all of turns each seperate conversion dictionary into one large dictionary
        # having one large dict removes the need to search each dicionary to find whether
        # a unit is stored
        dictlist = []
        for i in self.eq_dict:
            dictlist.append(self.eq_dict[i][1].dimdict)
        dimconlib = {k:v for d in dictlist for k, v in d.items()}
        return dimconlib

    def mkbaselist(self):
        baselist = []
        for i in self.eq_dict:
            baselist.append(self.eq_dict[i][1].base)
        return baselist

    @classmethod
    def get_no_equations(cls):
        # number of instances of the Equation class
        return cls.no_inst

    @staticmethod
    def round_to_thousandth(num):
        num = ceil(num*1000)/1000
        return num

    def check_typo(self):
        # it typo on dimensions give user another try to enter
        # not needed for dropdown tabs
        pass

    def clear_inputs(self):
        self.in_dict = {}   # clears in_dict
        return self.in_dict

    def input_vars(self, get):
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
        for key in self.in_dict:
            if self.in_dict[key][1] in self.libs:
                self.in_dict[key][0] = self.in_dict[key][0]*self.eq_dict[key][1].dimdict[self.in_dict[key][1]]
                self.in_dict[key][1] = self.eq_dict[key][1].base
            else:
                print('Conversion not stored')
        return self.in_dict

    def solvefor(self, get, get_units):
        if get_units not in self.libs:
            print('Equati does not currently support the dimension: {}'.format(get_units))
        else:
            self.clear_inputs()
            self.input_vars(get)
            self.dimcon()
            get = Symbol(get)
            # get_units = str(get_units)
            arrange = solve(self.equation, get) # solve for get
            get = str(get)
            # sympy sub to substitute dimcon.dimcon_dict into symfor's eq
            sub_vals = []
            for key in self.eq_dict:
                if key is not get:
                    sub_vals.append((self.eq_dict[key][0], self.in_dict[key][0]))
            subd_eq = self.equation.subs(sub_vals) # substituted all values for keys in in_dict
            base_sol = solve(subd_eq, get)
            answer = math.ceil(1000*base_sol[0]/self.libs[get_units])/1000 # convert base_sol's list output to correct units
            print(answer)
            return answer
'''
bern_dict = {'p1': ['p1', pressure],
 'rho': ['rho', density], 'z1': ['z1', length],
 'v1': ['v1', velocity], 'p2': ['p2', pressure],
 'z2': ['z2', length], 'v2': ['v2', velocity],
 'h_f': ['h_f', length], 'h_ff': ['h_ff', length],
 'h_pump': ['h_pump', length]}
bern = Formula('p1/(rho*9.80665)+z1+v1**2/(2*9.80665)-p2/(rho*9.80665)-z2-v2**2/(2*9.80665)-h_f-h_ff+h_pump', bern_dict)
#bern.solvefor('p1', 'N/m^2')
bern.show_eq()
'''

work_dict = {'x': ['x', length], 'F': ['F', force], 'W': ['W', energy]}
work = Formula('W-F*x', work_dict)
#work.solvefor('W', 'J')
work.show_eq()
work.solvefor('x', 'km')
