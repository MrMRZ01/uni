from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentPhone}")
def StudentPone(StudentPhone):
    phone = StudentPhone
    firsttow = str(phone[:2])
    len1 = int(len(str(phone)))

    if firsttow != "09":
        return "شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد"
    if len1 >= 12 or len1 <= 10:
        return "ارقام وارده باید 11 رقم باشد"

    return "شماره وارد شده صحیح است"