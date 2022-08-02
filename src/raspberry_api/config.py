import logging.config
from rich.logging import RichHandler
from pydantic import BaseSettings


class Settings(BaseSettings):
    class MediaServer:
        video_files = '/Users/aleksandrbortnikov/Projects/home_server'
        is_not_supported = ('avi',)
        to_be_converted = 'mp4'
        media_server = 'minidlna'

    class Cmd:
        systemctl = 'systemctl'
        rm = 'rm'


settings = Settings()
