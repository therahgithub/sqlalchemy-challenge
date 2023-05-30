# Flask Import
from flask import Flask, jsonify

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def Aloha():
    return (
        f"<b><u>Aloha and welcome to the Hawaii Weather API</u>!</b><br/>"
        f"<br/>"
        f"<b>Available Routes:</b><br/>"
        f"/api/v1.0/justice-league<br/>"
        f"/api/v1.0/justice-league/superhero/batman<br/>"
        f"/api/v1.0/justice-league/real_name/bruce%20wayne"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify(justice_league_members)


# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)