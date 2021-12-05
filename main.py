from datetime import datetime, timedelta
import requests
import winsound
import time

USER_COOKIE = 'CBR_COOKIE_HIER'
GEKOZEN_LOCATIE = '10-02-4'
GEKOZEN_DATUM = '01-02-2021'

while True:

    # Ververs de cookie (zodat deze niet ongeldig wordt en we de code 24/7 kunnen draaien)
    refresh_req = requests.get('https://www.cbr.nl/nl/mijncbr/session-refresh.htm', headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Sec-GPC': '1', 'Referer': 'https://www.cbr.nl/nl/mijncbr/reserveren.htm', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie': f'JSESSIONID={USER_COOKIE}'}, verify = False, proxies = None)
   
    req = requests.get(
        url = f'https://www.cbr.nl/web/business/coordinator/application/reservation/stage/getavailablecapacity?product_code=BTH&location={GEKOZEN_LOCATIE}&selected_date={GEKOZEN_DATUM}&hash=12345678&t-id=',
        headers = {'Accept': 'application/json', 'Cache-Control': 'no-cache,no-store,must-revalidate,max-age=-1,private', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Expires': '-1', 'Sec-GPC': '1', 'Referer': 'https://www.cbr.nl/nl/mijncbr/reserveren.htm', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie': f'JSESSIONID={USER_COOKIE}'},
        verify = False,
        proxies = None
    ).json()

    datums = req["data"]["nestedValueObjects"]
    if datums != []:
        for datum in datums:

            unixBegin = int(datum["valueObjectInformation"]["entry"][5]["value"]) / 1000
            timeObj = datetime.utcfromtimestamp(unixBegin) + timedelta(hours=2)
            formatTime = timeObj.strftime("%Y-%m-%d %H:%M:%S")

            print(f"CBR THEORIE AUTO_EXAMEN SPOT -> [{formatTime}]")
            winsound.Beep(432, 300)

    time.sleep(20)
