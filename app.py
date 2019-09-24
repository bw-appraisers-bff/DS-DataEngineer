from flask import Flask, render_template, request
import predictions
from random import randint

app = Flask(__name__)


@app.route('/')
def estimate():
    try:
        bedrooms = request.args['bedrooms']
        bathrooms = request.args['bathrooms']
        squarefeet = request.args['squarefeet']
        zipcode = request.args['zipcode']
        yearbuilt = request.args['yearbuilt']
    except KeyError:
        return ('Bad request: one of the required values '
                'was missing in the request.')
    else:
        features = [bedrooms, bathrooms, squarefeet, zipcode, yearbuilt]
        if any([string == '' for string in features]):
            return 'There was an empty value for one of the feautes.'
        else:
            return str(randint(40000, 1000000))


@app.route('/jayden')
def jayden():
    try:
        bedrooms = request.args['bedrooms']
        bathrooms = request.args['bathrooms']
        squarefeet = request.args['squarefeet']
        zipcode = request.args['zipcode']
        yearbuilt = request.args['yearbuilt']
    except KeyError:
        return ('Bad request: one of the required values '
                'was missing in the request.')
    else:
        feature_names = ['bedrooms', 'bathrooms', 'squarefeet',
                         'zipcode', 'yearbuilt']
        feature_values = [bedrooms, bathrooms, squarefeet, zipcode, yearbuilt]
        if any([string == '' for string in feature_values]):
            return 'There was an empty value for one of the feautes.'
        else:
            inputs = [int(value) for value in feature_values]
            estimate = predictions.jayden(inputs)
            return render_template('base.html',
                                   name='Jayden',
                                   features=zip(feature_names, feature_values),
                                   estimate=estimate)


@app.route('/taylor')
def taylor():
    try:
        typeid = request.args['typeid']
        assessmentyear = request.args['assessmentyear']
        bedrooms = request.args['bedrooms']
        bathrooms = request.args['bathrooms']
        squarefeet = request.args['squarefeet']
        yearbuilt = request.args['yearbuilt']
        lotsize = request.args['lotsize']
    except KeyError:
        return ('Bad request: one of the required values '
                'was missing in the request.')
    else:
        feature_names = ['typeid', 'assessmentyear', 'bedrooms', 'bathrooms',
                         'squarefeet', 'yearbuilt', 'lotsize']
        feature_values = [typeid, assessmentyear, bedrooms, bathrooms,
                          squarefeet, yearbuilt, lotsize]
        if any([string == '' for string in feature_values]):
            return 'There was an empty value for one of the feautes.'
        else:
            inputs = [int(value) for value in feature_values]
            estimate = predictions.taylor(inputs)
            return render_template('base.html',
                                   name='Taylor',
                                   features=zip(feature_names, feature_values),
                                   estimate=estimate)
