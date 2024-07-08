from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentCity}")
def StudentCity(StudentCity):
    city = StudentCity

    if city == int:
        return "لطفا نام شهر را به فارسی وارد کنید و از اعداد استفاده نکنید"
    return "شهر وارد شده درست است"

