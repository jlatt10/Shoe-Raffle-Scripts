url = 'https://thewebster.us/shop/the-10-nike-x-off-white-blazer/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

  
def main(limit):
    for i in range(1, limit):
        num = getrandbits(40)
        name = 'Jack Lattman{}'.format(num) # put your name here, don't remove the {}
        email = 'jlatt10+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'action': 'contest',
            'name': Jack Lattman, 
            'email': jlatt10@gmail.com,
            'size': '6.5', # change your size
            'group[]': 'Mens'
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(100000)
