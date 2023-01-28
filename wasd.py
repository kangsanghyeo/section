import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

ㅇㅇ = [731, 226, 227, 230, 732, 283, 229, 228]
for date in range(28, 27, -1):
    for section in ㅇㅇ:
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2={0}&sid1=105&date=202301{1}'.format(section, date)
        site = requests.get(url, headers=headers)
        source_data = site.text

        count = source_data.count('<dt>')

        for i in range(count):
            pos1 = source_data.find('<dt>')+ len('<dt>')
            source_data = source_data[pos1:]

            pos2 = source_data.find('">')+ len('">')
            source_data = source_data[pos2:]
            pos3 = source_data.find('</a>')
            extract_data = source_data[: pos3].strip()
                                 
            source_data = source_data[pos3+1:]
            print(i+1, extract_data)

