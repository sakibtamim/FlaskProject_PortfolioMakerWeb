from flask import Flask,render_template,request
import uuid
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/upload', methods = ["GET","POST"])
def upload():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        profession = request.form.get("profession")
        school = request.form.get("school")
        college = request.form.get("college")
        university = request.form.get("university")
        address = request.form.get("address")
        phone = request.form.get("phone")
        email = request.form.get("email")
        about = request.form.get("about")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        git = request.form.get("github")
        fb = request.form.get("facebook")
        linkedin = request.form.get("linkedin")
        key = uuid.uuid1()

        #Image uploading method
        img = request.files["pic"]
        img.save(f"static/dp's/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/dp's/{img.filename}",f"static/dp's/{img_new_name}")
    return render_template('design1.html', fname = firstname, lname = lastname, dprofession = profession, dschool = school, img = img_new_name,
                           dcollege = college, duniversity = university, daddress = address, dphone = phone, dmail = email, dabout= about, dskill1 = skill1,
                           dskill2 = skill2, dskill3 = skill3, dskill4 = skill4, dgit = git, dfb=fb, dlinkedin=linkedin)

if __name__ == '__main__':
    app.run(debug=True)
