import json


class Store:

    def get_data(self):
        store = {"dataSets": [
            {
                "dataSet": "ufab7d657a250e3461361c982ce9b38f3816e0c4b__ecartico_20200316",
                "label": "CREATE: Ecartico",
                "indexes": [
                    {
                        "collection": "ecartico_20200316_schema_article",
                        "collection_id": "schema_Article",
                        "label": "Articles"
                    },
                    {
                        "collection": "ecartico_20200316_http___purl_org_vocab_bio_0_1_marriage",
                        "collection_id": "http___purl_org_vocab_bio_0_1_Marriage",
                        "label": "Marriages"
                    },
                    {
                        "collection": "ecartico_20200316_schema_person",
                        "collection_id": "schema_Person",
                        "label": "Persons"
                    },
                    {
                        "collection": "ecartico_20200316_schema_occupation",
                        "collection_id": "schema_Occupation",
                        "label": "Occupations"
                    },
                    {
                        "collection": "ecartico_20200316_schema_publicationissue",
                        "collection_id": "schema_PublicationIssue",
                        "label": "Publication issues"
                    },
                    {
                        "collection": "ecartico_20200316_schema_role",
                        "collection_id": "schema_Role",
                        "label": "Roles"
                    }]
            },
            {
                "dataSet": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__ga_stcn_rmlibrary_20210908",
                "label": "Rijksmuseum Library (STCN part)",
                "indexes": [
                    {
                        "collection": "ga_stcn_rmlibrary_20210908_schema_person",
                        "collection_id": "schema_Person",
                        "label": "Persons"
                    },
                    {
                        "collection": "ga_stcn_rmlibrary_20210908_schema_book",
                        "collection_id": "schema_Book",
                        "label": "Books"
                    },
                    {
                        "collection": "ga_stcn_rmlibrary_20210908_schema_productmodel",
                        "collection_id": "schema_ProductModel",
                        "label": "Product models"
                    }
                ]
            },
            {
                "dataSet": "ufab7d657a250e3461361c982ce9b38f3816e0c4b__stcn_20200226",
                "label": "Koninklijke Bibliotheek: STCN",
                "indexes": [
                    {
                        "collection": "stcn_20200226_schema_person",
                        "collection_id": "schema_Person",
                        "label": "Persons"
                    },
                    {
                        "collection": "stcn_20200226_schema_place",
                        "collection_id": "schema_Place",
                        "label": "Places"
                    },
                    {
                        "collection": "stcn_20200226_schema_organization",
                        "collection_id": "schema_Organization",
                        "label": "Organisations"
                    }
                ]
            },
            {
                "dataSet": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__middelkoop_20211104",
                "label": "Middelkoop",
                "indexes": [
                    {
                        "collection": "middelkoop_20211104_ga_person",
                        "collection_id": "ga_Person",
                        "label": "Persons"
                    },
                    {
                        "collection": "middelkoop_20211104_ga_creativeartifact",
                        "collection_id": "ga_CreativeArtifact",
                        "label": "Creative artefacts"
                    }
                ]
            }
        ]}
        return json.dumps(store)
