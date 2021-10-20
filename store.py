import json

class Store:

    def get_data(self):
        store = { "dataSets": [
                {
                    "dataSet": "ufab7d657a250e3461361c982ce9b38f3816e0c4b__ecartico_20200316",
                    "label": "CREATE: Ecartico",
                    "indexes": [
                        {
                            "collection": "ecartico_20200316_schema_person",
                            "label": "Persons"
                        },
                        {
                            "collection": "ecartico_20200316_http___purl_org_vocab_bio_0_1_marriage",
                            "label": "Marriages"
                        },
                        {
                            "collection": "ecartico_20200316_schema_article",
                            "label": "Articles"
                        },
                        {
                            "collection": "ecartico_20200316_schema_occupation",
                            "label": "Occupations"
                        },
                        {
                            "collection": "ecartico_20200316_schema_publicationissue",
                            "label": "Publication issues"
                        },
                        {
                            "collection": "ecartico_20200316_schema_role",
                            "label": "Roles"
                        }]
                },
                {
                    "dataSet": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__ga_stcn_rmlibrary_20210908",
                    "label": "Rijksmuseum Library (STCN part)",
                    "indexes": [
                        {
                            "collection": "ga_stcn_rmlibrary_20210908_schema_person",
                            "label": "Persons"
                        },
                        {
                            "collection": "ga_stcn_rmlibrary_20210908_schema_book",
                            "label": "Books"
                        },
                        {
                            "collection": "ga_stcn_rmlibrary_20210908_schema_productmodel",
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
                            "label": "Persons"
                        },
                        {
                            "collection": "stcn_20200226_schema_place",
                            "label": "Places"
                        },
                        {
                            "collection": "stcn_20200226_schema_organization",
                            "label": "Organisations"
                        }
                    ]
                }
        ]}
        return json.dumps(store)