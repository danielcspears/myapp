from flask import Flask , render_template
import datetime

application = Flask(__name__)

@application.route("/", methods=["GET"])

def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
	"title" : "Daniel C Spears - Flask on AWS elastic beanstalk - deployed on 3-30-2018",
	"time": timeString
	}
	return render_template("main.html", **templateData)


if __name__ == "__main__":
 application.run()