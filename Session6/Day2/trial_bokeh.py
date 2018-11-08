import numpy as np

from astropy.table import Table

idsource = input("Insert your field id: \n >> ")
idsource = int(idsource)

magLim = 20
age = 10
rad_deg = 1
met = 0.00019
rh_pc = 50

def main():

    dist_kpc = int(input("Insert the limiting distance (kpc) for your study: \n >> "))
    mass = int(input("Insert the mass of the dwarf (stellar mass) galaxy: \n >> "))
    groupvel = int(input("Insert the velocity (km/s) for the group velocity of the dwarf: \n >> "))

    return  dist_kpc, mass,  groupvel

print("\n")
dist_kpc, mass,  groupvel = main()
print("Magnitude limit for this study is:", magLim)
print("Search radius (deg) for this study is:", rad_deg)
print("We are looking up to a distance (kpc) of:", dist_kpc)
print("The mass (stellar mass) of the dwarf is:", mass)
print("The rh (pc) for the dwarf is:", rh_pc)
print("The group velocity (km/s) for the dwarf is:", groupvel)


t_name = "/Users/ioanaciuca/Desktop/GDR2_and_Fermi/make_dwarfs/final_datafiles/sourceid%s_dwarf_d%s_M%s_Vgroup%s.fits "% (int(idsource), int(dist_kpc), int(mass), int(groupvel))

data = Table.read(t_name, format = "fits")

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

x = np.array(data["pmRA"])
y = np.array(data["pmDEC"])

bins = hexbin(x, y, 0.01)

p = figure(title="Manual hex bin points", tools="wheel_zoom,reset",
           match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("hex_tile.html")

show(p)