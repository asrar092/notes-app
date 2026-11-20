
from flask import Flask, request, redirect

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
        return redirect("/")

    html = """
    <h1>This is my Application </h1>

    <form method="POST">
        <input name="note" placeholder="Write your note..." required>
        <button type="submit">Add Note</button>
    </form>

    <h2>My Notes:</h2>
    <ul>
    """

    for note in notes:
        html += f"<li>{note}</li>"

    html += "</ul>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
