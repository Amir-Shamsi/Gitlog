from gitlog import User

user = User('amir-shamsi', terminal_logs=True)  # make "terminal_logs" True if you want to see the info loading logs

non_followers = user.get_non_followers(count=10)  # set a count for get the exact amount of non-followers as a list default is 1000

print(non_followers)