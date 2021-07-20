import requests
import uuid
import time
uid = str(uuid.uuid4())

print('''
░██████╗███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗██╗██████╗░
██╔════╝██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║██║██╔══██╗
╚█████╗░█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║██║██║░░██║
░╚═══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║██║██║░░██║
██████╔╝███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║██║██████╔╝
╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚═════╝░''')

print('Follow me on instagram @mostcode')

user = input(f"[+] Enter username: ")
Pass = input(f"[+] Enter password: ")




Login_url = 'https://i.instagram.com/api/v1/accounts/login/'
Login_head = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Host': 'i.instagram.com'
            }
Login_data = {
                '_uuid': uid,
                'username': user,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(Pass),
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_count': '0'
            }
LOG = requests.post(Login_url, data=Login_data, headers=Login_head, allow_redirects=True)

if LOG.text.find("is_private") >= 0:
    print(f"[+] Login Successfully To {user}")
    LOG.headers.update({'X-CSRFToken': LOG.cookies['csrftoken']})
    sid = LOG.cookies['sessionid']
    print(f"[+] Sessionid: {sid}")

    urIN = 'https://www.instagram.com/accounts/edit/?__a=1'

    hedIN = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; ds_user_id=45872034997; shbid=6144; csrftoken=uGeaBdGt8EF51aBV8x1MHP2aizo1Boye; rur=RVA; sessionid=' + sid,
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}

    datIN = {
        '__a': '1'}
    info = requests.get(urIN, headers=hedIN, data=datIN)
    name = str(info.json()['form_data']['first_name'])
    ext = str(info.json()['form_data']['external_url'])
    eml = str(info.json()['form_data']['email'])
    bio = str(info.json()['form_data']['biography'])
    num = str(info.json()['form_data']['phone_number'])
    print(f'[+] Name: {name}')
    print(f'[+] Email: {eml}')
    print(f'[+] Number: {num}')
    print('[+] Please write down or save information')
    print('[+] Thank you for using my tool')
    time.sleep(1000)
elif LOG.text.find("invalid_credentials") >= 0:
    print(f" Wrong Password {user} ")
elif LOG.text.find('two_factor_required') >= 0:
    print(f" Your Account Have Two Factor. Chang User.., ")
else:
    print(f"TRY LATER")
