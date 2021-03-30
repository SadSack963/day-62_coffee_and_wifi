from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import csv
from cafe_class import CafeForm
import inspect


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def append_to_csv(form):
    csv_data = [
        form.cafe.data,
        form.location.data,
        form.open.data,
        form.close.data,
        form.coffee.data,
        form.wifi.data,
        form.power.data
    ]
    with open('cafe-data.csv', newline='', encoding='utf-8', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(csv_data)


# All Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        append_to_csv(form)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
