import cv2
import time
import math

vid = cv2.VideoCapture("footvolleyball.mp4")

tracker = cv2.TrackerCSRT_create()
returned, img = vid.read()
bbox = cv2.selectROI("Tracking", img, False)

tracker.init(img, bbox)
print(bbox)

def draw_box(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (0, 255, 0), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)


while True:
    check, img = vid.read()
    success, bbox = tracker.update(img)

    if success:
        draw_box(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        print("Closing")
        break

vid.release()
cv2.destroyAllWindows()