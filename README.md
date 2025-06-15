# ✨ Ultimate Image Editor

A full-stack AI-powered image editing web app that lets users **remove backgrounds**, **enhance images**, and **download the result** — all within a beautiful drag-and-drop interface. Built using **FastAPI**, **Tailwind CSS**, and **Rembg**, it's optimized for speed, style, and simplicity.

---

## 🔥 Features

- 🎨 Remove background with AI (Rembg)
- 🪄 Enhance image colors with a custom factor
- 🖼 Live image preview before uploading
- 📥 Drag & Drop file upload support
- 🌈 Stylish Glassmorphism UI (Tailwind + Inter font)
- ✅ Fully responsive & mobile-friendly
- 🧠 Smart file handling and error feedback

---

## 🚀 Demo

Live version (if hosted):  
🔗 [https://your-live-site-url.com](https://your-live-site-url.com)

> _Replace the above URL with your Render or GitHub Pages live deployment._

![App Screenshot](https://your-screenshot-link.com/preview.png)

---

## 🛠 Technologies Used

- ⚡ FastAPI (Backend)
- 🎨 Tailwind CSS (Frontend Styling)
- 🧠 Rembg (AI Background Removal)
- 🖼 Pillow (Image Processing/Enhancement)
- 📦 Python-Multipart (for file uploads)
- 🧪 Jinja2 (HTML Templating)
- ☁️ Render (Deployment Platform)

---

## 💻 Installation

To run the project locally:

```bash
git clone https://github.com/your-username/image-editor.git
cd image-editor
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open your browser at:

```
http://127.0.0.1:8000
```

---

## 🔧 Usage

1. Drag & drop or upload your image.
2. Select one or both options:
   - ✅ Background Removal
   - 🎨 Color Enhancement (adjust factor from 1.0–2.0)
3. Click **Upload & Process**.
4. Download the final image once processed.

---

## 🌍 Deployment (Render - Free Hosting)

Steps to deploy on **[Render](https://render.com)**:

1. Create a new **Web Service**.
2. Connect your GitHub repository.
3. Add the following as your **Start Command**:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

4. Add environment variable:
```bash
PORT = 10000
```

5. Keep `main.py`, `requirements.txt`, and folders like `templates/` and `static/` at the root.

---

## 📁 Folder Structure

```
├── main.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── (optional assets)
├── processed/
│   └── processed images
```

---

## 📌 To-Do / Future Plans

- 🧑‍🎨 Add crop, rotate, and flip options
- 🎚️ Add preset filters (grayscale, sepia, etc.)
- 📁 User login + history
- 🌐 Multi-language support
- ☁️ Upload to cloud storage (e.g., Firebase)

---

## 🤝 Contributing

Contributions are always welcome!  
If you want to improve UI, performance, or features, feel free to open a pull request or issue.

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it for your needs.

---

## 🙏 Acknowledgements

- [Rembg by Daniel Gatis](https://github.com/danielgatis/rembg)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [Render](https://render.com)