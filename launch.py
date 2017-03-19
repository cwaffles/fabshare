import rh
import homePageController
import email
import smtplib



from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return rh.getIndex()

@app.route("/trips/")
def tripsIndex():
    return rh.tripsIndex()

@app.route("/vehicles/")
def vehiclesIndex():
    return rh.vehiclesIndex()

@app.route("/tripsCostPage/")
def blank():
    id = request.args.get('id', '')
    return rh.getTripPage(id)

#
# @app.route("/emailLoader/")
# def vehiclesIndex():
#     return rh.vehiclesIndex()
#



def sendCostEmail(emailadd, fuelUsed, costEst, personName):
    import smtplib
    from jinja2 import Template

    print(emailadd)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("dividfabshare@gmail.com", "fabshare")

    msg = "Hey there freeloader,\n\nMY CAR RUNS ON FUEL NOT FRIENDSHIP!\n I used {{gasamount}} liters of fuel so you part is {{Money}}$\n\n" \
          "your obedient servant,\n" \
          "{{userName}}"

    t = Template(msg)
    output = t.render(gasamount = fuelUsed, Money = costEst, userName = personName)
    server.sendmail("dividfabshare@gmail.com", emailadd, output)


@app.route('/emailTrip/<tid>')
def send_email(tid):
    tripCities = homePageController.getCitiesFromTrip(tid)
    print(tripCities)
    return render_template('email.html', startCity=tripCities[0], endCity=tripCities[1])
    # return send_from_directory('js', path)

@app.route('/emailSend', methods=['GET', 'POST'])
def sendEmails():
    if request.method == 'POST':

        fuelUsed = "$99"
        cost = "$100"
        name = "Anon"
        print(request.form['user_mail_one'])

        try:
            if(request.form['user_mail_one'] is not None):
                sendCostEmail(request.form['user_mail_one'], fuelUsed, cost, name)
            if (request.form['user_mail_two'] is not None):
                sendCostEmail(request.form['user_mail_two'], fuelUsed, cost, name)
            if (request.form['user_mail_three'] is not None):
                sendCostEmail(request.form['user_mail_three'], fuelUsed, cost, name)
            if (request.form['user_mail_four'] is not None):
                sendCostEmail(request.form['user_mail_four'], fuelUsed, cost, name)
        except:
            return 'sent!'

    else:
        return 'shouldnt see this'



@app.before_first_request
def init():
    rh.initAll()

@app.teardown_appcontext
def close_db(error):
    return rh.shutdownAll()

if __name__ == "__main__":
    app.run()

