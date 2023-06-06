# fastapi->module
# FastAPI, Form, UploadFile, File->class
from fastapi import FastAPI, Form, UploadFile, File
# uvicorn is like a library that runs fastapi project
import uvicorn
from extractor import extract
# to generate unique identifier
import uuid
import os

# app->FastAPI() object
app = FastAPI()

# api endpoint
@app.post("/extract_from_doc")
def extract_from_doc(

        # file_format->parameter
        # parameter should be of the type 'str'
        # str->type hinting/data validation
        # = Form(...)->default value
        file_format: str = Form(...),
        file: UploadFile = File(...),
):
    # temporarily place the content of the file uploaded by the client in contents object
    contents = file.file.read()

    # each time a client uploads the file to the server a new file gets created on the ser
    # ver in Uploads directory
    file_path = "../Uploads/" + str(uuid.uuid4()) + ".pdf"

    # write the contents of the 'content' object into newly created file
    with open(file_path, "wb") as f:
        f.write(contents)

    # extracting the field data through extract()
    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }
    # once you have data extracted ,file is no more needed on the server

    # delete the file
    if os.path.exists(file_path):
        os.remove(file_path)

    # return the data to the ui
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)