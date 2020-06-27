current_users = ['Angus', 'McCheng', 'quartz', 'Rayle', 'Redicue']
current_users_lower = []
new_users = ['Angus', 'RAYLE', 'Badminton', 'Raynor', 'Gadot']

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'You will need to enter a new username, {user} has already been taken')