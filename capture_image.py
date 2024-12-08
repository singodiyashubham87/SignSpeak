import cv2
import os
import time
import uuid

PATH='Data/images'

labels = ['yes', 'no', 'hello', 'thanks', 'help', 'quiet']

num_of_images = 15

for label in labels:
    os.makedirs(os.path.join(PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(num_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(PATH, label, label + '.{}.jpg'.format(str(uuid.uuid4())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()