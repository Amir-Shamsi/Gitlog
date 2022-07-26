from gitlog import User

user = User('amir-shamsi', terminal_logs=True)  # make "terminal_logs" True if you want to see the info loading logs

non_followings = user.get_non_followings(count=10)  # set a count for get the exact amount of non-followings as a list default is 1000

print(non_followings)