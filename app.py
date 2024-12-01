from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# POST Method: Set Cookies
@app.route('/setcookies', methods=['POST'])
def set_cookies():
    # Get data from the POST request
    user_data = request.get_json()
    username = user_data.get('username', '')
    age = user_data.get('age', '')

    # Create response and set cookies
    resp = make_response(jsonify({"message": "Cookies are set!"}))
    resp.set_cookie('username', username)
    resp.set_cookie('age', str(age))

    return resp


# GET Method: Get Cookies
@app.route('/getcookies', methods=['GET'])
def get_cookies():
    # Get cookies from the request
    username = request.cookies.get('username')
    age = request.cookies.get('age')

    if username and age:
        return jsonify({
            'username': username,
            'age': age
        })
    else:
        return jsonify({"message": "Cookies not found!"}), 404


if __name__ == '__main__':
    app.run(debug=True)
