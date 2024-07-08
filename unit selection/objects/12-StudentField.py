from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentField}")
def StudentField(StudentField: str):
    allfield = ["برق","کامپیوتر",
                  "عمران","معماری",'مکانیک']


    if StudentField not in allfield:
        return "رشته وارد شده نادرست است"

    return "رشته وارد شده صحیح است"


