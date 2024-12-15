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
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
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
            "geo": {"lat": "-43.9509", "lng": "-34.4618"},
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains",
        },
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
            "geo": {"lat": "-68.6102", "lng": "-47.0653"},
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications",
        },
    },
]


# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")


def list(request):
    html = "<h1>Users</h1> <ul>"
    for user in users:
        html+= f'''
        <li>User: {user['id']}</li>
        <ul>
        <li>Name: {user['name']} </li>
        <li>Username: {user['username']}</li>
        <li>Email: {user['email']}</li>
        <li>Address:</li>
            <ul>
                <li>Street: {user['address']['street']} </li>
                <li>Suite: {user['address']['suite']} </li>
                <li>City: {user['address']['city']} </li>
                <li>Zipcode: {user['address']['zipcode']} </li>
                <li>Geo: {user['address']['geo']} </li>
            </ul>
        <li>Phone: {user['phone']}:</li>
        <li>Website: {user['website']}</li>
        <li>Company: </li>
            <ul>
                <li>Name: {user['company']['name']} </li>
                <li>CatchPhrase: {user['company']['catchPhrase']} </li>
                <li>Bs: {user['company']['bs']} </li>
            </ul>
        </ul>
        <br>
        '''
    html += "</ul>"

    return HttpResponse(html)


def details(request, id):
    html = "<h1>Users</h1> <ul>"
    for user in users:
        if user['id']==id:
            html+= f'''
            <li>User: {user['id']}</li>
            <ul>
            <li>Name: {user['name']} </li>
            <li>Username: {user['username']}</li>
            <li>Email: {user['email']}</li>
            <li>Address:</li>
                <ul>
                    <li>Street: {user['address']['street']} </li>
                    <li>Suite: {user['address']['suite']} </li>
                    <li>City: {user['address']['city']} </li>
                    <li>Zipcode: {user['address']['zipcode']} </li>
                    <li>Geo: {user['address']['geo']} </li>
                </ul>
            <li>Phone: {user['phone']}:</li>
            <li>Website: {user['website']}</li>
            <li>Company: </li>
                <ul>
                    <li>Name: {user['company']['name']} </li>
                    <li>CatchPhrase: {user['company']['catchPhrase']} </li>
                    <li>Bs: {user['company']['bs']} </li>
                </ul>
            </ul>
            <br>
            '''
    html += "</ul>"

    
    return HttpResponse(html)