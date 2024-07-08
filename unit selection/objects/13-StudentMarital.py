from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentMarital}")
def StudentMarital(StudentMarital: str):
    maritalstatus = ["متاهل","مجرد"]



    if StudentMarital not in maritalstatus:
        return "لطفا یکی از دو گزینه مجرد و یا متاهل را وارد کنید"

    return "وضعیت وارد شد"


