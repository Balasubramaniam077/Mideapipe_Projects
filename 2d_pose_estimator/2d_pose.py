import cv2
import mediapipe as mp 
import time


mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose 
pose = mpPose.Pose()


cap = cv2.VideoCapture(0)
PTime = 0
cap.open(0)
while (cap.isOpened()):
    success, img = cap.read()
    img = resized = cv2.resize (img, (800,800))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (128,0,128), cv2.FILLED)


    cTime = time.perf_counter()
    fps = 1/ (cTime - PTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50),cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
