from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentNationalCode}")
def StudentNationalCode(StudentNationalCode):
    code = StudentNationalCode
    l = len(code)
    sum = 0
    for i in range(0, l - 1):
        c = ord(code[i])
        c -= 48
        sum = sum + c * (l - i)
    r = sum % 11
    c = ord(code[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r != c:
        return "کدملی وارد شده نامعتبر است"
    return "کدملی وارد شده صحیح است"