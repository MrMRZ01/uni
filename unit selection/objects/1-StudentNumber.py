from fastapi import FastAPI

app = FastAPI()

@app.get('/home/{StudentNumber}')
def StudentNumber(StudentNumber):
    year = int(str(StudentNumber)[:3])
    constant_part = str(StudentNumber)[3:9]
    index = int(str(StudentNumber)[9:])
    len1 = int(len(str(StudentNumber)))


    if len1 < 11 or len1 > 11:
        return "شماره دانشجویی باید 11 رقم باشد"
    if constant_part != "114150":
        return "قسمت ثابت نادرست است"
    if year >= 403 or year <= 399:
        return " سال وارد شده نادرست است"
    if index < 1 or index > 99:
        return "اندیس نادرست است"


    return f"سال: {year+1000}, قسمت ثابت: {constant_part}, اندیس: {index}"

