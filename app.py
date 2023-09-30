from flask import Flask, render_template   
from flask import Flask, render_template, request

app = Flask(__name__)             

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/job_postings')
def job_postings():
    # You can fetch job postings from a database here
    job_postings_data = [
        {'Doctor': 'Job 1', 'description': 'Description 1'},
        {'Teacher': 'Job 2', 'description': 'Description 2'},
    ]
    return render_template('job_postings.html', job_postings=job_postings_data)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    # Fetch job details based on job_id from database
    job_details_data = {'Doctor': 'Job 1', 'description': 'Description 1'}
    return render_template('job_details.html', job=job_details_data)   

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    

if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)