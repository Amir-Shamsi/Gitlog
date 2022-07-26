from gitlog import User

user = User('amir-shamsi', terminal_logs=True)

print(user.get_repos(count=2))