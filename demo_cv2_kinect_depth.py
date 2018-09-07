"""Sweeps throught the depth image showing 100 range at a time"""
from kin_emb.depth_processing import get_depth_in_threshhold
from kin_emb import kinect_proxy
import cv2
import matplotlib.pyplot as pplot
import signal
import time


def display_threshhold(lower, upper):
    depth = get_depth_in_threshhold(lower, upper)
    cv2.imshow('Depth', depth)
    cv2.waitKey(10)


def sweep_threshhold(lower, upper, max_upper):

    cv2.namedWindow('Depth')

    while upper < max_upper:
        print('%d < depth < %d' % (lower, upper))
        display_threshhold(lower, upper)
        time.sleep(.1)
        lower += 20
        upper += 20


def display_depth_plot():
    keep_running = True

    def handler(signum, frame):
        """Sets up the kill handler, catches SIGINT"""
        global keep_running
        print("SIGINT!!!")
        keep_running = False

    # Register signal interrupt handler
    signal.signal(signal.SIGINT, handler)

    pplot.ion()
    pplot.gray()
    pplot.figure(1)
    image_depth = pplot.imshow(kinect_proxy.get_depth(), interpolation='nearest', animated=True)
    print('Press Ctrl-C in terminal to stop')

    while keep_running:
        pplot.figure(1)
        image_depth.set_data(kinect_proxy.get_depth())
        pplot.draw_all()
        pplot.waitforbuttonpress(0.1)


if __name__ == '__main__':
    display_depth_plot()
