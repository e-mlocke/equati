from sympy import *
import math
from dimlib.dimensions import acceleration, angle, area, energy, force, \
    length, mass, pressure, time, velocity, volume, density

class Equation(object):
    # number of instances of the Equation class
    no_inst = 0
    def __init__(self, streq, strdict):
        self.equation = self.mkeq(streq)
        self.eq_dict = self.mkdict(strdict)
        self.baselist = self.mkbaselist()
        Equation.no_inst = Equation.no_inst + 1
    #=========== for __init__ ============
    def mkeq(self, astr):
        # turns streq into Sympy Eq()
        expr = sympify(astr)
        return expr

    def mkdict(self, adict):
        # turns the first string of each dict value into a Symbol
        for i in adict:
            adict[i][0] = Symbol(adict[i][0])
        return adict

    def mkbaselist(self):
        baselist = []
        for i in self.eq_dict:
            baselist.append(self.eq_dict[i][1].base)
        return baselist
    #=========================================
    def show_eq(self):
        print(self.equation)

def mklibs(equation):
    # this method takes all of turns each seperate conversion dictionary used in the equation into one large dictionary
    # having one large dict removes the need to search each dicionary to find whether
    # a unit is stored
    dictlist = []
    for i in equation.eq_dict:
        dictlist.append(equation.eq_dict[i][1].dimdict)
    all_conversions = {k:v for d in dictlist for k, v in d.items()}
    return all_conversions

def solver(equation, depvar, units):
    # see REDMINE line this is buggy
    in_dict = {}    # in_dict starts empty
    all_conversions = mklibs(equation)
    equation.show_eq()
    for key in equation.eq_dict:
        if key is not depvar:
            # asks for known dimensional values and units for each independent var
            known_val = float(raw_input("Value of {}: ".format(key)))
            known_units = raw_input("Units of {} : ".format(key))
            if known_units in equation.eq_dict[key][1].dimdict:
                # if the known unit is usable, convert the unit to the dimensional "base" unit
                # multiply its in_dict value by the corresponding all_conversions value
                known_val = all_conversions[known_units]*known_val
                #########REDMINE===================
                # using all_conversions allows the input of units that describe different types
                # of dimensions to be tied to variables
                # eg. giving "N" to an energy var
                ######SUGGEST--------------
                # when looping thru each key loop thru its related dimlib
                known_units = equation.eq_dict[key][1].base
                known_dimension = [known_val, known_units]
                in_dict[key] = known_dimension
                print(known_dimension)
            else:
                print("Conversion not stored")
                break
            print(in_dict)

work_dict = {'x': ['x', length], 'F': ['F', force], 'W': ['W', energy]}
work = Equation('W-F*x', work_dict)
solver(work, 'x', 'm')
'''
    def clear_inputs(self):
        self.in_dict = {}   # clears in_dict
        return self.in_dict

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
