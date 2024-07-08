from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentSerial}")
def StudentSerial(StudentSerial):
    alpha = (str(StudentSerial)[:1])
    townum = int(str(StudentSerial)[2:4])
    sixnum = int(str(StudentSerial)[4:10])
    len1 = int(len(str(StudentSerial)))
    allalpha = ["آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د",
                "ذ", "ر", "ز", "ط", "ظ", "ع", "غ", "ک", "گ", "ل", "ض",
                "ص", "ف", "ق", "ن", "ی", "س", "ش", "ژ", "و", "م"]

    if len1 >= 10 or len1 <= 8:
        return "تعداد کاراکتر های وارد شده نادرست است"
    if alpha not in allalpha:
        return "حرف فارسی وارد شده نادرست است"
    if not isinstance(townum, int):
        return "بخش دو رقمی حتما باید عدد باشد"
    if not isinstance(sixnum, int):
        return "بخش شش رقمی نیز حتما باید عدد باشد"

    return "شماره شناسنامه وارد شده صحیح است"














