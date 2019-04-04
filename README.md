# Web Face Detection Demo via Sockets

End to end face detection web application with communication via socket. This demo employs the python package
face-detector (pip install face-detector, https://github.com/roj4s/face\_detector).

## How to deploy

In order for this demo to work properly, backend server should be running and frontend open in a webcam supporting browser. Once both ends are running, frames from the webcam are exhibited in the browser along with a yellow bounding box around the face of the person standing in front of the webcam.

Frontend can be executed just by opening index.html in any browser with webcam
support. Also a Dockerfile is included in frontend folder which can be used to
build a docker image running nginx web server, in order to provide frontend
through network. Frontend code (index.html) must be edited (line 39) to specify
backend server url and port, it is not necessary if you are running this demo
locally in your pc (i.e

```console
    foo@bar:~/demo/frontend$ docker build -t face_detection_demo .
    foo@bar:~/demo/frontend$ docker run --name demo -p 8080:80 -d face_detection_demo
```

Fig 1 shows a screenshot of the demo running.

<div style="text-align:center">
<img src="https://raw.githubusercontent.com/roj4s/face_detection_server_socket/master/sample.png" />
<p>Fig. 1 Screenshot of demo running in Google Chrome browser.</p>
</div>


