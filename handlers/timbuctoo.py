import json
import requests

from queries import timbuctoo_queries

class Timbuctoo_handler:
    def __init__(self):
        self.server = "https://repository.goldenagents.org/v5/graphql"
        self.tq = timbuctoo_queries.Timbuctoo_queries()


    def fetch_data(self, query):
        params = {"query": query}
        results = requests.post(self.server, json = params, headers = {'Content-Type': 'application/json',
                                                                       "VRE_ID": "ufab7d657a250e3461361c982ce9b38f3816e0c4b__ecartico_20200316"})
        return json.loads(results.text)

    def get_colls(self, dataset):
        query = self.tq.get_collections(dataset)
        return self.fetch_data(query)

    def get_props(self, dataset, collection):
        query = self.tq.get_collection_properties(dataset, collection)
        return self.fetch_data(query)

    def build_query(self, dataset, collection, uri):
        props = self.get_props(dataset, collection)

