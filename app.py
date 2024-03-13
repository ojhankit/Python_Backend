from flask import Flask
from flask import render_template
from flask import jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru,India',
        'salary': 'Rs 15,00,000',
    },
    {   'id': 2,
        'title': 'Backend Engineer',
        'location': 'Bengaluru,India',
        'salary': 'Rs 20,00,000',
    },
    {   'id': 3,
        'title': 'Devop Engineer',
        'location': 'Bengaluru,India',
        'salary': 'Rs 25,00,000',
    }
]
@app.route("/")
def hello_world():
    return render_template('index.html' , jobs=JOBS,company_name='Jovian')


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0" , debug=True)