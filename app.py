from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Routes for each project
@app.route('/project/portfolio')
def portfolio_website():
    return render_template('project_files/portfolio_website.html')

@app.route('/project/invoice')
def invoice_generator():
    return render_template('project_files/Invoice_Generator.html')

@app.route('/project/iam')
def iam_solutions():
    return render_template('project_files/IAM_Solutions.html')

@app.route('/project/java')
def java_app_development():
    return render_template('project_files/java_app_development.html')

@app.route('/project/web')
def web_technologies_project():
    return render_template('project_files/web_technologies_project.html')

if __name__ == '__main__':
    app.run(debug=True)
