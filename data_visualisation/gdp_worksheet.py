import json
import pygal.maps.world

from country_code import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp_value = gdp_dict['Value'] / 1000000
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp_value
    elif gdp_dict['Year'] == 2011 and gdp_dict['Country Name'] == 'Libya':
        country_name = gdp_dict['Country Name']
        gdp_value = gdp_dict['Value'] / 1000000
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp_value



cc_gdp_1, cc_gdp_2, cc_gdp_3, cc_gdp_4 = {}, {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 100000:
        cc_gdp_1[cc] = gdp
    elif gdp < 1000000:
        cc_gdp_2[cc] = gdp
    elif gdp < 10000000:
        cc_gdp_3[cc] = gdp
    else:
        cc_gdp_4[cc] = gdp

# print(cc_gdp)


wm = pygal.maps.world.World()
wm.title = 'GDP in millions in 2016, by country \n*2011 for Yemen'
wm.add('< 10^5', cc_gdp_1)
wm.add('10^5-10^6', cc_gdp_2)
wm.add('10^6-10^7', cc_gdp_3)
wm.add('> 10^7', cc_gdp_4)
wm.render_to_file('GDP.svg')

