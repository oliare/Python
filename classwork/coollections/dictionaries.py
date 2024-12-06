# -------- dictionaries -------- 
users = {120:'Vlad', 555:"Nazar", 9800:"Luda"}

users[555] = 'Viktor'

if 555 in users:
    print('yes')
else: print('no')

for i in users: print(f"{i} - {users[i]}")
for key, val in users.items: print(f"{key} - {val}")