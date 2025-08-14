from flask import *
from forms import VoterForm
import os
from werkzeug.utils import *

app = Flask(__name__)

# config for csrf token
app.config["SECRET_KEY"] = "yitcseaflask"

# inmemory
applications = []

@app.route("/",methods=["GET","POST"])
def application():
    voter = VoterForm()
    if voter.validate_on_submit():
        applicant = {
            voter.fullname.name:voter.fullname.data,
            voter.age.name:voter.age.data,
            voter.email.name:voter.email.data,
            voter.gender.name:voter.gender.data,
            voter.aadhaar.name:voter.aadhaar.data,
            voter.constituency.name:voter.constituency.data,
            voter.declaration.name:voter.declaration.data
        }
        applications.append(applicant)
        return jsonify(applications)
    return render_template('application.html',form = voter)

if __name__ == "__main__": app.run('localhost',8899)