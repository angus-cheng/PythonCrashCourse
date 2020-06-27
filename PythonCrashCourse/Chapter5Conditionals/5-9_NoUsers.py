usernames = []
# usernames = ['admin', 'McCheng', 'quartz', 'Rayle', 'Redicue']
if usernames:
    for username in usernames:
        if username == 'admin': 
            print("Hello admin, would you like a status report?")
        else:
            print(f"Hello {username}")
else:
    print("We need to find some users")