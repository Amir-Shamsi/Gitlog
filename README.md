# Gitlog


<p align='center'>
    <a href="#">
        <img src="https://raw.githubusercontent.com/Amir-Shamsi/gitlog/master/doc/intro.png"  alt="gitlog" />
    </a>
</p>


[![Python version](https://img.shields.io/badge/python-%5E3.*-purple?style=flat-square)](https://www.python.org/)
[![BSD Licence](https://img.shields.io/badge/licence-MIT-geen?style=flat-square)](LICENSE)
<a href="https://github.com/Amir-Shamsi/gitlog" title="Repo Size">
<img src="https://img.shields.io/github/repo-size/Amir-Shamsi/gitlog?label=Repo%20Size&logo=Github&style=flat-square" alt="Project Initiator Repo Size"/>
</a>
[![Downloads](https://static.pepy.tech/personalized-badge/gitlog?period=total&units=international_system&left_color=black&right_color=MediumVioletRed&left_text=Downloads)](https://pepy.tech/project/gitlog)
[![PyPI version shields.io](https://img.shields.io/pypi/v/gitlog.svg?style=flat-square)](https://pypi.python.org/pypi/gitlog/)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/amir-shamsi/gitlog/CodeQL?style=flat-square)


Gitlog is a python library for working with @Github users' logs and ***hidden details***. you can use it in any python project using `pip install gitlog`

## Overview
Gitlog is a python library which helps you log users' followers, followings, repos, and user ***hidden details***.<br>
have you ever wanted to see who is in your `nonfollower` list? oh is it hard for you to look all over your followings to find out? well good news! gitlog gonna help you in not only that but also in for example if you want to show your `repos` on your blog and etc.


## Usage

In the following paragraphs, I am going to describe how you can get and use `gitlog` for your own projects and code.

###  Getting it

To download `gitlog`, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install gitlog
```

### Using it

`gitlog` was programmed with ease-of-use in mind. First, import User from gitlog.

for more exact usage documents you can see the example files [here](https://github.com/Amir-Shamsi/gitlog/blob/master/src/example)

```Python3
from gitlog import User
```

then you can use bassed on what you need:

1. to get your github or someone else github's `general information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

#  access the user information like this -->

>>> user.username
# amir-shamsi

>>> user.fullname
# Amir Shamsi

>>> user.id
# 59437623

>>> user.profile_url
# https://api.github.com/users/Amir-Shamsi

>>> user.avatar_url
# https://avatars.githubusercontent.com/u/59437623?v=4

>>> user.get_created_date()
# 2020-01-02 10:06:09

>>> user.get_bio()
# Computer engineering student (at Shiraz University🏛️) with 2+ years of work experience | It’s going to be
# interestin to see how society deals with synthetics🌃

>>> user.get_location()
# Earth
# ...
```

2. to get your github or someone else github's `repositories information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

>>> user.get_repos(count=2) # set a count for get the the exact amount of repositories default is 100
#  [{
#    'name': 'Amir-Shamsi',
#    'description': 'My GitHub Profile README 🙂'
#   },
#   {
#    'name': 'CleaningBot-partially-observable',
#    'description': 'cleaning agent where the environment is partially observable'
#  }]
```

3. to get your github or someone else github's `followings information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

>>> user.get_followings_count() # get user's followings count

>>> followings = user.get_followings(count=10) # set a count for get the exact amount of followings as a list
#                                                default is 1000
```

4. to get your github or someone else github's `followers information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

>>> user.get_followers_count() # get user's followers count

>>> followers = user.get_followers(count=10) # set a count for get the the exact amount of followers as a list
#                                              default is 1000
```

5. to get your github or someone else github's `non-followers information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

>>> non_followers = user.get_non_followers(count=10) # set a count for get the exact amount of non-followers as a list
#                                                      default is 1000
```

5. to get your github or someone else github's `non-followings information`:
```python3
>>> user = User('amir-shamsi', terminal_logs=True) # make "terminal_logs" True if you want to see the info loading logs

>>> non_followings = user.get_non_followings(count=10) # set a count for get the exact amount of non-followings as a
#                                                        list default is 1000
```

## Support 
Supported versions of python for this library are as follow:
* [Python v3](https://www.python.org/downloads/release/python-300/)
* [Python v3.4](https://www.python.org/downloads/release/python-340/)
* [Python v3.5](https://www.python.org/downloads/release/python-350/)
* [Python v3.6](https://www.python.org/downloads/release/python-360/)
* [Python v3.7](https://www.python.org/downloads/release/python-370/)
* [Python v3.8](https://www.python.org/downloads/release/python-380/)
* [Python v3.9](https://www.python.org/downloads/release/python-390/)
* [Python v3.10](https://www.python.org/downloads/release/python-3100/)

## License
This project is under MIT license read it 
[here](https://github.com/Amir-Shamsi/gitlog/blob/master/LICENSE):
```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

