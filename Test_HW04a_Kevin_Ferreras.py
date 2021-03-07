'''The purpose of this file is to test all function(s) in the HW04a file'''

import unittest
from typing import Dict
from HW04a_Kevin_Ferreras import github_repo_names_and_commits


class GithubRepoNamesandCommitsTest(unittest.TestCase):

    def test_github_repo_names_and_commits(self) -> None:
        '''Tests that the correct message is output'''

        github_user_id: str = 'TestAccountKF'

        expected_output: List[str] = [

                    'Repo name: Test-Repo1 Number of commits: 2',
                    'Repo name: Test-Repo2 Number of commits: 4',
                    'Repo name: Test-Repo3 Number of commits: 6',
                    'Repo name: Test-Repo4 Number of commits: 8',
        ]

        output_status: List[str] = list()

        for output in github_repo_names_and_commits(github_user_id):
            if output in expected_output:
                output_status.append('pass')
        
        self.assertEqual(len(expected_output), len(output_status))



if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)

