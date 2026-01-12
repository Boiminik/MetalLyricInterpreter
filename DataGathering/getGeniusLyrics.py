import asyncio
import requests

async def getSongs():
    client_id = "V6x81QBlfEDMKzRQJsYHr-Ae9xFv3bMCF6ulqnhjSjoYttwpI7O8cZVQFjhqn_cJ"
    redirect_uri = "http://localhost"
    scope = "me"
    state = ""
    response_type = "code"
    response = requests.get(f"https://api.genius.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}&response_type={response_type}")
    print(response.status_code)

if __name__ == "__main__":
    asyncio.run(getSongs())