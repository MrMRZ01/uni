from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{StudentCollege}")
def StudentState(StudentCollege: str):
    allcollege = ["فنی و مهندسی","علوم پایه",
                  "شیمی","اقتصاد",'ادبیات']


    if StudentCollege not in allcollege:
        return "دانشکده وارد شده نادرست است"

    return "دانشکده وارد شده صحیح است"


