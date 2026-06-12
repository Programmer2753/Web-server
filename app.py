from flask import Flask, session, request, flash, redirect, url_for, send_from_directory
import os

def start_site(site_id):
    session["site"] = site_id

def end_site():
    session.clear()

PROJECT_FOLDER = os.path.join(os.getcwd(), r"your_path_to_your_project_folder")

def index():
    if request.method == "POST":
        if request.form.get("username") == "admin" and request.form.get("password") == "admin":
            start_site("admin")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("index"))
        
    return send_from_directory(PROJECT_FOLDER, "index.html")

folder = os.getcwd()

app = Flask(__name__, static_folder=PROJECT_FOLDER, static_url_path="")
app.add_url_rule("/", "index", index, methods= ["post", "get"])
app.add_url_rule("/index", "index", index, methods= ["post", "get"])

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(PROJECT_FOLDER, filename)

app.config["SECRET_KEY"] = "gbasjml1gj2454kfsf83f"

if __name__ == "__main__":
    app.run()
