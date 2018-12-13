import time,json,urllib2
cnt = 0
dataFile = "/home/tyler/asnGeoData/geoData.data"

with open('/home/tyler/asnGeoData/asnData.data','r') as f:
    for line in f:
        ip_address = line.strip()
        print(ip_address)
        if ip_address != "begin" or ip_address != "end":
            try:
                url = 'http://ip-api.com/json/{}?lang=en'
                url = url.format(ip_address)
                print(url)
                data = urllib2.urlopen(url).read()
                print(data)
                time.sleep(1)
                with open (dataFile,'a') as file:
                    file.write(json.dumps(data))
                    file.write('\n')
                    cnt = cnt + 1
            except IOError as e:
                print(str(e))
                break         
            except Exception as e:
                print('Error: '+ str(type(e)))
                print(str(e))

            


print('\nLooked up ' + str(cnt) + ' ip address\'s geolocation')
