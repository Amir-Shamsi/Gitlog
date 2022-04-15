import unittest
from gitlog import User

class GitlogUser(unittest.TestCase):
    def test_user(self):
        user = User(username='Amir-Shamsi', terminal_logs=True)
        repo = user.get_repos()
        expected_repo = [{'name': 'Amir-Shamsi', 'description': 'My GitHub Profile README 🙂'},
                         {'name': 'code-generator-and-uml-diagram',
                          'description': 'Implementation of UML diagram Application using Java and Implementation of Graphic User Interface using JavaFX.'},
                         {'name': 'cost-prediction-LR',
                          'description': 'Insurance cost prediction using Linear Regression'},
                         {'name': 'cpu-scheduling-algorithm',
                          'description': "CPU scheduling algorithm program to calculate processes' process time"},
                         {'name': 'Data-Structure-Patient-Manager-Project', 'description': None},
                         {'name': 'Digi-Work-symfony-web-application', 'description': None},
                         {'name': 'facial-comparison-api-server', 'description': 'Fast face-comparison API server 👽'},
                         {'name': 'Hide-Data-BP',
                          'description': 'Hiding information or data behind a picture in python.'},
                         {'name': 'Hw5-Judge', 'description': 'Fifth Homework of Principle Of Programming Fall 2020'},
                         {'name': 'markdown',
                          'description': 'A Python implementation of John Gruber’s Markdown with Extension support.'},
                         {'name': 'MIPS-Microarchitecture-Processor',
                          'description': 'MIPS Single-Cycle Microarchitecture Processor'},
                         {'name': 'Multicycle-MIPS-in-Verilog', 'description': 'MIPS Multicycle CPU design in Verilog'},
                         {'name': 'numpy',
                          'description': 'The fundamental package for scientific computing with Python.'},
                         {'name': 'simple-php-website',
                          'description': "This is a personal blog which's coded by raw PHP and translated to Persian"},
                         {'name': 'SpAlgo',
                          'description': 'SpAlgo is a python library with special algorithms which will helps you a lot.'},
                         {'name': 'Symfony-Secure-Login-Registration-Form',
                          'description': 'Symfony registration form with all validations and no cheating allowed🥱 will code the login soon! just have some projects to do :) Enjoy'},
                         {'name': 'tocode', 'description': 'a python library to convert string into code { }'},
                         {'name': 'TUI-Bank-Client',
                          'description': 'This project had been created by a TUI method which is command method means bank clerk when start he/she will see a list of command with keywords and in the last line “Type Your Command:> “ will appear and clerk must type an valuable keyword, the good point in here is that program created in way that doesn’t crash and give clerk errors by typing wrong keywords, on other hand clerk doesn’t worry about errors in the whole program, even if the internet connection has problems, at the program launch! This it a big point and advantage. The other advantage is that the program or client is colorful, and the clerk won’t be tired during the performance! The client doesn’t care about the way you type it means if you type “exit” or “eXiT” client see them in same way and understand that you want to exit! (not a case sensitive)'},
                         {'name': 'uni-students-app-ui',
                          'description': "Students' homework mobile application user interface! 📱🎓"}]

        self.assertEqual(user.fullname, 'Amir Shamsi')
        self.assertEqual(user.avatar_url, 'https://avatars.githubusercontent.com/u/59437623?v=4')
        self.assertEqual(repo, expected_repo)
        self.assertEqual(user.get_followers_count(), 37)
        self.assertEqual(user.get_followings_count(), 23)
        self.assertEqual(user.get_location(), 'Earth')
        self.assertEqual(user.get_created_date(), "2020-01-02T10:06:09Z")
        self.assertEqual(user.get_bio(),
                         'Computer engineer with 2+ years of work experience | It’s going to be interesting to see how society deals with synthetics, but it will definitely be cool 🌃')


if __name__ == '__main__':
    unittest.main()
