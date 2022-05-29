from flask import Flask, request

app = Flask('__main__')

"""


"""
device = {
    "code": "11112222",
    "descrip": "Inclination for the sensor",
    "value": 14
}

#Save an user
@app.route('/users', methods=['POST'])
def save_users():
    user = request.json
    print(user)
    return user

#Get devices
@app.route('/devices', methods=['GET'])
def go_home():
    print(device)
    return device

# Save a device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')