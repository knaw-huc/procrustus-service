from flask import Flask, request
import json
from elastic_index import Index
from store import Store
from handlers import timbuctoo


app = Flask(__name__)

config = {
    "url" : "localhost",
    "port" : "9200",
    "doc_type" : "ecodices"
}

index = Index(config)
tb = timbuctoo.Timbuctoo_handler()


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
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
    ret_struc = index.get_facet(facet + ".keyword", amount)
    return json.dumps(ret_struc)

@app.route("/filter-facet", methods=['GET'])
def get_filter_facet():
    facet = request.args.get("name")
    amount = request.args.get("amount")
    facet_filter = request.args.get("filter")
    ret_struc = index.get_filter_facet(facet + ".keyword", amount, facet_filter)
    return json.dumps(ret_struc)

@app.route("/browse", methods=['POST'])
def browse():
    struc = request.get_json()
    ret_struc = index.browse(struc["page"], struc["page_length"], struc["sortorder"] + ".keyword", struc["searchvalues"], struc["index"])
    return json.dumps(ret_struc)

@app.route("/get_store")
def get_store():
    store = Store()
    return store.get_data()

@app.route("/get_entities/<ds>", methods=["GET"])
def get_entities(ds):
    result = tb.get_colls(ds)
    query = {"query": result}
    return json.dumps(result)

@app.route("/get_collection_properties/<ds>/<coll>")
def get_properties(ds, coll):
    result = tb.get_props(ds, coll)
    return json.dumps(result)



#Start main program

if __name__ == '__main__':
    app.run()

