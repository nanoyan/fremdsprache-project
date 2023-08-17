import json
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS, XSD, NamespaceManager
from otsrdflib import OrderedTurtleSerializer
from pathlib import Path
import os.path

core = Namespace('https://w3id.org/iqb/mdc-core/cs_')
lrmi = Namespace('http://purl.org/dcx/lrmi-terms/')
oeh_md = Namespace('http://w3id.org/openeduhub/learning-resource-terms/')
source = Namespace('https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2023/2023_06_22-Bista-ESA-MSA-ErsteFremdsprache.pdf')


def buildGraph(input_file, output_folder):
    with open(input_file, 'r',  encoding='utf-8') as f:
        data = json.load(f)
    
    head, tail= os.path.split(input_file)
    url_id = tail.split('.')[0]

    if(data['children']):
        for c in data['children']:
            base_url = URIRef("https://w3id.org/iqb/" + url_id + "/" + c['id']  + "/")
            title = data['title'] + '_' + c['title']
            g = Graph(base = base_url)
            g.add((base_url, RDF.type, SKOS.ConceptScheme))
            g.add((base_url, DCTERMS.title, Literal(title, lang="de")))
            if "description" in data:
                g.add((base_url, DCTERMS.description, Literal(data['description'], lang="de")))
            g.add((base_url, DCTERMS.creator, Literal("IQB - Institut zur Qualitätsentwicklung im Bildungswesen", lang="de"))) 
            g.add((base_url,DCTERMS.source, Literal('https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2023/2023_06_22-Bista-ESA-MSA-ErsteFremdsprache.pdf', lang="de") ))

            if "children" in c:
                for cc in c['children']:
                    cc_url = URIRef(cc['id'])
                    g.add((cc_url, RDF.type, SKOS.Concept))
                    g.add((cc_url, SKOS.prefLabel, Literal(cc['notation'] +". "+ cc['title'], lang="de")))
                    g.add((cc_url, SKOS.notation, Literal(cc['notation'])))
                    # if "description" in cc:
                    #     g.add((cc_url, SKOS.definition, Literal(cc['description'], lang="de")))
                    # g.add((cc_url, SKOS.inScheme, base_url))
                    g.add((base_url, SKOS.hasTopConcept, cc_url))
                    g.add((cc_url, SKOS.topConceptOf, base_url))
                    if "children" in cc:
                     
                        for ccc in cc['children']:
                            ccc_url = URIRef(ccc['id'])
                            g.add((ccc_url, RDF.type, SKOS.Concept))
                            g.add((ccc_url, SKOS.prefLabel, Literal(ccc['notation'] +". "+ ccc['title'], lang="de")))
                            g.add((ccc_url, SKOS.notation, Literal(ccc['notation'])))
                            #if "description" in ccc:
                            #    g.add((ccc_url, SKOS.definition, Literal(ccc['description'], lang="de")))
                            #g.add((ccc_url, SKOS.inScheme, base_url))
                            g.add((ccc_url, SKOS.broader, cc_url))
                            g.add((cc_url, SKOS.narrower, ccc_url))
                            g.add((ccc_url, SKOS.inScheme, base_url))
                            if "children" in ccc:
                                
                                for cccc in ccc['children']:
                                    cccc_url = URIRef(cccc['id'])
                            #         g.add((cccc_url, SKOS.notation, Literal(cccc['notation'])))
                                    g.add((cccc_url, RDF.type, SKOS.Concept))
                                    g.add((cccc_url, SKOS.prefLabel, Literal(cccc['notation'] +". "+ cccc['title'], lang="de")))
                                    g.add((cccc_url, SKOS.notation, Literal(cccc['notation'])))
                                    g.add((cccc_url, SKOS.inScheme, base_url))
                                    g.add((cccc_url, SKOS.broader, ccc_url)) 
                                    g.add((ccc_url, SKOS.narrower, cccc_url))
                            #         if "description" in cccc:
                            #             g.add((cccc_url, SKOS.definition, Literal('description', lang="de")))
                            #         g.add((ccc_url, SKOS.narrower, cccc_url))
                                  
                            #         g.add((cccc_url, SKOS.broader, ccc_url))
                                                      
        

            outfile_path = os.path.join(output_folder, ("iqb_" + data['title'] + '_' + c['id'] + ".ttl"))
            serializer = OrderedTurtleSerializer(g)
            
            #print(type(serializer.topClasses[0]))

            serializer.sorters = {
                ('/^[0-9]+(\.[0-9]+)*$/', lambda x: x),
                ('.', lambda x: 0.0),  # default
            }

            serializer.class_order = [
                SKOS.notation,
            ]


            with open (outfile_path,'wb') as fp:
                serializer.serialize(fp)
