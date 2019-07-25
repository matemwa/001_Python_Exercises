import json
import pygal.maps.world

from country_code import get_country_code

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Grouping countries by population levels


wm = pygal.maps.world.World()
wm.title = 'World population in 2010, by country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
