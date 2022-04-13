import unittest

from gitlog import User


class GitlogUser(unittest.TestCase):
    def test_user(self):
        user = User(username='Amir-Shamsi')
        repo = user.get_repos()
        expected_repo = ['Amir-Shamsi', 'code-generator-and-uml-diagram', 'cost-prediction-LR',
                         'cpu-scheduling-algorithm', 'Data-Structure-Patient-Manager-Project',
                         'Digi-Work-symfony-web-application', 'facial-comparison-api-server', 'Hide-Data-BP',
                         'Hw5-Judge', 'markdown', 'MIPS-Microarchitecture-Processor', 'Multicycle-MIPS-in-Verilog',
                         'numpy', 'simple-php-website', 'SpAlgo', 'Symfony-Secure-Login-Registration-Form', 'tocode',
                         'TUI-Bank-Client', 'uni-students-app-ui']

        self.assertEqual(user.fullname, 'Amir Shamsi')
        self.assertEqual(user.avatar_url, 'https://avatars.githubusercontent.com/u/59437623?v=4')
        self.assertEqual(repo, expected_repo)
        self.assertEqual(user.get_followers_count(), 33)
        self.assertEqual(user.get_followings_count(), 19)
        self.assertEqual(user.get_bio(),
                         'Computer engineer with 2+ years of work experience | It’s going to be interesting to see how society deals with synthetics, but it will definitely be cool 🌃')


if __name__ == '__main__':
    unittest.main()
