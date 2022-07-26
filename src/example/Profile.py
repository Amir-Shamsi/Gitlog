from gitlog import User

user = User('amir-shamsi', terminal_logs=True)

#  access the user information like this -->

print(user.username)
print(user.fullname)
print(user.id)
print(user.get_bio())
print(user.get_location())
print(user.profile_url)
print(user.avatar_url)
print(user.get_created_date())
