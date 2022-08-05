# Example file for patch antenna design
# Generates a PCB profile
# by bhanuchander210
# requires patch_antenna, scipy library

from gerber_writer import (DataLayer, Path, set_generation_software)
import os
import patch_antenna as pa

# resonant frequency in Hz
freq = 2.4 * 10 ** 9

# dielectric constant
er = 4.4

# thickness of the cavity in meter
h = 1.6 * 10 ** -3

pa_design = pa.design(freq, er, h)
pl = pa_design.patch_length * 10 ** 3
pw = pa_design.patch_width * 10 ** 3
fl = pa_design.feeder_length * 10 ** 3
fw = pa_design.feeder_width * 10 ** 3


version = '0.3.1'
set_generation_software('patch_antenna', 'patch_antenna_gerber_writer', version)
profile_layer = DataLayer('Copper,L1,Top')
profile = Path()
profile.moveto((0, 0))
profile.lineto((pl, 0))
profile.lineto((pl, (pw/2)-(fw/2)))
profile.lineto((pl+fl, (pw/2)-(fw/2)))
profile.lineto((pl+fl, (pw/2)-(fw/2)+fw))
profile.lineto((pl, (pw/2)-(fw/2)+fw))
profile.lineto((pl, pw))
profile.lineto((0, pw))
profile.lineto((0, 0))
profile_layer.add_region(profile, 'Other,Antenna')
with open(os.path.join('gerbers', 'gerber_writer_antenna_design_2.4GHz.gbr'), 'w') as outfile:
    profile_layer.dump_gerber(outfile)
