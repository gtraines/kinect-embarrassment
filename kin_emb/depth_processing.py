import freenect
import numpy as np


def pretty_depth(depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        A numpy array that has been processed whos datatype is unspecified
    """
    np.clip(depth, 0, 2**10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth


def get_depth_in_threshhold(lower, upper):
    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth > lower, depth < upper)
    depth = depth.astype(np.uint8)
    return depth
