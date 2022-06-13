import requests
import json
import sys

from queries import timbuctoo_queries, timbuctoo_fragments

class Timbuctoo_handler:
    def __init__(self):
        self.server = "https://repository.goldenagents.org/v5/graphql"
        self.tq = timbuctoo_queries.Timbuctoo_queries()
        self.tf = timbuctoo_fragments.Timbuctoo_fragments()
        self.normalized_props = {}
        self.unique_props = {'title': {'shortendedUri': 'title'}}



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

    def get_prefixes(self, dataset):
        query = self.tq.get_dataset_prefixes(dataset)
        return self.fetch_data(query)



    def create_field_query(self, item):
        if item["isList"]:
            if len(item["referencedCollections"]["items"]) > 1:
                return self.tf.entity_list(item["name"])
            else:
                if item["isValueType"]:
                    return self.tf.default_value_list(item["name"])
                else:
                    return self.tf.uri_title_value_list(item["name"])
        else:
            if len(item["referencedCollections"]["items"]) > 1:
                return self.tf.entity(item["name"])
            else:
                if item["isValueType"]:
                    if len(item["referencedCollections"]["items"]) == 1:
                        return self.tf.entity(item["name"])
                    else:
                        return self.tf.default_value(item["name"])
                else:
                    return self.tf.uri_title_value(item["name"])


    def value_extractor(self, props):
        subquery = "title {value} "
        for item in props["data"]["dataSetMetadata"]["collection"]["properties"]["items"]:
            subquery = subquery + self.create_field_query(item)
        return subquery


    def build_query(self, dataset, collection, uri):
        props = self.get_props(dataset, collection)
        self.normalize_props(props)
        values = self.value_extractor(props)
        query = self.tf.get_item(dataset, collection, uri, values)
        return query

    def normalize_props(self, props):
        for item in props["data"]["dataSetMetadata"]["collection"]["properties"]["items"]:
            self.normalized_props[item["name"]] = item

    def get_value(self, item):
        if "uri" in item.keys():
            return item["title"]["value"]
        else:
            try:
                return item["value"]
            except:
                return ""

    def humanify_notion(self, field):
        #ret_value = field.replace("_inverse_", "")
        #ret_value = ret_value.replace("List", "")
        #ret_value = ret_value.replace("schema_", "")
        if field != 'title':
            if self.normalized_props[field]["shortenedUri"]:
                label = self.normalized_props[field]["shortenedUri"]
            else:
                label = field

            labelTruncs = label.split(':')
            if labelTruncs[-1]:
                return labelTruncs[-1]
            else:
                return label
        else:
            return field

    def put_list_values(self, field, data):
        values = []
        for item in data["items"]:
            values.append(self.get_value(item))
        return {"notion": field, "label": self.humanify_notion(field), "values": values}


    def unify_data(self, field, data, pref_list, human = True):
        if data == None:
            return {"notion": field, "label": self.humanify_notion(field), "values": []}
        else:
            if "items" in data.keys():
                return self.extract_list(field, data)
            else:
                values = []
                if field == "rdf_type" and human:
                    rtype = self.humanize_rdf_type(self.get_value(data))
                    values.append(rtype)
                else:
                    values.append(self.get_value(data))
                return {"notion": field, "label": self.humanify_notion(field), "values": values}

    def humanize_rdf_type(self, value):
        type = value.split("/");
        if type[-1]:
            return type[-1]
        else:
            return ""

    def extract_list(self, field, data):
        if field == "rdf_typeList":
            return self.put_rdf_type_list(field, data)
        else:
            return self.put_list_values(field, data)

    def put_rdf_type_list(self, field, data):
        values = []
        for item in data["items"]:
            if "uri" in item.keys():
                rdf_type = item["uri"].split("/")
                if rdf_type[-1] not in values:
                    values.append(rdf_type[-1])
        return {"notion": field, "label": self.humanify_notion(field), "values": values}

    def model_results(self, dataset, collection, result, list):
        items = []
        for field in result["data"]["dataSets"][dataset][collection]:
            items.append(self.unify_data(field, result["data"]["dataSets"][dataset][collection][field], list))
        return items

    def undouble_items(self, list):
        labels = []
        retList = []
        for item in list:
            if item["label"] not in labels:
                labels.append(item["label"])
                retList.append(item)
        return retList

    def rdf_label_as_title(self, title, items):
        ret_title = title
        for item in items:
            if item["notion"] == "rdfs_label":
                ret_title = item["values"][0]
        return ret_title

    def create_adressed_prefixes(self, dataset):
        prefixes = self.get_prefixes(dataset)
        prefixList = {}
        for item in prefixes["data"]["dataSetMetadata"]["prefixMappings"]:
            prefixList[item["uri"]] = item["prefix"]
        return prefixList

    def strip_prefixes(self, dataset, list):
        prefixes = self.get_prefixes(dataset)
        for item in list:
            if item["values"]:
                for i in range(len(item["values"])):
                    value = self.check_prefixes(item["values"][i], prefixes)
                    if value != item["values"][i]:
                        item["values"][i] = value

    def check_prefixes(self, val, prefixes):
        retval = val
        if "http://" in val or "https://" in val:
            for prefix in prefixes["data"]["dataSetMetadata"]["prefixMappings"]:
                if val.startswith(prefix["uri"]):
                    print('Bingo')
                    print(val)
                    retval = val.replace(prefix["uri"], "")
                    print(retval)
        return retval


    def get_item(self, dataset, collection, uri):
        query = self.build_query(dataset, collection, uri)
        #print(query)
        list = self.create_adressed_prefixes(dataset)
        result = self.fetch_data(query)
        items = self.model_results(dataset, collection, result, list)
        tmp = items.pop(0);
        title = tmp["values"][0]
        title = self.rdf_label_as_title(title, items)
        return {"title": title, "uri": uri, "items": items}

    def get_human_item(self, dataset, collection, uri):
        query = self.build_query(dataset, collection, uri)
        list = self.create_adressed_prefixes(dataset)
        result = self.fetch_data(query)
        items = self.model_results(dataset, collection, result, list)
        items = self.undouble_items(items)
        self.strip_prefixes(dataset, items)
        tmp = items.pop(0);
        title = tmp["values"][0]
        title = self.rdf_label_as_title(title, items)
        return {"title": title, "uri": uri, "items": items}


