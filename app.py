from flask import Flask,render_template,request
import re

app = Flask(__name__)

def check_strength(password) :
    tips = []
    score = 0
    #Removing any extra spaces
    password.strip()
    #Checking for password length; ideally >= 8 characters
    if(len(password)>=8) :
        score += 1
    else :
        tips.append("Use atleast 8 characters!")

    #Checking for uppercase characters being present
    if(re.search(r"[A-Z]",password)):
        score += 1
    else :
        tips.append("Password does not contain uppercase characters(A-Z)!")

    #Checking for lowercase characters being present
    if(re.search(r"[a-z]",password)):
        score += 1
    else :
        tips.append("Password does not contain lowercase characters(a-z)!")
    
    #Checking for the presence of atleast one digit
    if(re.search(r"\d",password)) :
        score += 1
    else :
        tips.append("Password does not contain digits!")

    #Checking for special characters 
    if(re.search(r"[!@#$%^&*()_+]",password)) :
        score += 1
    else :
        tips.append("Password does not contain special symbols!")


    #Limits for the password score

    if(score<=2) :
        strength = "Weak"
    
    elif(score==3 or score==4) :
        strength = "Medium"
    
    else :
        strength = "Strong"


    return strength,tips

def get_strength_percentage(strength):
    return {"Strong":100,"Medium":60,"Weak":30}.get(strength,30)

def get_strength_colour(strength):
    return {"Strong":"bg-success","Medium":"bg-warning","Weak":"bg-danger"}.get(strength, "bg-danger")

def get_width_class(strength):
    return {
    "Strong": "w-100",
    "Medium": "w-60",
    "Weak": "w-30"
    }.get(strength, "w-30")

@app.route("/",methods=["GET","POST"])
def index() :
    strength = None
    suggestions = []
    percentage=0
    colour=""
    width_class = ""

    if request.method == "POST" :
        password = request.form["password"]
        strength,suggestions=check_strength(password)
        percentage=get_strength_percentage(strength)
        colour=get_strength_colour(strength)
        width_class = get_width_class(strength)

    return render_template("index.html",strength=strength,suggestions=suggestions,percentage=percentage,colour=colour,width_class=width_class)


if __name__ == "__main__" :
    app.run(debug=True)