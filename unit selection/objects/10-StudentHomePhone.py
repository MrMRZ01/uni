from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentPhone}")
def StudentPone(StudentPhoneHome):
    phoneH = StudentPhoneHome
    len1 = int(len(str(phoneH)))
    code = str(phoneH)[:3]
    first = str(phoneH)[3:4]
    allcode = ["086","021",'025','041','044','045','031','026','084','077',
               '028','071','054','023','024','058','061','051','056','038',
               '087','034','083','013','017','074','066','011','076','081','035']
    allfirst = ['3','4','5','8']

    if code not in allcode:
        return "کد شهرستان وارد شده نادرست است"
    if first not in allfirst:
        return "رقم اول بعد از کد شهرستان نادرست است"
    if len1 >= 12 or len1 <= 10:
        return "ارقام وارده باید 11 رقم باشد"

    return "شماره وارد شده صحیح است"