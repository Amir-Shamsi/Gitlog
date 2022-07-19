from gitlog import User

user = User('amir-shamsi', terminal_logs=True)

print(user.get_followers_count())

followers_10 = user.get_followers(count=10)
print(followers_10)

followers_40 = user.get_followers(count=40)
print(followers_40)