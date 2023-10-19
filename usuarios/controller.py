from flask import Blueprint, request, session, url_for, redirect, flash, render_template

bp = Blueprint("Usuario", __name__ )

@bp.route("/login", methods=('POST', 'GET'))
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        from database.dados import alunos
        for k,v in alunos.items():
            if email == v.get('usuario') and senha == v.get('senha'):
                session['user'] = v
                return redirect(url_for('index'))
            else:
                error = "Usuario ou senha inválidos!"

    return render_template("usuario/login.html", error=error)

@bp.route("/perfil", methods=('POST', 'GET'))
def perfil():

    if 'user' not in session and False:
        # se não tiver logado devolve para login
        return redirect(url_for(login))
    
        # 1-Pegar dados do banco
        #for k,v...in alunos...session['user']['email']

    if request.method == 'POST':
        # lógica salvar
        nome = request.form.get("nome")
        email = request.form.get("email")

        from database.dados import alunos
        for k,v,x in alunos.items():
            pass

    return render_template("perfil.html") #, usuario=usuario

@bp.route("/logout")
def logout():
    return redirect(url_for("login"))

        