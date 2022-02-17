from cv2 import cv2
import cvzone

def main():
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    overlay_option = input('Which Overlay do you want to show?')
    if overlay_option == 'sunglass':
        overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
    elif overlay_option == 'star':
        overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
    elif overlay_option == 'cool':
        overlay = cv2.imread('cool.png', cv2.IMREAD_UNCHANGED)
    elif overlay_option == 'pirate':
        overlay = cv2.imread('pirate.png', cv2.IMREAD_UNCHANGED)
    elif overlay_option == 'native':
        overlay = cv2.imread('native.png', cv2.IMREAD_UNCHANGED)
    else:
        print('The overlay you want to use doesnt exist')


    while True:
        _, frame = cap.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            overlay_resize = cv2.resize(overlay, (w, h))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
        cv2.imshow('Face Filter', frame)
        if cv2.waitKey(10) == ord('q'):
            break


if __name__ == '__main__':
    main()
