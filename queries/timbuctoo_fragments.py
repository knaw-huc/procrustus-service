class Timbuctoo_fragments:
    def default_value(self, field):
        return " " + field + " {value} "

    def default_value_list(self, field):
        return " " + field + " {items {value}}"

    def entity(self, field):
        return " " + field + " ...on Entity"