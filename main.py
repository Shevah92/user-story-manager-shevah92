from models import *
from flask import *
import config


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/list", methods=["GET"])
def render_index():
    stories = UserStories.select()
    return render_template("list.html", stories = stories, address= config.address,
                           delete = config.address+"story/delete/", edit= config.address+"story/")

@app.route("/story/<story_id>", methods=["GET"])
def render_edit(story_id):
    data = UserStories.get(UserStories.id == story_id)
    return render_template("story.html", data = data, function = "Edit")


@app.route("/story/<story_id>", methods=["POST"])
def update_story(story_id):
    update = UserStories.update(story_title=request.form["story_title"],
                       user_story=request.form["user_story"],
                       acceptance=request.form["acceptance"],
                       business_value=request.form["business_value"],
                       estimation=request.form["estimation"],
                       status=request.form["status"]).where(UserStories.id == story_id)
    update.execute()
    return redirect(config.address)


@app.route("/story", methods=["GET"])
def render_story():
    data = []
    return render_template("story.html", data = data, function = "Add New")


@app.route("/story/", methods=["POST"])
def get_data():
    UserStories.create(story_title=request.form["story_title"],
                       user_story=request.form["user_story"],
                       acceptance=request.form["acceptance"],
                       business_value=request.form["business_value"],
                       estimation=request.form["estimation"],
                       status=request.form["status"])

    return redirect(config.address)

@app.route("/story/delete/<story_id>", methods=["GET"])
def delete_story(story_id):
    data = UserStories.get(UserStories.id == story_id)
    data.delete_instance()
    return redirect(config.address)

if __name__ == '__main__':
    app.run(debug=True)

