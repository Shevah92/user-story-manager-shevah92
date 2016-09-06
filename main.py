from models import *
from flask import *


app = Flask(__name__)


@app.route("/story", methods=["GET"])
def render_story():
    return render_template("story.html")


@app.route("/story", methods=["POST"])
def get_data():
    fos = UserStories.create(story_title = request.form["story_title"],
                       user_story = request.form["user_story"],
                       acceptance = request.form["acceptance"],
                       business_value = request.form["business_value"],
                       estimation = request.form["estimation"],
                       status = request.form["status"])
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
