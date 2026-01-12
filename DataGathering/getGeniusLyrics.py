import asyncio
import requests

async def getSongs(songID):
    AToken = "OX2CI4He1koN9YH1pporxZkTGkD5OxDV-3QMbgoqe3Xc8PlyiURq7Oskx9DYBsPX"
    getSongs = requests.get(f"https://api.genius.com/songs/{songID}", headers={'Authorization': f"Bearer {AToken}"})
    print(f"Status code:\n{getSongs.status_code}\n")
    print(f"Raw Text:\n{getSongs.text}\n")
    print(f"Raw JSON:\n{getSongs.json}\n")

if __name__ == "__main__":
    songID = 12345
    asyncio.run(getSongs(songID))

    