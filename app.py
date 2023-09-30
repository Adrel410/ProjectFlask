from flask import Flask, render_template   
from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for job postings (use the API's database)
job_postings = [
    {"id": 1, "title": "Web Developer", "description": "Full-stack web developer position"},
    {"id": 2, "title": "Data Scientist", "description": "Data science role"},
    {"id": 3, "title": "UX Designer", "description": "User experience designer needed"},
]

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

@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        # In the real application, you would save the job posting to a database.
        # we added it to the dummy data.
        job_id = len(job_postings) + 1
        job_postings.append({"id": job_id, "title": title, "description": description})
        return redirect(url_for('index'))
    return render_template('post_job.html')

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    

if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)