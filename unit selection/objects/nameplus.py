import re
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def StudentName(Name):
    if re.match("^[آ-ی]+$", Name):
        return("نام ذخیره شد")
    else:
        return("نام وارد شده نامعتبر است، لطفا نام با حروف فارسی وارد کنید.")

Name = "محمدd"

