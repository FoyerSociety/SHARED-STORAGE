import re, smtplib, random, sys, subprocess
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
def home(request):
    return render(request, 'Application/index.html', {})


def verifie_mail(request):
    print('aty e')
    if request.method == "POST":
        mail = request.POST.get('mail')

        if not re.match(r'[a-z]{1}[a-z0-9_.]{1,}@esti.mg', mail):
            return JsonResponse(["Un mail de l'esti est attendue", 0], safe=False)

        key = send_code(mail)
        return JsonResponse([1, key], safe=False)

    raise Http404("Chemin Non Trouvé")


def send_code(mail):
    sys.stdin = open('pass.lock', 'r')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Confirmation Mail ESTI'
    key = random.randint(100000, 999999)
    message = MIMEText("Samba Serveur ESTI")
    html = MIMEText(f"""
        <html>
        <head>
          <link href="https://fonts.googleapis.com/css?family=Poppins&display=swap" rel="stylesheet">
          <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
        </head>
        <body style="font-family: Sans;">
          <section style=" margin-left: 3%; width:70%;   box-shadow: 0 6px 8px 0 #888; padding-bottom: 1.5%;">
          <h1 style="color: #fff; margin-top: 0%; background-color: #034f62; padding:3%;"> <i class="fa fa-rss"></i> ESTI SERVEUR SAMBA </h1>
          <h3 style=" margin-left: 2%;  color: #034f62; "> Bonjour </h3>
    
          <p style="margin-left: 2%; color: #222"> Votre  code de confirmation : <span style="color:#e74926; font-size:18px;">{key}<span></p>
    
          <br>
          </section>
        </body>
    </html>
        """, 'html')
    msg.attach(message)
    msg.attach(html)
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login("gaetan.jonathan.bakary@esti.mg", sys.stdin.read())
    server.sendmail('gaetan.jonathan.bakary@esti.mg', mail, msg.as_string())
    server.quit()
    print(key)
    return key


def create_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        mail = request.POST.get('mail')
        niveau = request.POST.get('niveau')

        rt = subprocess.call(f'Scripts/run_as_root.sh acc {username} {password} {niveau}')

        return HttpResponse(rt)


    raise Http404("Pas Trouvé")
