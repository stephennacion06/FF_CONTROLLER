from flask import Flask,render_template, request, redirect, url_for, Response
import pickle
 
app = Flask(__name__)

initial_control = [0,0]

with open('controls.pkl', 'wb') as f:
    pickle.dump(initial_control, f)


@app.route('/')
def helloHandler():
    return render_template('remote_control.html')

@app.route('/left_side')
def left_side():
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[1] = 1

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)

    return 'true'

@app.route('/right_side')
def right_side():
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[1] = 2

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)
    return 'true'


@app.route('/up_side')
def up_side():
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[0] = 1

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)
    return 'true'


@app.route('/down_side')
def down_side():
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[0] = 2

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)
    return 'true'


@app.route('/stop')
def stop():
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[0] = 0

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)
    return 'true'

@app.route('/straight')
def straight():
    print("straight")
    with open('controls.pkl', 'rb') as f:
        controls_list = pickle.load(f)
    
    controls_list[1] = 0

    with open('controls.pkl', 'wb') as f:
        pickle.dump(controls_list, f)
    return 'true'
 
app.run(host='0.0.0.0', port= 8090)