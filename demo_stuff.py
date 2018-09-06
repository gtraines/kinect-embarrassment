import freenect
import cv2
from kin_emb import frame_convert2


def display_cam_stream(cam_idx):
    cap = cv2.VideoCapture(cam_idx)

    while True:
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)

        except Exception:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])


def display_kinect_stream():

    cv2.namedWindow('Depth')

    try:

        print('Press ESC in window to stop')

        while 1:
            cv2.imshow('Depth', get_depth())
            if cv2.waitKey(10) == 27:
                break

    except Exception as ex:
        print(ex)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    display_kinect_stream()
