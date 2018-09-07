import freenect
import cv2
from kin_emb import frame_convert2


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
