import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key , Controller

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 420)

detector = HandDetector(detectionCon = 0.7 , maxHands = 1)

keyboard = Controller()
while True:
    _, img = cap.read()
    hands , img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0,0,0,0,0] :
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif fingers[1] == 1:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        elif fingers == [1,1,1,1,1] :
            keyboard.press(Key.down)
            keyboard.release(Key.down)
    else :
        keyboard.release(Key.down)
        keyboard.release(Key.enter)
    cv2.imshow("...Manoj..." , img)
    if cv2.waitKey(1) == ord("q"):
        break
