# main.py
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageEnhance
from rembg import remove
import os
from io import BytesIO

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

os.makedirs("processed", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process/", response_class=HTMLResponse)
async def process_image(
    request: Request,
    file: UploadFile = File(...),
    enhance_factor: float = Form(1.0),
    remove_bg: bool = Form(False),
    apply_enhance: bool = Form(False)
):
    try:
        img_data = await file.read()
        img = Image.open(BytesIO(img_data)).convert("RGBA")

        if remove_bg:
            img = Image.open(BytesIO(remove(img_data))).convert("RGBA")

        if apply_enhance:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(enhance_factor)

        # Save as PNG to preserve transparency
        output_filename = f"processed_{os.path.splitext(file.filename)[0]}.png"
        output_path = os.path.join("processed", output_filename)
        img.save(output_path)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "image_url": f"/download/{output_filename}"
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })


@app.get("/download/{filename}", response_class=FileResponse)
async def download_image(filename: str):
    file_path = os.path.join("processed", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/png", filename=filename)
    return {"error": "File not found"}