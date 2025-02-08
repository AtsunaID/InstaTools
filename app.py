from flask import Flask, request, jsonify
import requests as r

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def instagram_info():
    iu = request.args.get('username')
    
    if not iu:
      return jsonify({"error": "Username is required"}), 400
    
    url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username='
    b = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
      "x-asbd-id": "129477",
      "x-csrftoken": "6ap085rbBxWc5G9deBCkBXYUXdNTMOX4",
      "x-ig-app-id": "936619743392459",
      "x-ig-www-claim": "hmac.AR0Vq4Mb4I1toglwKO8lMn8SFJ3-GYGALeriWG1p7c_BVbxt"
    }
    
    try:
      # Make the request
      response = r.get(url + iu, headers=b)
      w = response.json()
      # Check if the response has data
      if 'data' not in w:
        return jsonify({"error": "User not found or error fetching data"}), 404
      user_data = {
        "Username": w['data']['user']['username'],
      }

      return jsonify(user_data)
  
    except Exception as e:
      return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
