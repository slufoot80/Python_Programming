import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

"""Make an api call and store the response"""
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

"""Store API response in a variable."""
response_dict = r.json()

"""Process results."""
print("Total repositories: ",  format(response_dict['total_count'], ',d'))

"""Export information about the respositories."""
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

"""Make Visualization."""
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('/home/fnowicki/python_repos.svg')
