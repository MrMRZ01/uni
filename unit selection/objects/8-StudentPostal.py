from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentPostal}")
def StudentPostal(StudentPostal):
    postal = StudentPostal
    len1 = len(postal)

    if len1 >= 11 or len1 <= 9:
        return "تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد"
    return "کدپستی وارد شده صحیح است"