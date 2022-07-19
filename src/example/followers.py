from gitlog import User

user = User('amir-shamsi', terminal_logs=True)

print(user.get_followers_count())


followings_10 = user.get_followings(count=10)
print(followings_10)

followings_30 = user.get_followings(count=30)
print(followings_30)