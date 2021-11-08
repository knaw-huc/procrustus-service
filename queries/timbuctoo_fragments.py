class Timbuctoo_fragments:
    def default_value(self, field):
        return " " + field + " {value} "

    def default_value_list(self, field):
        return " " + field + " {items {value}} "

    def entity(self, field):
        return " " + field + " {... on Entity {uri title {value}} "

    def entity_list(self, field):
        return " " + field + " {items { ... on Entity {uri title {value}}}} "

    def uri_title_value(self, field):
        return " " + field + " { uri title {value}} "

    def uri_title_value_list(self, field):
        return " " + field + " {items {uri title {value}}} "

    def get_item(self, dataset, collection, uri, fields):
        return "{dataSets {" + dataset + " {" + collection + '(uri: "' + uri + '") {' + fields + "}}}}"
