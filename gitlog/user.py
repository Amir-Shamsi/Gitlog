import requests
import simplejson as json
from enum import Enum, unique


class User:
    @unique
    class Url(Enum):
        user = 'https://api.github.com/users/{}'
        repo = 'https://api.github.com/users/{}/repos'

    id = None
    username = None
    fullname = None
    profile_url = None
    avatar_url = None
    _profile_data = None
    _repos_data = None

    def __init__(self, username: str, fullname=None, profile_url=None, avatar_url=None):
        self.username = username

        if fullname or profile_url or avatar_url is None:
            self._prof_jdata_init()
            self.fullname = self._profile_data['name']
            self.avatar_url = self._profile_data['avatar_url']
            self.profile_url = self._profile_data['url']

    def _prof_jdata_init(self):
        if self._profile_data is not None: return
        url = self.Url['user'].format(self.username)
        self._profile_data = json.loads((requests.get(url)).text)

    def get_bio(self):
        self._prof_jdata_init()
        return self._profile_data['bio']

    def get_followers_count(self):
        self._prof_jdata_init()
        return self._profile_data['followers']

    def get_followings_count(self):
        self._prof_jdata_init()
        return self._profile_data['followings']

    def get_created_date(self):
        self._prof_jdata_init()
        return self._profile_data['created_at']

    def get_location(self):
        self._prof_jdata_init()
        return self._profile_data['location']

    def get_repos(self):
        self._repo_jdata_init()
        return self._repos_data

    def _repo_jdata_init(self):
        if self._profile_data is not None: return
        url = self.Url['repo'].format(self.username)
        self._repos_data = json.loads((requests.get(url)).text)

