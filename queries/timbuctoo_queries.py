class Timbuctoo_queries:
    def get_collections(self, dataset_id):
        return '{dataSetMetadata(dataSetId: "' + dataset_id + '") {dataSetId dataSetName collectionList {items {collectionId collectionListId shortenedUri itemType total title {value}}}}}'

    def get_basic_collection_items(self, dataset_id, collection_id, count, cursor=""):
        if cursor == "":
            return '{dataSets {' + dataset_id + ' {' + collection_id +  '(count: ' + count + ') {total prevCursor nextCursor items {uri title {value}}}}}}'
        else:
            return '{dataSets {' + dataset_id + ' {' + collection_id +  '(cursor: "' + cursor + '" count: ' + count + ') {total prevCursor nextCursor items {uri title {value}}}}}}'

    def get_collection_properties(self, dataset_id, collection):
        return '{dataSetMetadata(dataSetId: "' + dataset_id + '") {collection(collectionId: "' + collection + '") {uri shortenedUri title {value} properties {items { uri name  shortenedUri isList isValueType isInverse  referencedCollections {items}}}}}}'

    def get_dataset_prefixes(selfself, dataset_id):
        return '{dataSetMetadata(dataSetId: "' + dataset_id + '") { prefixMappings {prefix uri}}}'
