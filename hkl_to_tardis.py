from ophyd import Component as Cpt
from ophyd import (PseudoSingle, EpicsMotor, SoftPositioner, Signal)
from hkl.diffract import E6C
from hkl.util import Lattice
from ophyd.pseudopos import (pseudo_position_argument, real_position_argument)

# TODO: fix upstream!!
class NullMotor(SoftPositioner):
    @property
    def connected(self):
        return True

class Tardis(E6C):
    h = Cpt(PseudoSingle, '')
    k = Cpt(PseudoSingle, '')
    l = Cpt(PseudoSingle, '')

    theta = Cpt(NullMotor)
    omega = Cpt(NullMotor)
    chi =   Cpt(NullMotor)
    phi =   Cpt(NullMotor)
    delta = Cpt(NullMotor)
    gamma = Cpt(NullMotor)
    #energy = Cpt(NullMotor)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theta.move(0.0)
        self.omega.move(0.0)
        self.chi.move(0.0)
        self.phi.move(0.0)
        self.delta.move(0.0)
        self.gamma.move(0.0)

    @pseudo_position_argument
    def set(self, position):
        return super().set([float(_) for _ in position])


tardis = Tardis('', name='tardis')

# re-map Tardis' axis names onto what an E6C expects
name_map = {'mu': 'theta', 'omega': 'omega', 'chi': 'chi', 'phi': 'phi', 'gamma': 'delta', 'delta': 'gamma'}
tardis.calc.physical_axis_names = name_map

tardis.calc.engine.mode = 'lifting_detector_mu'
