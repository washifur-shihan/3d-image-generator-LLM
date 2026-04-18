# 3D Image Generator with LLM

**Live Demo:** https://threed-image-generator-llm.onrender.com/docs

## Description

A FastAPI-based web application that generates 3D images using Large Language Models (LLMs). This project leverages the power of LLMs to understand image descriptions and convert them into stunning 3D visual outputs. The application provides a simple REST API for seamless integration with frontend applications or other services.

## Features

- 🚀 Fast and scalable REST API built with FastAPI
- 🤖 LLM-powered image generation from text descriptions
- 🎨 3D image rendering and processing
- 📚 Interactive API documentation (Swagger UI)
- 🔧 Production-ready with Render deployment configuration

## Tools & Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Python 3.x** - Programming language
- **LLM Integration** - Language models for understanding and generating image descriptions
- **Pillow (PIL)** - Python Imaging Library for image processing
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI web server
- **Render** - Cloud platform for deployment

## Project Structure

```
project/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── llm_service.py       # LLM integration service
│   ├── image_service.py     # Image generation and processing
│   └── schemas.py           # Pydantic request/response schemas
├── requirements.txt         # Python dependencies
├── render.yaml             # Render deployment configuration
├── .env                    # Environment variables (not tracked in git)
└── .gitignore             # Git ignore rules
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd generate-3d-image-LLM
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`  
API documentation: `http://localhost:8000/docs`

## Usage

Access the interactive API documentation at the `/docs` endpoint to explore and test all available endpoints.

## Deployment

This project is configured for deployment on Render. Push your changes to the repository, and Render will automatically build and deploy the application.

## License

MIT License - Feel free to use this project for your own purposes.
