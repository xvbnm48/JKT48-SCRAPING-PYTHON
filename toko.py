import requests

url = 'https://tokopedia.com'
def get_data(url):
    r = requests.get(url)
    print(r.status_code)
    # soup = BeautifulSoup(r.text, 'html.parser')
    return r.text

if __name__ == '__main__':
    data = get_data(url)
    # final_Data = parse(data)
    # output(final_Data)