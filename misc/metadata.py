import json

class MetaData:

    def __init__(self):
        self.metadata = {
            "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__rijksmuseum" : {
                        "title": "Rijksmuseum Collection",
                        "description": "This dataset is a copy of the Europeana Data Model dump of the Rijksmuseum Collection data that can be downloaded at https://data.rijksmuseum.nl/object-metadata/download/. \n\nThe data published by the Golden Agents project is a copy dated 17th February 2021 - the only editing done is replacing the AAT-Ned Thesaurus, http://www.aat-ned.nl/ (offline and lost since 16-11-2020) with the Getty AAT Thesaurus, http://vocab.getty.edu/aat/.",
                        "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/67/Rijks_museum_logo.png",
                        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
                        "publisher": "Golden Agents project",
                        "creator": "Rijksmuseum",
                        "contributor": "",
                        "dataProvider": "Rijksmuseum",
                        "subject": "",
                        "source": "https://data.rijksmuseum.nl/object-metadata/download/",
                        "created": "2021-02-17",
                        "modified": "2021-02-17",
                        "sparqlEndpoint": ""
                    },
            "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__stcn" :  {
                "title": "Short-Title Catalogue Netherlands (STCN)",
                "description": "Expert descriptions of books printed in the Netherlands between 1473 and 1801 in more than 210.000 editions in 550.000 copies. Contains descriptions of books in the collections of many libraries in the Netherlands and various libraries abroad. All books are described book in hand. Descriptions contain information about authors, titles, imprints, size, collation formula, subject keywords and typographical features. Every edition is distinguished by the STCN fingerprint. Newspapers and ambassadors’ letters are excluded. \n\nThis dataset is a https://schema.org/ copy of the STCN datadump (http://data.bibliotheken.nl/id/dataset/stcn), the STCN Printers (http://data.bibliotheken.nl/id/dataset/stcn/printers) and the STCN Thesauri (http://data.bibliotheken.nl/id/dataset/stcn/thes) from 2022-04-29. ",
                "imageUrl": "https://www.kb.nl/kbhtml/stcnhandleiding/logo.jpg",
                "license": "https://creativecommons.org/publicdomain/zero/1.0/",
                "publisher": "Golden Agents project",
                "creator": "Koninklijke Bibliotheek",
                "contributor": "Golden Agents project",
                "dataProvider": "Koninklijke Bibliotheek",
                "subject": "book production",
                "source": "http://data.bibliotheken.nl/id/dataset/stcn",
                "created": "2022-04-29",
                "modified": "2022-04-29",
                "sparqlEndpoint": ""
            },
            "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__schrijverskabinet": {
                "title": "Schrijverskabinet",
                "description": "The Panpoëticon Batavûm is a collection of small portraits of Dutch poets (and writers in general). The collection was set up at the beginning of the eighteenth century by the painter Arnoud Halen (1673-1732). As a collection the Panpoëticon is no longer intact, but fortunately a digital reconstruction can be seen at http://www.schrijverskabinet.nl/. This dataset offers a RDF version of this website, so that one can connect the entities that are included in the Schrijverskabinet to other relevant datasets that for instance include more detailed biographical information, such as ECARTICO, ONSTAGE, and Wikidata.\n\nIn this version, all URIs that were prefixed on https://data.create.humanities.uva.nl/id/ are replaced by https://data.goldenagents.org/datasets/. This is a https://schema.org version of the data.\n\nFor more information on this dataset or for citation, please refer to the paper: Nijboer, H., van Deinsen, L., van Wissen, L., Brouwer, J., van Strien, T., & Blom, F. (2021). Using Linked Data to Track and Trace Processes of Canonization in early Modern Dutch Literature. DH Benelux Journal, 3, 39-59. https://doi.org/10.17613/p3z7-4c05",
                "imageUrl": "http://www.schrijverskabinet.nl/wp-content/uploads/2015/10/tijdlijn-onderhandse-verkoop.jpg",
                "license": "https://creativecommons.org/licenses/by-sa/4.0/",
                "publisher": "Golden Agents project",
                "creator": "Harm Nijboer, Leon van Wissen",
                "contributor": "Lieke van Deinsen, Ton van Strien",
                "dataProvider": "http://schrijverskabinet.nl/",
                "subject": "canonization",
                "source": "https://doi.org/10.5281/zenodo.4727106",
                "created": "2020-05-29",
                "modified": "2021-04-29",
                "sparqlEndpoint": ""
            },
            "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__notarissennetwerk" : {
                "title": "Notarissen netwerk",
                "description": "Description upcoming..",
                "imageUrl": "http://www.schrijverskabinet.nl/wp-content/uploads/2015/10/tijdlijn-onderhandse-verkoop.jpg",
                "license": "https://creativecommons.org/licenses/by-sa/4.0/",
                "publisher": "Upcoming..",
                "creator": "Upcoming..",
                "contributor": "Upcoming..",
                "dataProvider": "Upcoming..",
                "subject": "Upcoming..",
                "source": "Upcoming..",
                "created": "2020-05-29",
                "modified": "2021-04-29",
                "sparqlEndpoint": ""
            },
            "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__jaikwil" : {
                "title": "Ja, ik wil!",
                "description": "Description upcoming..",
                "imageUrl": "http://www.schrijverskabinet.nl/wp-content/uploads/2015/10/tijdlijn-onderhandse-verkoop.jpg",
                "license": "https://creativecommons.org/licenses/by-sa/4.0/",
                "publisher": "Upcoming..",
                "creator": "Upcoming..",
                "contributor": "Upcoming..",
                "dataProvider": "Upcoming..",
                "subject": "Upcoming..",
                "source": "Upcoming..",
                "created": "2020-05-29",
                "modified": "2021-04-29",
                "sparqlEndpoint": ""
            }
        }

    def get_metadata(self, set):
        if set == "all":
            return json.dumps(self.send_metadata_list())
        try:
            return json.dumps(self.metadata[set])
        except:
            return json.dumps({})

    def send_metadata_list(self):
        return [
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__jaikwil",
                "metadata": {
                    "title": "Ja, ik wil!",
                    "description": [
                        "This dataset is a Golden Agents RDF conversion of the data that was collected in the Vele Handen Citizen Science-project 'Ja, ik wil!' [Yes, I do!]. The dataset contains the socio-economic data on grooms and brides that registered their marriage banns in Amsterdam for every fifth year between 1580 and 1810 in the Amsterdam marriage banns registers.",
                        "",
                        "Golden Agents has reconciled the described marriage bans to their original (scanned) source. This dataset is based on an identical earlier as CC-BY 4.0 shared spreadsheet with the project's data. See: https://doi.org/10.25397/eur.14049842.v1 for the current public version."
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "",
                    "dataProvider": "Tine de Moor, René van Weeren",
                    "subject": "Ondertrouwregisters",
                    "source": "https://doi.org/10.25397/eur.14049842.v1",
                    "created": "2020-04-29",
                    "modified": "2022-11-01",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/saa"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__saa",
                "metadata": {
                    "title": "City Archives of Amsterdam",
                    "description": "RDF dataset based on the inventories and indices of the Amsterdam City Archives. It features the persons that are indexed by the archive in relation to the registration event that they are mentioned in.\n\nIn total, twelve indices and their respective inventory information are covered:\n1. Index op notarieel archief\n2. Index op doopregisters\n3. Index op ondertrouwregisters\n4. Index op kwijtscheldingen\n5. Index op poorterboeken\n6. Index op confessieboeken\n7. Index op boetes op trouwen en begraven\n8. Index op begraafregisters voor 1811\n9. Index op overledenen gast pest werk spinhuis\n10. Index op averijgrossen\n11. Index op boedelpapieren\n12. Index op lidmatenregister doopsgezinde gemeente\n\nAll data have been converted from EAD or A2A into the Golden Agents archival ontology ROAR++. See for more information: https://github.com/knaw-huc/golden-agents-saa-pipeline/",
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "",
                    "dataProvider": "Amsterdam City Archives",
                    "subject": "Archival data",
                    "source": "https://opendata.picturae.com/organization/ams",
                    "created": "2018-11-01",
                    "modified": "2022-10-25",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/saa"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__notarissennetwerk",
                "metadata": {
                    "title": "Notary network (Notarissennetwerk)",
                    "description": [
                        "RDF version of the Notary Network (Notarissennetwerk, https://notarissennetwerk.nl/), a structured version of the Repertorium van Notarissen. The dataset is included in the Golden Agents project (https://www.goldenagents.org/). ",
                        "",
                        "The repo was forked from https://gitlab.com/uvacreate/vondel/notarissennetwerk-rdf/ and has been updated to fit in the Golden Agents infrastructure:",
                        "",
                        "* All schema.org resources now use https",
                        "* The prefix is changed from https://data.create.humanities.uva.nl/id/ to https://data.goldenagents.org/datasets/"
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "",
                    "dataProvider": "Notarissennetwerk",
                    "subject": "notaries",
                    "source": "https://doi.org/10.5281/zenodo.7278142",
                    "created": "",
                    "modified": "2022-11-03",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/notarissennetwerk"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__rijksmuseum",
                "metadata": {
                    "title": "Rijksmuseum Collection",
                    "description": [
                        "This dataset is a copy of the Europeana Data Model dump of the Rijksmuseum Collection data that can be downloaded at https://data.rijksmuseum.nl/object-metadata/download/. ",
                        "",
                        "The data published by the Golden Agents project is a copy dated 17th February 2021 - the only editing done is replacing the AAT-Ned Thesaurus, http://www.aat-ned.nl/ (offline and lost since 16-11-2020) with the Getty AAT Thesaurus, http://vocab.getty.edu/aat/."
                    ],
                    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/67/Rijks_museum_logo.png",
                    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Rijksmuseum",
                    "contributor": "",
                    "dataProvider": "Rijksmuseum",
                    "subject": "",
                    "source": "https://data.rijksmuseum.nl/object-metadata/download/",
                    "created": "2021-02-17",
                    "modified": "2021-02-17",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/rijksmuseum"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__schrijverskabinet",
                "metadata": {
                    "title": "Schrijverskabinet",
                    "description": [
                        "The Panpoëticon Batavûm is a collection of small portraits of Dutch poets (and writers in general). The collection was set up at the beginning of the eighteenth century by the painter Arnoud Halen (1673-1732). As a collection the Panpoëticon is no longer intact, but fortunately a digital reconstruction can be seen at http://www.schrijverskabinet.nl/. This dataset offers a RDF version of this website, so that one can connect the entities that are included in the Schrijverskabinet to other relevant datasets that for instance include more detailed biographical information, such as ECARTICO, ONSTAGE, and Wikidata.",
                        "",
                        "In this version, all URIs that were prefixed on https://data.create.humanities.uva.nl/id/ are replaced by https://data.goldenagents.org/datasets/. This is a https://schema.org version of the data.",
                        "",
                        "For more information on this dataset or for citation, please refer to the paper: Nijboer, H., van Deinsen, L., van Wissen, L., Brouwer, J., van Strien, T., & Blom, F. (2021). Using Linked Data to Track and Trace Processes of Canonization in early Modern Dutch Literature. DH Benelux Journal, 3, 39-59. https://doi.org/10.17613/p3z7-4c05"
                    ],
                    "imageUrl": "http://www.schrijverskabinet.nl/wp-content/uploads/2015/10/tijdlijn-onderhandse-verkoop.jpg",
                    "license": "https://creativecommons.org/licenses/by-sa/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Harm Nijboer, Leon van Wissen",
                    "contributor": "Lieke van Deinsen, Ton van Strien",
                    "dataProvider": "http://schrijverskabinet.nl/",
                    "subject": "canonization",
                    "source": "https://doi.org/10.5281/zenodo.4727106",
                    "created": "2020-05-29",
                    "modified": "2021-04-29",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/schrijverskabinet"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__corporatiestukken",
                "metadata": {
                    "title": "Amsterdam Corporate Group Portraits",
                    "description": [
                        "The Amsterdam Corporate Group Portraits dataset contains biographical information on persons depicted on institutional/corporate group portraits in the seventeenth and eighteenth century in Amsterdam.",
                        "",
                        "The original data were collected by Norbert Middelkoop and published as attachment to his dissertation Schutters, gildebroeders, regenten en regentessen (2019). The Golden Agent project took his data and heavily structured these, so that they could be used in the project's infrastructure infrastructure."
                    ],
                    "imageUrl": "https://lh3.googleusercontent.com/-sA-pF2Y-y-S52zipGtwTZ-rSVWQ9y2yJS1oya2vUjAv5yJuZa1XQEhq9JdgTVqPGa24QP8oTzD1BQ_N319WIoYm-A=s2500",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Leon van Wissen, Jirsi Reinders",
                    "contributor": "",
                    "dataProvider": "Norbert Middelkoop, University of Amsterdam",
                    "subject": "",
                    "source": "https://hdl.handle.net/11245.1/509fbcc0-8dc0-44ae-869d-2620f905092e",
                    "created": "2020-03-30",
                    "modified": "2022-11-03",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/corporatiestukken"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__ecartico",
                "metadata": {
                    "title": "ECARTICO",
                    "description": [
                        "Linking cultural industries in the early modern Low Countries, ca. 1475 - ca. 1725",
                        "",
                        "ECARTICO is a comprehensive collection of structured biographical data concerning painters, engravers, printers, book sellers, gold- and silversmiths and others involved in the ‘cultural industries’ of the Low Countries in the sixteenth and seventeenth centuries. As in other biographical databases, users can [search and browse](http://www.vondel.humanities.uva.nl/ecartico/persons/) for data on individuals or make selections of certain types of data. However, ECARTICO also allows users to [visualize and analyze](http://www.vondel.humanities.uva.nl/ecartico/analysis/) data on cultural entrepreneurs and their ‘milieus’.",
                        "",
                        "This dataset is a copy of the data hosted by the University of Amsterdam in their [Linked Open Data platform](https://lod.uba.uva.nl/CREATE/ECARTICO). "
                    ],
                    "imageUrl": "https://www.vondel.humanities.uva.nl/ecartico/images/logo.png",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Harm Nijboer",
                    "contributor": "Judith Brouwer, Marten Jan Bok",
                    "dataProvider": "CREATE, University of Amsterdam",
                    "subject": "",
                    "source": "https://vondel.humanities.uva.nl/ecartico/",
                    "created": "2011",
                    "modified": "2022-11-02",
                    "sparqlEndpoint": "http://sparql2.goldenagents.org/ecartico"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__onstage",
                "metadata": {
                    "title": "ONSTAGE",
                    "description": [
                        "Online Datasystem of Theatre in Amsterdam from the Golden Age to the present. This is your address for questions about the repertoire, performances, popularity and revenues of the cultural program in Amsterdam’s public theatre during the period 1637 - 1772. All data provided in this system links to archival source materials in contemporary administration.",
                        "",
                        "This dataset is a copy of the data hosted by the University of Amsterdam in their [Linked Open Data platform](https://lod.uba.uva.nl/CREATE/ONSTAGE)."
                    ],
                    "imageUrl": "https://www.vondel.humanities.uva.nl/onstage/images/logo.png",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Harm Nijboer",
                    "contributor": "Flans Blom, Rob van der Zalm",
                    "dataProvider": "CREATE, University of Amsterdam",
                    "subject": "",
                    "source": "https://www.vondel.humanities.uva.nl/onstage/",
                    "created": "2015",
                    "modified": "2022-11-03",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/onstage"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__nta",
                "metadata": {
                    "title": "Nederlandse Thesaurus van Auteursnamen",
                    "description": [
                        "The Dutch Thesaurus of Author names (Nederlandse Thesaurus van Auteursnamen, NTA) contains name and biographical information on persons in KB datasets.",
                        "",
                        "This dataset is a https://schema.org/ copy of the Persons datadump (http://data.bibliotheken.nl/id/dataset/persons) from 2022-09-26."
                    ],
                    "imageUrl": "",
                    "license": "http://creativecommons.org/publicdomain/zero/1.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Koninklijke Bibliotheek",
                    "contributor": "",
                    "dataProvider": "Koninklijke Bibliotheek",
                    "subject": "",
                    "source": "http://data.bibliotheken.nl/id/dataset/persons",
                    "created": "2017-05-12",
                    "modified": "2022-09-26",
                    "sparqlEndpoint": "http://sparqladmin2.goldenagents.org/repositories/stcn"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__ggd",
                "metadata": {
                    "title": "Occasional Poetry",
                    "description": [
                        "The dataset with occasional poetry (=Gelegenheidsgedichten) published in the Dutch Republic between c. 1600-1800 built by the Royal Library (KB) contains 6,906 printed poems or collections of poems on a particular type of event, such as marriage (2,433), death (1,049), or various types of anniversaries (474). Work on the dataset has been concluded by the KB, but we do know the dataset itself is not complete; occasional poetry kept in family archives, for instance, is often not included. It holds bibliographical information on a poem written for an event, together with information on the event's date and participants. Names of authors and publishers are included, be it as a textual reference only: they are not linked to a unique entity (e.g. in a thesaurus).",
                        "",
                        "We converted the GGD to RDF and modelled it similar to the STCN. We disambiguated textual references to authors and printers/publishers and connected them to existing resources for metadata: the Dutch Thesaurus of Author names (NTA) and the STCN printer thesaurus respectively. The same was done, if possible, for persons that are mentioned in relation to the event described in the poems, such as the bride and groom in case of a marriage. ",
                        "",
                        "For more information, see: https://github.com/knaw-huc/golden-agents-occasional-poetry",
                        ""
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "",
                    "dataProvider": "Koninklijke Bibliotheek",
                    "subject": "Occasional Poetry",
                    "source": "https://github.com/knaw-huc/golden-agents-occasional-poetry",
                    "created": "2021-08-25",
                    "modified": "2022-11-03",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/ggd"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__bredius",
                "metadata": {
                    "title": "Bredius excerpts",
                    "description": [
                        "Data from the RKD's Bredius Notes project, enriched with information from and links to the Golden Agents project. ",
                        "",
                        "Early 2021 the RKD launched a crowdsourcing platform to digitize and index the archival material made by art historian Abraham Bredius (1855-1946), who was one of the first researchers to delve into the Dutch archives (which at the time were not open to the public), taking a systematic approach to his search for life facts about artists working between the late sixteenth and early eighteenth century. Bredius' research resulted in tens of thousands of excerpts: summaries of equally numerous archive entries, written on small scraps of paper. The data collected by Bredius still offers a wealth of information and presents an initial point of access to the original archives.",
                        "",
                        "By digitizing this material, one obtains more information on place names, dates, persons and occupations, and record types that are relevant for art historical research. Further more, the Golden Agents project integrates this dataset in RDF/LOD in its infrastructure, by which it offers a researcher additional context on this material, for instance by reconciling it with the original (digitized/indexed) material that is kept in the Amsterdam City Archives, but also by connecting the actors that are described to other (biographical) datasets, leading to a more accessible entry to information on the lifes of both producers and consumers of creative goods in seventeenth and eighteenth century Amsterdam.",
                        "",
                        "More information on the notes and the crowdsourcing project can be read on the website of the RKD: https://rkd.nl/en/projects-publications/projects/916-bredius-notes. Documentation on the data transformation and the reconciliation to the original sources can be found in: https://doi.org/10.5281/zenodo.7271871"
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "RKD",
                    "dataProvider": "RKD",
                    "subject": "Abraham Bredius",
                    "source": "https://doi.org/10.5281/zenodo.7271871",
                    "created": "2022-11-01",
                    "modified": "2022-11-01",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/bredius"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__stcn",
                "metadata": {
                    "title": "Short-Title Catalogue Netherlands (STCN)",
                    "description": [
                        "Expert descriptions of books printed in the Netherlands between 1473 and 1801 in more than 210.000 editions in 550.000 copies. Contains descriptions of books in the collections of many libraries in the Netherlands and various libraries abroad. All books are described book in hand. Descriptions contain information about authors, titles, imprints, size, collation formula, subject keywords and typographical features. Every edition is distinguished by the STCN fingerprint. Newspapers and ambassadors’ letters are excluded. ",
                        "",
                        "This dataset is a https://schema.org/ copy of the STCN datadump (http://data.bibliotheken.nl/id/dataset/stcn), the STCN Printers (http://data.bibliotheken.nl/id/dataset/stcn/printers) and the STCN Thesauri (http://data.bibliotheken.nl/id/dataset/stcn/thes) from 2022-04-29. "
                    ],
                    "imageUrl": "https://www.kb.nl/kbhtml/stcnhandleiding/logo.jpg",
                    "license": "http://creativecommons.org/publicdomain/zero/1.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Koninklijke Bibliotheek",
                    "contributor": "Golden Agents project",
                    "dataProvider": "Koninklijke Bibliotheek",
                    "subject": "book production",
                    "source": "http://data.bibliotheken.nl/id/dataset/stcn",
                    "created": "2022-04-29",
                    "modified": "2022-04-29",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/stcn"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__htr",
                "metadata" : {
                    "title": "Golden Agents HTR - Amsterdam City Archives",
                    "description": [
                        "This dataset contains the Named Entity Recognition output done on the HTR from the Amsterdam City Archives. For deeds of type Probate Inventory, Last Will and Prenuptial Agreement the Analiticcl tool (https://github.com/proycon/analiticcl) was run on the material. The result is modelled as Web Annotations that point to a specific scan from the archive.  ",
                        "",
                        "For more information, see: https://github.com/knaw-huc/golden-agents-htr",
                        "",
                        ""
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "",
                    "dataProvider": "Amsterdam City Archives",
                    "subject": "probate inventories",
                    "source": "https://github.com/knaw-huc/golden-agents-htr",
                    "created": "2022-10-21",
                    "modified": "2022-10-21",
                    "sparqlEndpoint": "https://sparql2.goldenagents.org/saa"
                }
            },
            {
                "dataset": "u692bc364e9d7fa97b3510c6c0c8f2bb9a0e5123b__poc",
                "metadata": {
                    "title": "Processes of Creativity",
                    "description": [
                        "Data of the 'Processes of Creativity' case study. ",
                        "",
                        "We can observe a 'rise' of or 'renewed interest' in the illustrated book in the second half of 17th century and the beginning of the 18th century. New genres and techniques and an increasing competition in the book market lead to new collaborations between authors, printers, and illustrators. It would be interesting to track these producers who collaborated on illustrated book projects and trace whether these commercial collaborations were grounded or resulted in social and/or religious interactions. For this, we are bringing together several datasets in the Golden Agents infrastructure that each contain information on the production of books, or on social relations between actors involved in the production process.",
                        "",
                        "Aim of case study:",
                        "",
                        "Linking & querying different datasets to find overarching patterns on creative industries in the Dutch Republic",
                        "Overarching Research Question:",
                        "",
                        "How can we map innovation in cultural production?",
                        "What is the relation between different sorts (bonding & bridging) of creative and social interactions?"
                    ],
                    "imageUrl": "",
                    "license": "https://creativecommons.org/licenses/by/4.0/",
                    "publisher": "Golden Agents project",
                    "creator": "Golden Agents project",
                    "contributor": "Iman Hashemi",
                    "dataProvider": "Rijksmuseum Library, ECARTICO, Ja, ik wil!, STCN",
                    "subject": "Illustrated books",
                    "source": "https://github.com/knaw-huc/golden-agents-processes-of-creativity/",
                    "created": "2021-08-25",
                    "modified": "2022-11-07",
                    "sparqlEndpoint": "http://sparqladmin2.goldenagents.org/repositories/poc"
                }
            }

        ]