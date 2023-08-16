import datetime,time
from flask import Blueprint, Flask, render_template, request,Response
import cv2 as cv

site = Blueprint('site', __name__, template_folder='templates')

app1 = Flask(__name__)

video_path6 =  'rtsp://104.194.11.25:554/livedemocam'
video_path7 = 'rtsp://104.194.11.25:554/livedemocam'
video_path8 = 'rtsp://104.194.11.25:554/livedemocam'
video_path9 = 'rtsp://104.194.11.25:554/livedemocam'

@app1.route('/')
def index():
    return render_template('Side_bar.html')
    
def generate_frames(video_path):
    cap = cv.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        resize = cv.resize(frame, (1000, 500))

        number_of_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv.CAP_PROP_FPS))

        f = str(fps)
        n = str(number_of_frames)
        d = str(number_of_frames/fps)
        # rect = cv
        # .rectangle(frame, (50, 100), (150, 200), (255, 255, 255), 2)
        font = cv.FONT_HERSHEY_SIMPLEX
        # text = "Width:" + str(cap.get(3)) + " Heigth:" + str(cap.get(4))
        date = str(datetime.datetime.now())

        t = "Total Frames:" + " " + n + "  " + \
            "Frame per second:" + " " + f + "  " + "duration:" + d
        frame = cv.putText(resize, t, (20, 50), font, 1,
                           (0, 0, 128), 2, cv.LINE_AA)
        frame = cv.putText(frame, date, (20, 100), font,
                           1, (198, 249, 1), 2, cv.LINE_AA)

        ret, frame = cv.imencode('.jpg', frame)

        frame_bytes = frame.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        

          
@app1.route('/video0')
def video5():
    return Response(generate_frames(video_path6), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video1')
def video6():
    return Response(generate_frames(video_path7), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video2')
def video7():
    return Response(generate_frames(video_path8), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video3')
def video8():
    return Response(generate_frames(video_path9), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app1.run(debug=True, host="127.0.0.1", port=2001)
    

