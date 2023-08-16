import datetime
import time
from flask import Flask, render_template,Response,request
import cv2 as cv


app1 = Flask(__name__)

video_path1 = 'rtsp://104.194.11.25:554/livedemocam'
video_path2 = 'rtsp://104.194.11.25:554/livedemocam'
video_path3 = 'rtsp://104.194.11.25:554/livedemocam'
video_path4 = 'rtsp://104.194.11.25:554/livedemocam'
video_path5 = 'rtsp://104.194.11.25:554/livedemocam'

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
def video0():
    return Response(generate_frames(video_path1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video1')
def video1():
    return Response(generate_frames(video_path2), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video2')
def video2():
    return Response(generate_frames(video_path3), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video3')
def video3():
    return Response(generate_frames(video_path4), mimetype='multipart/x-mixed-replace; boundary=frame')

@app1.route('/video4')
def video4():
    return Response(generate_frames(video_path5), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app1.run(debug=True, host="127.0.0.1", port=2000)
