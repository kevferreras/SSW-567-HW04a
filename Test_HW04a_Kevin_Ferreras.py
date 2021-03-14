'''The purpose of this file is to test all function(s) in the HW04a file'''

import unittest
from unittest.mock import Mock, patch
from HW04a_Kevin_Ferreras import github_repo_names_and_commits
import json


class GithubRepoNamesandCommitsTest(unittest.TestCase):

    @patch('requests.get')
    def test_github_repo_names_and_commits(self, mock_get) -> None:
        '''Tests that the correct message is output'''

        results = [Mock(), Mock(), Mock(), Mock(), Mock()]
        results[0].json.return_value = json.loads('[{"name":"Test-Repo1"}, {"name":"Test-Repo2"}, \
                                                    {"name":"Test-Repo3"}, {"name":"Test-Repo4"}]')
        results[1].json.return_value = json.loads('[{"commit":"1"}, {"commit":"2"}]')
        results[2].json.return_value = json.loads('[{"commit":"1"}, {"commit":"2"}, {"commit":"3"}, {"commit":"4"}]')
        results[3].json.return_value = json.loads('[{"commit":"1"}, {"commit":"2"}, {"commit":"3"}, {"commit":"4"}, \
                                                    {"commit":"5"}, {"commit":"6"}]')
        results[4].json.return_value = json.loads('[{"commit":"1"}, {"commit":"2"}, {"commit":"3"}, {"commit":"4"}, \
                                                    {"commit":"5"}, {"commit":"6"}, {"commit":"7"} , {"commit":"8"}]')

        mock_get.side_effect = results

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

