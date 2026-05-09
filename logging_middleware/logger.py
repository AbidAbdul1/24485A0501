# Logger middleware
import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJhYmlkNDU5ODFAZ21haWwuY29tIiwiZXhwIjoxNzc4MzA2MjM4LCJpYXQiOjE3NzgzMDUzMzgsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiJhMDdmOWZjYi00NDU2LTRkNjAtYmQ5Yi1jZDk5OGYxYTlhNmYiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJhYmR1bCBhYmlkIiwic3ViIjoiYjM4OTE5NmItMzZiNy00ZjNlLTk2YWEtMGMwMDQ2ZDk2MTkxIn0sImVtYWlsIjoiYWJpZDQ1OTgxQGdtYWlsLmNvbSIsIm5hbWUiOiJhYmR1bCIsInJvbGVPbSI6IjI0NDg1YTA1MDEiLCJhY2Nlc3NDb2RlIjoiZUpjRHRUMiIsImNsaWVudElEIjoiYjM4OTE5NmItMzZiNy00ZjNlLTk2YWEtMGMwMDQ2ZDk2MTkxIn0.dummy"

def Log(stack, level, package, message):

    url = ""

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    data = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    print(response.json())