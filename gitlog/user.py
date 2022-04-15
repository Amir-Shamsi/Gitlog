import queue
import threading

from .follow import Follow
from .profile import Profile
from .repo import Repo

class User(Follow, Repo, Profile):

    username = None

    def __init__(self, username: str, fullname=None, profile_url=None, avatar_url=None, terminal_logs=True):
        Profile.__init__(self, username, fullname, profile_url, avatar_url, terminal_logs)
        Repo.__init__(self, terminal_logs)
        Follow.__init__(self, terminal_logs)
        self.username = username
        self._repos_data, self._followers_data, self._followings_data = [], [], []

    def get_bio(self):
        return self._profile_data['bio']

    def get_followers_count(self):
        return self._profile_data['followers']

    def get_followings_count(self):
        return self._profile_data['following']

    def get_created_date(self):
        return self._profile_data['created_at']

    def get_location(self):
        return self._profile_data['location']

    def get_repos(self, *keys, count=100):
        if len(keys) == 0:
            keys=['name', 'description']
        self._repo_jdata_init(count, self.username)
        repos, _cc = [], 0
        for repo in self._repos_data:
            if _cc == count: break
            try:
                repos.append({key: repo[key] for key in keys})
            except KeyError as ky_err:
                raise RuntimeError('Key {} is invalid for repository info!'.format(ky_err))
            _cc += 1
        return repos

    def get_followers(self, count=100, _q=None):
        self._followers_jdata_init(count, self.username)
        _res_fo = [data['login'] for data in self._followers_data][:count]
        if isinstance(_q, queue.Queue): _q.put(_res_fo)
        else: return _res_fo

    def get_followings(self, count=100, _q=None):
        self._followings_jdata_init(count, self.username)
        _res_fo = [data['login'] for data in self._followings_data][:count]
        if isinstance(_q, queue.Queue): _q.put(_res_fo)
        else: return _res_fo

    def _get_follow_data(self, count):
        _qfg, _qfr = queue.Queue(), queue.Queue()
        _tfg = threading.Thread(target=self.get_followings, args=(count, _qfg))
        _tfr = threading.Thread(target=self.get_followers, args=(count, _qfr))
        _tfr.start(), _tfg.start()
        _tfr.join(), _tfg.join()
        return _qfg.get(), _qfr.get()

    def get_non_followers(self, count=1000):
        _followings, _followers = self._get_follow_data(count)
        return [each for each in _followings if each not in _followers][:count]

    def get_non_followings(self, count=1000):
        _followings, _followers = self._get_follow_data(count)
        return [each for each in _followers if each not in _followings][:count]


