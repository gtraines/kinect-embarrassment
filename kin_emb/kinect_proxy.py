import freenect
from . import frame_convert2


def is_kinect_available():
    context = freenect.init()
    return freenect.num_devices(context) > 0


def get_depth():
    return frame_convert2.pretty_depth(freenect.sync_get_depth()[0])


def get_video():
    return freenect.sync_get_video()[0]
