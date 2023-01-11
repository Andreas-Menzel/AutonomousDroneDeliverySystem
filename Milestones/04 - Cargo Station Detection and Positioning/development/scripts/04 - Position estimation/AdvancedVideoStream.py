from imutils.video import VideoStream, FileVideoStream
import time
import threading
from pathlib import Path
import sys

# Bug: stream will wait until queue is filled
# Detect end of video


class AdvancedVideoStream:
    fps = 30
    #resolution = (1920, 1080)

    video_source = Path('/dev/video0')
    stream_type = None
    source_is_file = False

    frames = []
    frames_count = 0
    keep_all_frames = False

    frames_queue = []
    frames_queue_size = 64

    video_stream = None
    time_stream_started = 0
    stream_started = False
    stream_active = False

    update_thread = None
    

    def __init__(self, src = '/dev/video0', fps = None, keep_all_frames = False):
        self.video_source = Path(src)

        # Try to guess stream type
        if src.startswith('/dev/'):
            print('[AVS] Detecting video source as device.')
            self.stream_type = 'device'
            self.frames_queue_size = 1
        elif self.video_source.exists() and self.video_source.is_file():
            print('[AVS] Detecting video source as file.')
            self.stream_type = 'file'
        elif self.video_source.exists() and self.video_source.is_dir():
            print('[AVS] Detecting video source as directory.')
            self.stream_type = 'directory'
        else:
            print('[AVS] Error: Video source unknown.')
            sys.exit(1)
        
        if fps is None:
            if self.stream_type == 'device':
                # Set default
                self.fps = 30
                print(f'[AVS] Setting default of {self.fps} fps for the device.')
            elif self.stream_type == 'video':
                # Get from video or set default
                # TODO
                self.fps = 30
                print(f'[AVS] Got {self.fps} fps from video file.')
            elif self.stream_type == 'directory':
                # Set default
                self.fps = 30
                print(f'[AVS] Setting default of {self.fps} fps for the "directory video".')
        else:
            self.fps = fps
        
        self.keep_all_frames = keep_all_frames

        if self.stream_type == 'device':
            self.video_stream = VideoStream(str(self.video_source.absolute()))
        elif self.stream_type == 'file':
            self.video_stream = FileVideoStream(str(self.video_source.absolute()))
        elif self.stream_type == 'directory':
            pass
            #self.video_stream = DirectoryVideoStream(self.video_source)
    

    def start(self, block = True):
        self.video_stream.start()

        self.stream_started = True
        self.time_stream_started = time.time() - (1 / self.fps)
        self.update_thread = threading.Thread(target=self._active_update).start()

        # TODO: What if block is false?
        if block:
            print('[AVS] Waiting for first frame...', end='')
            while self.frames_count == 0:
                time.sleep(0.5)
                print('.', end='', flush=True)
            print('')
        
        self.stream_active = True
        self.time_stream_started = time.time()


    def stop(self):
        self.stream_started = False
        self.stream_active = False
        self.video_stream.stop()

    
    def _active_update(self):
        while True:
            if not self.stream_active and not self.stream_started:
                break

            self._fill_queue()
            self._update_frame()

            if self.stream_active \
                    and len(self.frames_queue) >= self.frames_queue_size \
                    and (((time.time() - self.time_stream_started) * self.fps) - self.frames_count) < 0:
                # Calculate time to next frame
                sleep_time = (self.time_stream_started + ((self.frames_count + 1) / self.fps)) - time.time()
                if sleep_time > 0:
                    time.sleep(sleep_time)
                else:
                    print(f'ERROR - sleep_time <= 0!: {sleep_time}')
            
            if not self.stream_active:
                # Stream not active yet.
                time.sleep(0.1)


    def _fill_queue(self):
        if len(self.frames_queue) < self.frames_queue_size:
            new_frame = None

            if self.stream_type == 'device':
                new_frame = self.video_stream.read()
            elif self.stream_type == 'file':
                new_frame = self.video_stream.read()
            elif self.stream_type == 'directory':
                new_frame = self.video_stream.read()
            
            if not new_frame is None:
                self.frames_queue.append(new_frame)


    def _update_frame(self):
        frames_behind = ((time.time() - self.time_stream_started) * self.fps) - self.frames_count

        if self.stream_active and frames_behind > 5:
            print(f'[AVS] WARNING: Can\'t keep up: {int(frames_behind)} frames behind.')

        if not self.stream_active or frames_behind > 0:
            if not self.keep_all_frames:
                self.frames = []
            
            if len(self.frames_queue) > 0:
                new_frame = self.frames_queue.pop(0)
                self.frames.append(new_frame)
                self.frames_count = self.frames_count + 1


    def get_frame(self):
        if len(self.frames) > 0:
            return self.frames[-1]
        else:
            return None
    

    def is_active(self):
        return self.stream_active
