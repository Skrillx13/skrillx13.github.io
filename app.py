# Libary Import
from flask import Flask, render_template, render_template_string, abort, send_from_directory
import markdown
import os
import pathlib

app = Flask(__name__, static_folder='assets')

# Directory Configuration
CONTENT_FOLDER = "content"
INDEX_FILE = "index.md"

# Index Page Routing
@app.route("/")
def index():
    # Load and display the index.md file as the home page
    if not os.path.exists(INDEX_FILE):
        abort(404)

    with open(INDEX_FILE, "r") as file:
        md_content = file.read()

    html_content = markdown.markdown(md_content)
    return render_template("index.html", content=html_content, filename="Home")


# Markdown Page Routing
@app.route("/<filename>")
def view_file(filename):

    # Filters out files to find Markdown files
    if not filename.endswith(".md"):
        filename += ".md"

    # Returns a 404 if the file is not found
    file_path = os.path.join(CONTENT_FOLDER, filename)
    if not os.path.exists(file_path):
        return render_template("404.html")
    
    # Reads the Markdown file, and translates it to HTML
    with open(file_path, "r") as file:
        md_content = file.read()

    # Renders the Markdown
    html_content = markdown.markdown(md_content)
    return render_template("page.html", content=html_content, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)