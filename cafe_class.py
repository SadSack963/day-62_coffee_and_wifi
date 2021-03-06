from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis βοΈ/πͺ/β/π
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


class CafeForm(FlaskForm):
    cafe = StringField(
        label='Cafe name',
        validators=[DataRequired()],
    )
    location = URLField(
        label='Location',
        validators=[URL()]
    )
    open = TimeField(
        label='Open',
        validators=[DataRequired()],
        render_kw={'style': 'width: 12ch'}
    )
    close = TimeField(
        label='Close',
        validators=[DataRequired()],
        render_kw={'style': 'width: 12ch'}
    )
    coffee = SelectField(
        label='Coffee',
        choices=['β', 'β', 'ββ', 'βββ', 'ββββ'],
        validators=[DataRequired()],
        render_kw={'style': 'width: 16ch'}
    )
    wifi = SelectField(
        label='WiFi',
        choices=['β', 'πΆ', 'πΆπΆ', 'πΆπΆπΆ', 'πΆπΆπΆπΆ'],
        validators=[DataRequired()],
        render_kw={'style': 'width: 16ch'}
    )
    power = SelectField(
        label='Power',
        choices=['β', 'π', 'ππ', 'πππ', 'ππππ'],
        validators=[DataRequired()],
        render_kw={'style': 'width: 16ch'}
    )
    submit = SubmitField(
        label='Submit',
        render_kw={'btn-primary': 'True'}
    )
