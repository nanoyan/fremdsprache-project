import json
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS, XSD, NamespaceManager
from otsrdflib import OrderedTurtleSerializer
from pathlib import Path
import os.path

core = Namespace('https://w3id.org/iqb/mdc-core/cs_')
lrmi = Namespace('http://purl.org/dcx/lrmi-terms/')
oeh_md = Namespace('http://w3id.org/openeduhub/learning-resource-terms/')


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
            if "children" in c:
                for cc in c['children']:
                    cc_url = URIRef(cc['id'])
                    g.add((cc_url, RDF.type, SKOS.Concept))
                    if "title" in cc:
                        g.add((cc_url, SKOS.prefLabel, Literal(cc['title'], lang="de")))
                    if cc["notation"] != "None":
                        g.add((cc_url, SKOS.notation, Literal(cc['notation'])))
                    g.add((base_url, SKOS.hasTopConcept, cc_url))
                    g.add((cc_url, SKOS.topConceptOf, base_url))
                    if "children" in cc:                     
                        for ccc in cc['children']:
                            ccc_url = URIRef(ccc['id'])
                            g.add((ccc_url, RDF.type, SKOS.Concept))
                            if "title" in ccc:
                                g.add((ccc_url, SKOS.prefLabel, Literal(ccc['title'], lang="de")))
                            if ccc["notation"] != "None":
                                g.add((ccc_url, SKOS.notation, Literal(ccc['notation'])))
                            if "description" in ccc:
                                g.add((ccc_url, SKOS.definition, Literal(ccc['description'], lang="de")))
                            g.add((ccc_url, SKOS.broader, cc_url))
                            g.add((cc_url, SKOS.narrower, ccc_url))
                            g.add((ccc_url, SKOS.inScheme, base_url))
                            if "children" in ccc:                                
                                for cccc in ccc['children']:
                                    cccc_url = URIRef(cccc['id'])
                                    if cccc["notation"] != "None":
                                        g.add((cccc_url, SKOS.notation, Literal(cccc['notation'])))
                                    if "description" in cccc:
                                        g.add((cccc_url, SKOS.definition, Literal(cccc['description'], lang="de")))    
                                    g.add((cccc_url, RDF.type, SKOS.Concept))
                                    if "title" in cccc:
                                        g.add((cccc_url, SKOS.prefLabel, Literal(cccc['title'], lang="de")))
                                    g.add((cccc_url, SKOS.inScheme, base_url))
                                    g.add((cccc_url, SKOS.broader, ccc_url)) 
                                    g.add((ccc_url, SKOS.narrower, cccc_url))
        
            outfile_path = os.path.join(output_folder, ("iqb_" + data['title'] + '_' + c['id'] + ".ttl"))
            
            # Using this serializer order just the first layer
            # serializer = OrderedTurtleSerializer(g)
            # serializer.sorters = {
            #     ('.*?/[A-Za-z]+([0-9.]+)$', lambda x: float(x[0])),
            #     ('.', lambda x: 0.0),  # default
            # }
            # serializer.class_order = [
            #     SKOS.notation,
            # ]
            # with open (outfile_path,'wb') as fp:
            #     serializer.serialize(fp)
            g.serialize(str(outfile_path), format="turtle", base=base_url, encoding="utf-8")              