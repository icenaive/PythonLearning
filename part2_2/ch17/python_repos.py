import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("status code", r.status_code)

response_dict = r.json()

print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['item']