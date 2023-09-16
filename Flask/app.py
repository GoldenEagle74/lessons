from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'your-secret-key'  # Замените на ваш собственный секретный ключ
app.config['UPLOAD_FOLDER'] = 'uploads'  # Папка для загрузки файлов
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Максимальный размер загружаемого файла (16 МБ)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    username = None
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        if user:
            username = user.username
    return render_template('index.html', username=username)

# Добавлен маршрут для страницы управления файлами
@app.route('/user/files')
def user_files():
    if 'user_id' not in session:
        flash('Вы должны войти в систему, чтобы управлять файлами', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    user_files = os.listdir(app.config['UPLOAD_FOLDER'])

    return render_template('user_files.html', user=user, user_files=user_files)

# Маршрут для скачивания файла
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Маршрут для удаления файла
@app.route('/delete/<filename>')
def delete_file(filename):
    if 'user_id' not in session:
        flash('Вы должны войти в систему, чтобы управлять файлами', 'danger')
        return redirect(url_for('login'))

    # Проверка наличия файла и прав пользователя на удаление
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f'Файл {filename} успешно удален', 'success')
    else:
        flash(f'Файл {filename} не существует', 'danger')

    return redirect(url_for('user_files'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неправильное имя пользователя или пароль', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрированы!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Вы успешно вышли из системы!', 'success')
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        flash('Вы должны войти в систему, чтобы загружать файлы', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Сохраняем файл в папке UPLOAD_FOLDER
            filename = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(filename)
            flash('Файл успешно загружен!', 'success')
    
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
