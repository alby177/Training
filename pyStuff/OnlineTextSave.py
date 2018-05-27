import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('Something went wrong :', exc)
playFile = open('RomeoAndJuliet2.txt', 'wb')
for i in res.iter_content(len(res.text)):
    playFile.write(i)
playFile.close()