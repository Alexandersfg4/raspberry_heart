import os
import subprocess

import ffmpeg

from src.raspberry_api.config import settings


class VideoConverter:
    def __init__(self):
        self.directory = settings.MediaServer.video_files
        self.is_not_supported = settings.MediaServer.is_not_supported
        self.convert_to = settings.MediaServer.to_be_converted

    def convert_files(self):
        not_converted_files = self.return_else_converted
        converted_files = []
        for file in not_converted_files:
            stream = ffmpeg.input(file)
            stream = ffmpeg.output(stream, file.replace(file.split('.')[-1], self.convert_to))
            ffmpeg.run(stream)
            converted_files.append(file)
            subprocess.run([settings.Cmd.rm, file])
        return converted_files

    @property
    def return_else_converted(self):
        files = self._files
        for file in files:
            if file.endswith(self.is_not_supported.value) and\
                    file.replace(file.split('.')[-1], self.convert_to) not in files:
                files.append(file)
        return files

    @property
    def _files(self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.directory):
            for file in f:
                files.append(os.path.join(r, file))
        return files
