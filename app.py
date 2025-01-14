from flask import Flask, render_template
from components import header, footer, content

app = Flask(__name__)

# Rejestracja komponentów
components = {
    "header": header.render(),
    "content": content.render(),
    "footer": footer.render()
}

@app.route("/")
def index():
    return render_template("page.html", components=components)

if __name__ == "__main__":
    app.run(debug=True)
