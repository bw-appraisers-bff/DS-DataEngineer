from flask import Flask, request

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
        if any([s == '' for s in [bedrooms, bathrooms, squarefeet,
                                  zipcode, yearbuilt]]):
            return 'There was an empty value for one of the feautes.'
        else:
            return (f'estimate: $185,000, bedrooms: {bedrooms}, '
                    f'bathrooms: {bathrooms}, squarefeet: {squarefeet}, '
                    f'zipcode: {zipcode}, yearbuilt: {yearbuilt}')
