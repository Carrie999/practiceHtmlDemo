from flask import Flask,render_template,request
import config
app = Flask(__name__)

app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')


# 123213
@app.route('/search')
def search():
    q = request.args.get('q')
    return '用户提交的数据是 %s' % q


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        print('username:', username)
        print('password:', password)
        return 'post request'

if __name__ == '__main__':
    app.run(debug=True)
