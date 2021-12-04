from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.


def index(request):
    return render(request, "homepages/home.html")


def login(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, "homepages/signin.html")


def register(request):
    if request.method == "POST":
        email = request.form['txtEmail']
        school = request.form["txtSch"]
        file = request.FILES["fileAuthentication"]
        filename = file.name
        notes = request.form["txtNotes"]
        if file.size > 25165824:
            return render(request, "homepages/signup.html", {
                "errormessage": "File too large! Maximum upload of 24MB",
                "successmessage": ""
            })
        body_text = "<h1>Details</h1><br/>"
        body_text += "<b>Email: </b>" + str(email)
        body_text += "</br><b>School: </b>" + str(school)
        body_text += "<br/><b>Additional Notes: </b>" + str(notes)
        email_obj = EmailMessage(
            'Registration attempt',
            body_text,
            'sgs.aether@aol.com',
            'sgs.aether@aol.com',
        )
        email_obj.content_subtype = "html"
        email_obj.attach(filename, file)
        confirmation_text = "Registration success! You should receive an email in the next couple of weeks. If not, please try again or contact us at sgs.aether@aol.com."
        confirmation_email = EmailMessage(
            'Registration attempt made',
            confirmation_text,
            'sgs.aether@aol.com',
            email,
        )
        try:
            confirmation_email.send()
            email_obj.send()
        except:
            return render(request, "homepages/signup.html", {
                "errormessage": "An unknown error has occurred. :(",
                "successmessage": ""
            })
        return render(request, "homepages/signup.html", {
            "errormessage": "",
            "successmessage": "Registration success! You should receive confirmation of your account creation in a couple of weeks."
        })
    elif request.method == "GET":
        return render(request, "homepages/signup.html", {
            "errormessage": "",
            "successmessage": ""
        })
