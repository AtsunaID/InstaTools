from flask import Flask, request, jsonify
from flask_cors import CORS
import requests , json, random ,re

app = Flask(__name__)
CORS(app)

def check_instagram_account(username):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'dpr': '1.2000000000000002',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.196", "Google Chrome";v="132.0.6834.196"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'viewport-width': '864',
    }
    cok = 'datr=bZKDZxzywjeZPcsGTGP4GNl-; ig_did=0D69018E-D3A7-4E8C-B99C-E27901FE98DB; mid=Z4OSbQABAAEN5LKUbKhosr0_xAp7; ps_l=1; ps_n=1; ig_nrcb=1; dpr=2; wd=360x634; csrftoken=QLjzDC52Qo8SJsr2bcDnCcxjNGYiGraD; ds_user_id=62720478966; sessionid=62720478966%3AH4PC5vNISkHby5%3A8%3AAYe1PltE1brm2Irt0N1vPc5uLBWIqxHQl1VJiVnZGQ; rur="EAG\05462720478966\0541770700189:01f73363a744b206569748784bae58387e4fe961b458e903b1fa0c9f5d666e1c2023f7bc"'
    url = f'https://www.instagram.com/{username}/'
    
    try:
        response = requests.get(url, headers=headers)
        if "username" in str(response.text):
          user = re.search('"params":{"query":{"username":"(.*?)"}}',str(response.text)).group(1)
          return {"Username": user}
        else:
          return {"Username": user, "status": "dead"}
    except Exception as e:
        return {"Username": username, "status": "Error", "message": str(e)}

@app.route("/Live", methods=["GET"])
def checker():
    username = request.args.get("username")
    
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400
    
    result = check_instagram_account(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
