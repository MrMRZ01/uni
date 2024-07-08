from fastapi import FastAPI

app = FastAPI()

@app.get('/home/{StudentName}')
def StudentName(StudentName):
    if not StudentName.isalpha():
        return "نام باید فقط شامل حروف فارسی باشد."
    if len(StudentName) > 15:
        return "نام نباید بیشتر از 15 حرف باشد."
    for char in StudentName:
        if not char.isalpha():
            return "نام نباید حاوی عدد یا علامت خاص باشد."
    return "نام درست است."



