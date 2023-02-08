import requests
from bs4 import BeautifulSoup
import json
r = requests.Session()

def main():
    req = r.request('GET', 'https://jkt48.com/member/list')
    if bool(req.status_code == 200):
        bs = BeautifulSoup(req.text, 'html.parser')
        members = []
        names = bs.find_all('p', class_='entry-member__name')
        # for name in names:
        #     print(name.text)
        for i in bs.select('.col-4 > .entry-member'):
            # print(f"Link: jkt48.com{i.a.img.get('src')}")
            # print(f"Name: {i.a.img.get('alt')}")
            # print(i.a.p.entry-member__name.text)
            # print(name)
            member = {
                'name': i.a.img.get('alt'),
                'link-foto': f"jkt48.com{i.a.img.get('src')}",
                'link-profile': f"jkt48.com{i.a.get('href')}",
                # 'name-tanpa-spasi': name.text,
            }
            members.append(member)
        with open('members.json', 'w') as f:
            json.dump(members, f, indent=4)
        print(json.dumps(members, indent=4))

if __name__ == '__main__':
    main()