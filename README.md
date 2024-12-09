# Flask Blog Project

## Overview
This is a simple blog application built with Flask. It allows users to:
- Create, edit, and delete blog posts.
- View all posts on the homepage.
- View details of individual posts.

The application uses SQLite for the database, Flask-WTF for form handling, and CKEditor for a rich text editor.

## Features
1. **CRUD Operations**:
   - Add new blog posts.
   - Edit existing blog posts.
   - Delete blog posts.
2. **Rich Text Editing**:
   - CKEditor is integrated for writing blog content.
3. **Database Integration**:
   - SQLite is used to store blog posts.
4. **Bootstrap Integration**:
   - Bootstrap is used for styling and layout.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask and its extensions (detailed in the requirements section below)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dimplektech/Flask-Blog-Project
   cd flask-blog-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python app.py
   ```
   This will create the `posts.db` file with the required tables.

## Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5003/
   ```

## File Structure
```
flask-blog-project/
├── app.py                # Main application file
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Homepage displaying all posts
│   ├── post.html         # Single post details
│   ├── make-post.html    # Form for creating/editing posts
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
├── static/               # Static files (CSS, JS, Images)
├── posts.db              # SQLite database file
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Dependencies
The required Python packages are listed in `requirements.txt`. Here are the key dependencies:
- Flask
- Flask-Bootstrap
- Flask-WTF
- Flask-SQLAlchemy
- Flask-CKEditor

To install all dependencies:
```bash
pip install -r requirements.txt
```

## Key Components
### Routes
- `/`: Displays all blog posts.
- `/show_post/<post_id>`: Displays details of a specific post.
- `/new_post`: Allows users to create a new post.
- `/edit_post/<post_id>`: Allows users to edit an existing post.
- `/delete/<post_id>`: Deletes a specific post.
- `/about`: Displays the About page.
- `/contact`: Displays the Contact page.

### Database Model
- `BlogPost`:
  - `id`: Unique identifier.
  - `title`: Title of the blog post.
  - `subtitle`: Subtitle of the blog post.
  - `date`: Date of publication.
  - `body`: Content of the post (rich text).
  - `author`: Name of the author.
  - `img_url`: URL of the post's image.

## Known Issues
- Ensure the form validation is correctly implemented when using CKEditor.
- SQLite is used for simplicity; switch to a more robust database like PostgreSQL for production.

## Future Improvements
- Add user authentication for managing posts.
- Add pagination for the homepage.
- Enhance styling and responsiveness.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

