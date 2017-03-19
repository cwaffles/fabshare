import rh
import homePageController

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return rh.getIndex()

# @app.route("/trips/")
# def tripsIndex():
#     return rh.tripsIndex()

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



def sendCostEmail(inputSubject, emailadd, fuelUsed, costEst, personName):
    import email
    import smtplib
    from jinja2 import Template

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("dividfabshare@gmail.com", "fabshare")

    msg = "Subject: {{subject}}\n\nHey there freeloader,\n\nMY CAR RUNS ON FUEL NOT FRIENDSHIP!\n I used {{gasamount}} liters of fuel so you part is {{Money}}$\n\n" \
          "your obedient servant,\n" \
          "{{userName}}"

    t = Template(msg)

    output = t.render(subject = inputSubject, gasamount = '%.2f' %fuelUsed, Money = '%.2f' %costEst, userName = personName)
    server.sendmail("dividfabshare@gmail.com", emailadd, output)
    server.quit()


@app.route('/emailTrip/<tid>')
def send_email(tid):
    tripCities = homePageController.getCitiesFromTrip(tid)
    print(tripCities)
    return render_template('email.html', startCity=tripCities[0], endCity=tripCities[1], tripId=tid)
    # return send_from_directory('js', path)

@app.route('/emailSend', methods=['GET', 'POST'])
def sendEmails():
    if request.method == 'POST':
        tripSummary = homePageController.getTripSingleSummary(request.form['tid'])

        # print(id)
        efficiency = float(tripSummary[5])
        # print(id[4])
        distance = float(tripSummary[4]) / 1000
        fuelConsumed = 0.1
        fuelConsumed = efficiency * distance / 100

        # Calculate cost of gas
        print(fuelConsumed)
        import view

        subject = "Your DIVID share from " + tripSummary[1] + " to " + tripSummary[2]
        cost = fuelConsumed * view.GAS_PRICE
        name = "Your friend"
        # print(request.form['user_mail_one'])
        tripPassengers = 0
        try:
            
            #get trip pass
            if(request.form['user_mail_one'] is not ""):
                tripPassengers+=1
            if (request.form['user_mail_two'] is not ""):
                tripPassengers += 1
            if (request.form['user_mail_three'] is not ""):
                tripPassengers += 1
            if (request.form['user_mail_four'] is not ""):
                tripPassengers += 1
            
                   
            if(request.form['user_mail_one'] is not None):
                sendCostEmail(subject, request.form['user_mail_one'], fuelConsumed, (cost/tripPassengers), name)
            if (request.form['user_mail_two'] is not None):
                sendCostEmail(subject, request.form['user_mail_two'], fuelConsumed, (cost/tripPassengers), name)
            if (request.form['user_mail_three'] is not None):
                sendCostEmail(subject, request.form['user_mail_three'], fuelConsumed, (cost/tripPassengers), name)
            if (request.form['user_mail_four'] is not None):
                sendCostEmail(subject, request.form['user_mail_four'], fuelConsumed, (cost/tripPassengers), name)
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

