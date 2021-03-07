'''The purpose of this file is to test all functions in the HW04a file'''

import unittest
from typing import Dict
from HW04a_Kevin_Ferreras import github_repo_names_and_commits, github_repo_names_and_commits_output 


class GitHubRepoNamesandCommitsTest(unittest.TestCase):


    def test_github_repo_names_and_commits(self) -> None:
        '''Tests that the function gathers a dictionary of correct repo names and number of commits based on a given GitHub User ID'''

        gitub_user_id: str = 'TestAccountKF'
        expected_repository_names_and_commits: Dict[str : int] = {
                                                                    'Test-Repo1' : 2,
                                                                    'Test-Repo2' : 4,
                                                                    'Test-Repo3' : 6,
                                                                    'Test-Repo4' : 8,
                                                                }


        self.assertEqual(expected_repository_names_and_commits, github_repo_names_and_commits(gitub_user_id))

    def test_github_repo_names_and_commits_output(self) -> None:
        '''Tests that the correct message is output'''

        expected_output: List[str] = [

                    'Repo name: Test-Repo1 Number of commits: 2',
                    'Repo name: Test-Repo2 Number of commits: 4',
                    'Repo name: Test-Repo3 Number of commits: 6',
                    'Repo name: Test-Repo4 Number of commits: 8',
        ]

        output_status: List[str] = list()

        for output in github_repo_names_and_commits_output(): # <------Generator
            if output in expected_output:
                output_status.append('pass')
        
        self.assertEqual(len(expected_output), len(output_status))















if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)

