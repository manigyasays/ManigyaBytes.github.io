from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')  # You will need to create this template

@app.route('/skills')
def skills():
    return render_template('skills.html')  # You will need to create this template

@app.route('/contact')
def contact():
    return render_template('contact.html')  # You will need to create this template

@app.route('/resume')
def resume():
    return app.send_static_file('assets/resume.pdf')  # If you're serving the resume file from static folder

if __name__ == '__main__':
    app.run(debug=True)
