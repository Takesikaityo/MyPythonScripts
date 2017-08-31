import requests,datetime

headers = {
    'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.4; AWOS-0701 Build/KTU84P)',
    }

while True:
    r = requests.get("https://m.youtube.com/channel/UCaminwG9MTO4sLYeC3s6udA?ajax=1",headers=headers)
    pos = r.text.find('"runs": [{"text": "2,')
    dt = datetime.datetime.now()
    print str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second)+" > " + r.text[pos:pos+28].replace('"runs": [{"text": "','')
