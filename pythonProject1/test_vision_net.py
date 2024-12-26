import uvicorn
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from db import get_session

app = FastAPI()

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 MB

@app.post('/upload/')
async def upload_file(file: UploadFile = File(...), db=Depends(get_session)):
    try:
        content = await file.read()
        file_size = len(content)
        if file_size > MAX_FILE_SIZE:
            raise HTTPException(status_code=404, detail='File too large')

        return JSONResponse({"file_size": file_size}, status_code= 201)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def home():
    return RedirectResponse("http://127.0.0.1:8000/docs", status_code=status.HTTP_303_SEE_OTHER)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


