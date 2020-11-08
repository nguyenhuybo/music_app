from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import StreamingResponse
import shutil
from typing import List

some_file_path = "hai.mp3"
app = FastAPI()


@app.get("/listen")
async def listen(song: str = Query(...)):
    file_like = open(song, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")


@app.post("/image")
async def image(images: List[UploadFile] = File(...)):
    for image in images:
        with open(image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    return {"filename": image.filename}
