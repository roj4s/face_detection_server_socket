from flask import Flask
from flask_socketio import SocketIO
from face_recognition_manager.face_alignment.mtcnn import FaceAlignmentMTCNN
import cv2
import numpy as np

face_aligner= FaceAlignmentMTCNN("/home/neo/dev/face_recognition/face_recognition_manager/data/models/mtcnn",
                     config={'gpu_memory_fraction': 0.2})

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('detect')
def handle_message(data):
    print("Got new image ...")
    try:
        img_data = np.fromstring(data['data'], dtype=np.uint8)
        img = cv2.imdecode(img_data, 1)
        '''
        # Uncomment to see frontend sent image
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
        bb = face_aligner.find_one_face(img)

        socketio.emit('detected', {'x': bb.x_float, 'y': bb.y_float, 'w':
                                   bb.w_float, 'h': bb.h_float});
    except Exception as e:
        print("Error: {}".format(str(e)))

if __name__ == '__main__':
    print("Starting server ...")
    socketio.run(app)
