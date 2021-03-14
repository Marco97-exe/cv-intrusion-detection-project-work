import numpy as np
import cv2

from intrusiondetection.parameters import ParameterList
from intrusiondetection.video import Video
from intrusiondetection.displayable import Background
from intrusiondetection.utility import default_parameters


def execute_intrusion_detection():
    params = default_parameters()
    initial_background = Background(
        input_video_path=params.input_video, 
        interpolation=params.initial_background_interpolation, 
        frames_n=params.initial_background_frames
    )

    video = Video(params.input_video)
    video.intrusion_detection(params, initial_background)

if __name__ == "__main__":
    execute_intrusion_detection()
