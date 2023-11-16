from flask import Blueprint, render_template, request, redirect, url_for
import optimisation

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        typeOfCalculation = request.form.get('typeOfCalculation')
<<<<<<< HEAD
        startDate = datetime.strptime(request.form.get('startDate'), '%Y-%m-%d')
        endDate = datetime.strptime(request.form.get('endDate'), '%Y-%m-%d')

        if startDate > endDate:
            flash("Your end-date cannot be before your start-date", category='error')
            predictie = None
            datums = None
            werkelijk = None

        else:
            duration = (endDate - startDate).days
            beginDateData = datetime.strptime('2018-01-11', '%Y-%m-%d')
            start = (startDate - beginDateData).days
            predictionResults = models.predictConsumptie(start, duration)
            predictie = predictionResults[0]
            werkelijk = predictionResults[1]
            datums = list()
            for i in range(len(predictie)):
                datums.append(str(i))
    else:
        predictie = None
        datums = None
        werkelijk = None

    return render_template('demo.html', result = predictie, datums = datums, werkelijk = werkelijk)
=======
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
    return render_template('demo.html')
>>>>>>> 229e468b6957c8d15d6eab727a5f25b97f38a86e
