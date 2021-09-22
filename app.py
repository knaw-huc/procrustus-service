from flask import Flask, request
import json
from elastic_index import Index


app = Flask(__name__)

config = {
    "url" : "localhost",
    "port" : "9200",
    "doc_type" : "ecodices"
}

index = Index(config)


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Content-type'] = 'application/json'
    return response

@app.route("/")
def hello_world():
    retStruc = {"app": "Procrustus service", "version": "0.1"}
    return json.dumps(retStruc)

@app.route("/facet", methods=['GET'])
def get_facet():
    facet = request.args.get("name")
    amount = request.args.get("amount")
    retStruc = index.get_facet(facet + ".keyword", amount)
    return json.dumps(retStruc)

@app.route("/browse", methods=['GET'])
def browse():
    page = request.args.get("page")
    retStruc = index.browse(page)
    return json.dumps(retStruc)

#Start main program

if __name__ == '__main__':
    app.run()
