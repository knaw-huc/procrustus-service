import json
from store import Store

from elasticsearch import Elasticsearch
import math

class Index:
    def __init__(self, config):
        self.config = config
        self.es = Elasticsearch([{"host": self.config["url"], "port": self.config["port"]}])
        self.client = Elasticsearch()

    def no_case(self, str_in):
        str = str_in.strip()
        ret_str = ""
        if (str != ""):
            for char in str:
                ret_str = ret_str + "[" + char.upper() + char.lower() + "]"
        return ret_str + ".*"


    def get_switch(self, uri):
        response = self.client.search(
            index='*',
            body ={
                "query": {
                    "match": {
                        "uri.keyword": uri
                    }
                },
                "_source": ["uri", "title"]
            }
        )
        ret_array = []
        for hit in response["hits"]["hits"]:
            buffer = {}
            buffer["index"] = hit["_index"]
            buffer["title"] = hit["_source"]["title"]
            buffer["uri"] = hit["_source"]["uri"]
            buffer["tb"] = self.get_labels(hit["_index"])
            ret_array.append(buffer)
        return ret_array

    def get_labels(self, indexName):
        store = Store()
        data = store.get_data()
        for ds in data["dataSets"]:
            for coll in ds["indexes"]:
                if coll["collection"] == indexName:
                    return {
                        "dataSet": ds["dataSet"],
                        "label": ds["label"],
                        "index": coll
                    }
        return {}






    def browse(self, page, length, orderFieldName, searchvalues, index):
        int_page = int(page)
        start = (int_page -1) * length
        matches = []

        if searchvalues == "none":
            response = self.client.search(
                index=index,
                body={ "query": {
                    "match_all": {}},
                    "size": length,
                    "from": start,
                    "_source": ["uri", "title"],
                    "sort": [
                        { "title.keyword": {"order":"asc"}}
                    ]
                }
            )
        else:
            for item in searchvalues:
                for value in item["values"]:
                    if item["field"] == "FREE_TEXT":
                        matches.append({"multi_match": {"query": value, "fields": ["*"]}})
                    else:
                        matches.append({"match": {item["field"] + ".keyword": value}})

            response = self.client.search(
                index=index,
                body={ "query": {
                    "bool": {
                        "must": matches
                    }},
                    "size": length,
                    "from": start,
                    "_source": ["uri", "title"],
                    "sort": [
                        { "title.keyword": {"order":"asc"}}
                    ]
                }
            )
        ret_array = {"amount" : response["hits"]["total"]["value"], "pages": math.ceil(response["hits"]["total"]["value"] / length) ,"items": []}
        for item in response["hits"]["hits"]:
            ret_array["items"].append(item["_source"])
        return ret_array







