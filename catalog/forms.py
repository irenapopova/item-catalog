from wtforms import Form, BooleanField, StringField, SelectField, PasswordField, FloatField, TextAreaField, validators

# parent -child relationship


class CategoryForm(Form):
    name = StringField('Category Name:', [validators.Length(min=4, max=25)])


class BookForm(Form):
    name = StringField('Book Name:', [validators.Length(min=4, max=25)])
    # category = IntegerField('')
    category = SelectField('Category', coerce=int)
    author = StringField('Author:', [validators.Length(min=4, max=250)])
    # the price column should have a value
    price = FloatField('Price:', [validators.required()])
    description = TextAreaField(
        'Description:', [validators.Length(min=10, max=500)])
    image = StringField('Image Url:', [validators.Length(min=10, max=100)])
