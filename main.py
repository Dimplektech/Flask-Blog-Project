
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

#=== To avoid  version warning and serve locally
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['CKEDITOR_CONFIG']={'versionCheck':False}
#==================================================
# Initialize Bootstrap
Bootstrap5(app)
# Initialise the CKEditor so that you can use it in make_post,html
ckeditor = CKEditor(app)

# Configure the SQLite database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define the form for creating and editing blog posts
class BlogPostForm(FlaskForm):
    title = StringField(label="Blog Post Title",validators=[DataRequired()])
    subtitle = StringField(label="Subtitle",validators=[DataRequired()])
    author = StringField(label="Your name",validators=[DataRequired()])
    img_url = StringField(label="Blog Image URl",validators=[DataRequired()])
    # body is using a CKEditorField and not a StringField
    body = CKEditorField(label="Blog content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")



# Define the database model for blog posts
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        dict = {}
        for column in self.__table__.columns:
            # Create new dictionary entry
            # where key is column name and
            # value is value of the column
            dict[column.name] = getattr(self,column.name)
        return dict


with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    """Route to display all blog posts on the home page."""
    # Query all blog posts from the database
    data = db.session.execute(db.select(BlogPost)).scalars().all()
    posts = []
    for post in data:
        posts.append(post.to_dict())
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/show_post/<post_id>')
def show_post(post_id):
    """Route to display a single blog post by ID."""
    #  Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost,post_id)
    print(requested_post)
    return render_template("post.html", post=requested_post)


#  add_new_post to create a new blog post
@app.route("/new_post",methods = ["GET","POST"])
def add_new_post():
    """Route to create a new blog post."""
    blog_form = BlogPostForm()
    today_date = datetime.now().strftime("%B %d, %Y")
    print(today_date)
    if request.method == "POST" and blog_form.validate_on_submit():
        # Create a new blog post instance and add it to the database
        post = BlogPost(
            title = blog_form.title.data,
            subtitle = blog_form.title.data,
            date = today_date,
            body = blog_form.body.data,
            author = blog_form.author.data,
            img_url  = blog_form.img_url.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',form = blog_form)



# edit_post to change an existing blog post
@app.route("/edit_post/<post_id>",methods=["GET","POST"])
def edit_post(post_id):
    """Route to edit an existing blog post."""
    # Retrieve the blog post to edit
    post = db.session.get(BlogPost,post_id)
    # Pre-fill the form with the existing post data
    edit_form = BlogPostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )

    if edit_form.validate_on_submit():
            # Update the blog post with new data
            post.title= edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.body=edit_form.body.data
            post.author=edit_form.author.data
            post.img_url=edit_form.img_url.data
            db.session.commit()
            return redirect(url_for("show_post",post_id=post.id))

    return render_template("make-post.html", form=edit_form, is_edit=True)



# delete_post to remove a blog post from the database
@ app.route("/delete/<post_id>")
def delete_post(post_id):
    """Route to delete a blog post by ID."""
    post =db.session.get(BlogPost,post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        print("Post has been deleted!!")
        return redirect(url_for('get_all_posts'))
    return render_template('index.html')

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    """Route to display the About page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Route to display the Contact page."""
    return render_template("contact.html")


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True, port=5003)
