from flask import redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(16), nullable=False)

@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Задание №4. Реализовать проверку пользователей
            users_db = User.query.all()
            for user in users_db:
                if form_login == user.login and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'Неправильно указан пользователь или пароль'
                return render_template('login.html', error=error)
           
        


            
        else:
            return render_template('login.html')
        
@app.route('/index') 
def index():    
    return render_template('index.html')


@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        
        #Задание №3. Реализовать запись пользователей
        user = User(login=login, password=password)
        
        db.session.add(user)
        db.session.commit()
        
        return redirect('/index')
    
    else:    
        return render_template('registration.html')

@app.route('/ques')
def quest():
    return render_template('question.html')


if __name__ == "__main__":
    app.run(debug=True)




