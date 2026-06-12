# Mini web server (Flask)

## 💥 **About project**

Simple local server based on Flask for running and testing websites directly on your computer.

## 💫 Features
* Quickly launch static sites from any local folder.
* Support for SPA routing (all requests are redirected to `index.html`).
* Automatic serving of assets (scripts, styles, images).
* Support for sessions and basic authentication.

## ⚒️ How to build
Clone the repository or download the project files.

To build this project, you need to have the following dependencies installed:
* Python 3.x;
* Flask;
* python-dotenv (If you use Environment Variables);

Install Flask:
\`\`\`bash
pip install flask
\`\`\`

Install python-dotenv:
\`\`\`
pip install python-dotenv
\`\`\`

Copy the full path to the folder containing your website and set it as the PROJECT_FOLDER variable in app.py.
For example:
\`\`\`
C:\Users\User\Desktop\your_folder
\`\`\`

## 💻 Starting the server
Start the server by entering the following command in the terminal:
\`\`\`
python app.py
\`\`\`

After that, the site will be accessible in your browser at: http://127.0.0.1:5000

✨ Designed for local testing of interfaces and integrations.