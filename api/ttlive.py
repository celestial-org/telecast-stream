import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json

def ttl(url):
    response = requests.get(url, stream=True, headers={"user-agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"})
    soup = BeautifulSoup(response.text, 'html.parser')
    state = soup.find('script', id='SIGI_STATE')
    json_ = json.loads(unquote(state.string))
    json_ = json_["LiveRoomMobile"]
    json_ = json_["userInfo"]["liveRoom"]["streamData"]["pull_data"]["stream_data"]
    json_ = json.loads(json_)["data"]["origin"]["main"]
    return json_["hls"]