from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    text = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Post', validators=[Required()])


class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:', validators=[Required()])
    submit = SubmitField('Submit')