from flask import Flask, render_template
from components import header, footer, content
import subprocess
import threading

app = Flask(__name__)

# Rejestracja komponentów
components = {
    "header": header.render(),
    "content": content.render(),
    "footer": footer.render(),
}

def run_other_script():
    # Uruchamianie pliku .py w tle
    subprocess.run(["python", "components/working_app_light.py"])

@app.route("/")
def index():
    return render_template("page.html", components=components)

if __name__ == "__main__":
    # Uruchamianie pliku innego w tle
    threading.Thread(target=run_other_script).start()
    
    # Uruchomienie aplikacji Flask
    app.run(debug=True)
