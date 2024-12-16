from django.http import HttpResponse
from django.shortcuts import render

users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
    },
]

def home(request):
    return HttpResponse("<h1>Welcome to the User List</h1> <a href='/users/'>View Users</a>")

def list(request):
    html = "<h1>Users</h1><ul>"
    for user in users:
        html += f"""
            <li>
                <strong>Name:</strong> {user['name']}<br>
                <strong>Username:</strong> {user['username']}<br>
                <strong>Email:</strong> {user['email']}<br>
                <strong>Address:</strong> {user['address']['street']}, {user['address']['city']}<br>
                <strong>Phone:</strong> {user['phone']}<br>
                <strong>Website:</strong> <a href='http://{user['website']}'>Visit Website</a><br>
                <a href='/users/{user["id"]}/'>More details</a>
                <br><br>
            </li>
        """
    html += "</ul>"
    return HttpResponse(html)


def details(request, id):
    user = []
    for u in users:
        if u["id"] == id:
            user = u
            break

    if user is None:
        return HttpResponse("<h1>User not found</h1>")

    html = f'''
    <h1>{user['name']}</h1>
    <p><strong>Username:</strong> {user['username']}</p>
    <p><strong>Email:</strong> {user['email']}</p>
    <p><strong>Address:</strong> {user['address']['street']}, {user['address']['city']}</p>
    <p><strong>Phone:</strong> {user['phone']}</p>
    <p><strong>Website:</strong> <a href='http://{user['website']}'>{user['website']}</a></p>
    <a href='/users/'>Back to User List</a>
    '''
    return HttpResponse(html)
