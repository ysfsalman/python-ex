'''
source : http://ubuntuhandbook.org/index.php/2015/01/use-android-phone-as-wireless-webcam/
source :https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
'''
import cv2


#cap = cv2.VideoCapture('http://192.168.1.16:4747/video')
cap = cv2.VideoCapture('http://192.168.1.16:4747/video')


while True:
    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
