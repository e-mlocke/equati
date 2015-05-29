from dimlib.conversions import acceleration_dimcon, angle_dimcon, area_dimcon, energy_dimcon, \
 force_dimcon, length_dimcon, mass_dimcon, pressure_dimcon, time_dimcon, \
 velocity_dimcon, volume_dimcon, density_dimcon

class Dimension(object):
    def __init__(self, dimdict, base):
        self.dimdict = dimdict
        self.base = base

    def get_base(self):
        print(self.base)
        return self.base

    def chk_dict(self, key):
        if key in self.dimdict:
            print('True')
            return True
        else:
            print('False')
            return False


acceleration = Dimension(acceleration_dimcon, 'm/s^2')
angle = Dimension(angle_dimcon, 'radian')
area = Dimension(area_dimcon, 'm^2')
density = Dimension(density_dimcon, 'kg/m^3')
energy = Dimension(energy_dimcon, 'J')
force = Dimension(force_dimcon, 'N')
length = Dimension(length_dimcon, 'm')
mass = Dimension(mass_dimcon, 'kg')
pressure = Dimension(pressure_dimcon, 'N/m^2')
time = Dimension(time_dimcon, 's')
velocity = Dimension(velocity_dimcon, 'm/s')
volume= Dimension(volume_dimcon, 'm^3')

dimconlib = (acceleration, angle, area, energy, force, length, mass, pressure,
 time, velocity, volume)


'''
for i in dimconlib:
    i.get_base()
'''
