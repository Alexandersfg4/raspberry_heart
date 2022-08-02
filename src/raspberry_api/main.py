import logging

from fastapi import FastAPI

from src.raspberry_api.config import settings
from src.raspberry_api.converters import VideoConverter
from src.raspberry_api.services import Service

app = FastAPI()
converter = VideoConverter()
media = Service(settings.MediaServer.media_server)
logger = logging.getLogger(__name__)


@app.get("/media/restart")
def restart_media_server():
    status = media.restart()
    if status.returncode == 1:
        return {"status": status.stderr}
    return {"status": "Service has been restarted"}


@app.get("/convert_files")
def convert_files():
    files = converter.convert_files()
    return {"status": "All files have been converted",
            "convertedFiles": files}
