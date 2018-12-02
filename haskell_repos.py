import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call to github and prints a status code

url = 'https://api.github.com/search/repositories?q=language:haskell&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# working on a data in .json file
response_dict = r.json()
print("Total repositories:", (response_dict['total_count']))
repo_dicts = response_dict['items']

# filling up dicts with and necessary data from repositories API call
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if not description:
        description = "No description was provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualisation / draw chart
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 18
my_style.major_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 60
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-starred Python projects on Github.'
chart.x_labels = names
chart.y_labels = (0, 5000, 10000, 15000)

chart.add('', plot_dicts)
chart.render_to_file('haskell_repos.svg')