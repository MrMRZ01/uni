from fastapi import FastAPI

app = FastAPI()

@app.get('/home/{StudentBirth}')
def StudentBirth(StudentBirth):
    year = int(str(StudentBirth)[:4])
    month = int(str(StudentBirth)[4:6])
    day = int(str(StudentBirth)[6:8])
    len1 = int(len(str(StudentBirth)))

    if len1 >= 9 or len1 <= 7:
        return "تعداد ارقام وارد شده نادرست است"
    if year >= 1500 or year <= 1250:
        return " سال وارد شده نادرست است"
    if month >= 13 or month <= 1:
        return "ماه وارد شدن نادرست است"
    if day >= 32 or day <= 0:
        return "روز وارد شده نادرست است"
    return "تاریخ تولد صحیح است"

