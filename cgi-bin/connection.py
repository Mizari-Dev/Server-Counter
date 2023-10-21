import cgi
import requests

args = cgi.FieldStorage()
redirect = "http://localhost:8000"

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '[YOUR_CLIENT_ID]'
CLIENT_SECRET = '[YOUR_CLIENT_SECRET]'
REDIRECT_URI = 'http://localhost:8000/cgi-bin/connection.py'
try:
    CODE = args["code"].value

    data = {
        'grant_type': 'authorization_code',
        'code': CODE,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
    r.raise_for_status()
    json = r.json()
    token = json["access_token"]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token
    }
    r = requests.get('%s/users/@me/guilds' % API_ENDPOINT, headers=headers)
    r.raise_for_status()
    json = r.json()
    count = len(json)
    redirect += "?count="+str(count)

    print(
        f"""\
Content-Type: text/html
Location: {redirect}

<html>
    <head>
        <title>Vous allez être redirigé...</title>
        <meta http-equiv=\"refresh\" content=\"0;url={redirect}\">
    </head>
    <body>
        Redirection... Cliquez <a href={redirect}>ici</a> si vous n'êtes pas redirigé
    </body>
</html>"""
    )
except Exception as error:
    print(
        f"""\
Content-Type: text/html

<html>
    <head>
        <title>Error</title>
    </head>
    <body>
        {error}
    </body>
</html>"""
    )
