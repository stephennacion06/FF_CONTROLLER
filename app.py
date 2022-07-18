from flask import Flask,render_template, request, redirect, url_for, Response
import pickle
 
app = Flask(__name__)

initial_control = [0,0]

with open('controls.pkl', 'rb') as f:
    mynewlist = pickle.load(f)


@app.route('/')
def helloHandler():
    return render_template('remote_control.html')

@app.route('/left_side')
def left_side():
    print("left side")
    return 'true'

@app.route('/right_side')
def right_side():
    global speed, angle
    data1 = "RIGHT"
    angle += 1
    if angle > 90:
        angle = 90
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/up_side')
def up_side():
    global speed, angle
    data1 = "FORWARD"
    speed = 4
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/down_side')
def down_side():
    global speed, angle
    speed = -4
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/stop')
def stop():
    global speed, angle
    speed = 0
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'
 
app.run(host='0.0.0.0', port= 8090)