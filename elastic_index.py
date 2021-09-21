from elasticsearch import Elasticsearch

class Index:
    def __init__(self, config):
        self.config = config
        self.es = Elasticsearch([{"host": self.config["url"], "port": self.config["port"]}])
        self.client = Elasticsearch()

    def get_facet(self, field, amount):
        ret_array = []
        response = self.client.search(
            index="ecodices",
            body=
                {
                    "size": 0,
                    "aggs": {
                        "names": {
                            "terms": {
                                "field": field,
                                "size": amount,
                                "order": {
                                    "_count": "desc"
                                }
                            },
                            "aggs": {
                                "byHash": {
                                    "terms": {
                                        "field": "hash"
                                    }
                                }
                            }
                        }
                    }
                }
        )
        for hits in response["aggregations"]["names"]["buckets"]:
            buffer = {"key": hits["key"], "doc_count": hits["doc_count"]}
            ret_array.append(buffer)
        return ret_array

    






