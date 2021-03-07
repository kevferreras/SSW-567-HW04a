'''The Purpose of this file is to create a function that uses Github's API to collect and output repo names and number of 
    commits to each repo, based on a given user github ID'''

import requests, json
from typing import Dict, DefaultDict, Iterator
from collections import defaultdict


def github_repo_names_and_commits(github_user_id: str) -> Iterator:
    '''Parses through the Github API json response object to collect and output all repo names and the number of commits for a given user'''

    repo_names_and_commits: DefaultDict[str, int] = defaultdict(int) #key = repo name : value = # of commits

    github_api_response = requests.get(f'https://api.github.com/users/{github_user_id}/repos').json()

    for element in github_api_response:
        repo_name: str = element['name']
        repo_names_and_commits[repo_name]

    for repo_name in repo_names_and_commits:
        number_of_commits: int = len(requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits').json())
        repo_names_and_commits[repo_name] = number_of_commits

    for repo_name, commits in repo_names_and_commits.items():
        yield f'Repo name: {repo_name} Number of commits: {commits}'

def main() -> None:
    '''Prints the output of repository names and number of commits made to that repository'''

    for output in github_repo_names_and_commits('TestAccountKF'):
        print(output)



if __name__ == "__main__":
    main()