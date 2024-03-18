from flask import Flask, render_template, request, jsonify
import json

# Path to your JSON file
data_file = "data.json"

app = Flask(__name__)

# Load data from JSON file on startup
def load_data():
  try:
    with open(data_file, "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return {}

# Save data to JSON file
def save_data(data):
  with open(data_file, "w") as f:
    json.dump(data, f, indent=4)

# Load data on initial page load
data = load_data()

@app.route("/")
def edit_json():
  return render_template("edit.html", data=data)

@app.route("/save", methods=["POST"])
def save_changes():
  # Get form data
  new_time = request.form.get("time")
  new_time2 = request.form.get("time2")
  new_venue = request.form.get("venue")
  #botdate = str(request.form.get("date"))
  
  """# rearrange the date to mm/dd/yyyy
  botdate = botdate.split("-")
  botdate = botdate[1] + "/" + botdate[2] + "/" + botdate[0]"""

  # Update data dictionary
  data["time2"] = new_time2
  data["time"] = new_time
  data["venue"] = new_venue
  #data["date"] = botdate

  # Save data to file
  save_data(data)

  # Return success message as JSON
  return render_template("save.html", data=data)
if __name__ == "__main__":
  app.run(debug=True)
