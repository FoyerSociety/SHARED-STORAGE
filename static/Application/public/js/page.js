csrf_token = $('body').attr('name');
key = '';

function verifier(btn){
    $('.alert-danger').remove()
    btn.html("<img src='static/Application/public/images/loading.gif'>")
    frm = $('#mail_space');
    mail = frm.find('input[type=email]');
    $.post(

        "/verifie_mail",

        {
            csrfmiddlewaretoken: csrf_token,
            mail: mail.val()
        },

        fb_verifier

        );

        function fb_verifier(rep){
            btn.html("Envoyer");
            if (rep[0] == 1){
                code = mail.clone();
                code.attr('type', 'text');
                code.val('');
                code.attr('id', 'code_conf');
                code.css('margin-top', '20px');
                code.attr('placeholder', 'Entrer code de confirmation')
                mail.after(code);
                btn.removeAttr("onclick");
                btn.click(function (){
                  verifie_code();
                });
                key = rep[1];
            }
            else{
                let html = `
                    <div style="margin: 15px" class="form-group text-center alert-danger">
                        <p> ${rep[0]} <p>
                    </div>`;
                frm.append(html);
            }
        }
    }


function verifie_code(){
  $('.alert-danger').remove()
  let code = $('#code_conf').val();

  if (code == key){
      let newhtml = `
      <div class="form-group">
        <input type="email" id="mail" style="marign: 10px" value="${mail.val()}" class="form-control form-control-user" aria-describedby="emailHelp" disabled=disabled placeholder="Entrer votre email">
      </div>

      <div class="form-group">
        <input type="text" id="username" style="marign: 10px" class="form-control form-control-user" aria-describedby="emailHelp" placeholder="Nom d'utilisateur">
      </div>

      <div class="form-group">
        <input type="text" list="niveau_list" id="niveau" style="marign: 10px" class="form-control form-control-user" aria-describedby="emailHelp" placeholder="Niveau">
      </div>

      <datalist id="niveau_list">
        <option> L1 </option>
        <option> L2 </option>
        <option> L3 </option>
        <option> M1 </option>
        <option> M2 </option>
      </datalist>

      <div class="form-group">
        <input type="password" id="password" style="marign: 10px"  class="form-control form-control-user" aria-describedby="emailHelp" placeholder="Mot de passe">
      </div>

      <a style="color: white" onclick="create_account()" class="btn btn-primary btn-user btn-block">
        Generer Compte
      </a>`;

      frm.html(newhtml);
  }
  else{
    html = `
        <div style="margin: 15px" class="form-group text-center alert-danger">
            <p> Mauvais code <p>
        </div>`;
    frm.append(html);
  }
}


function create_account(){
  let usr = $('#username');
  let passwd = $('#password');
  let niveau = $('#niveau');

  $.post(

      "/create_account",

      {
          csrfmiddlewaretoken: csrf_token,
          mail: mail.val(),
          username: usr.val(),
          password: usr.val(),
          niveau: niveau.val()

      },

      code_reponse

  );

function(dt){
  if (dt == 0){
    alert('succes');
  }
}
}
