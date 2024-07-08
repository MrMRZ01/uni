from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentAddress}")
def StudentAddress(StudentAddress):
    address = StudentAddress
    len1 = int(len(address))

    if len1 >= 101:
        return "تعداد کاراکتر های مجاز استفاده 100 عدد می باشد"
    if address is int:
        return "لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید"

    return "آدرس وارد شده صحیح است"