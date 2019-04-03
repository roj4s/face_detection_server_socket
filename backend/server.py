from flask import Flask
from flask_socketio import SocketIO
import face_detector as fd
import cv2
import numpy as np
import tempfile

detector = fd.FaceDetector()

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('detect')
def handle_message(data):
    print("Got new image ...")
    #try:
    img_data = np.fromstring(data['data'], dtype=np.uint8)
    img = cv2.imdecode(img_data, 1)
    temp_file = tempfile.NamedTemporaryFile()
    img_path = "{}.jpg".format(temp_file.name)
    cv2.imwrite(img_path, img)
    '''
    # Uncomment to see frontend sent image
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    faces = detector.get_faces(img_path)
    for face in faces:
        bb = face.bounding_box
        socketio.emit('detected', {'x': bb.x, 'y': bb.y, 'w':
                               bb.w, 'h': bb.h})
    temp_file.close()

    #except Exception as e:
    #    print("Error: {}".format(str(e)))

if __name__ == '__main__':
    print("Starting server ...")
    socketio.run(app)
