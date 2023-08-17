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
    print(url_id)

    if("dimensions" in data):
        for dimension in data['dimensions']:
            g = Graph(base = "https://w3id.org/iqb/" + url_id + "/" + dimension['id']  + "/")
            g.add((base_url, RDF.type, SKOS.ConceptScheme))
            g.add((base_url, DCTERMS.creator, Literal("IQB - Institut zur Qualitätsentwicklung im Bildungswesen", lang="de")))
            title = data['title'] + '_' + dimension['title']
            g.add((base_url, DCTERMS.title, Literal(title, lang="de")))
            if "description" in data:
                g.add((base_url, DCTERMS.description, Literal(data['description'], lang="de")))
            g.bind("skos", SKOS)
            g.bind("dct", DCTERMS)
            g.bind("core", core)
            g.add((base_url, SKOS.prefLabel, Literal(dimension['title'], lang="de")))
            if "description" in dimension:
                g.add((base_url, DCTERMS.description, Literal(dimension['description'], lang="de")))
            
            for c in dimension['children']:
                #child_url = URIRef(base_url + str(uuid.uuid4()))
                #child_url = URIRef(c['id'])
                child_url = URIRef(base_url + c['id'])
                g.add((base_url, SKOS.narrower, child_url))
                g.add((child_url, RDF.type, SKOS.Concept))
                g.add((child_url, SKOS.inScheme, base_url))
                g.add((base_url, SKOS.hasTopConcept, child_url))
                g.add((child_url, SKOS.topConceptOf, base_url))
                g.add((child_url, SKOS.prefLabel, Literal(c['title'], lang="de")))
                g.add((child_url, SKOS.notation, Literal(c['notation'])))
                g.add((child_url, SKOS.broader, base_url))
                if "description" in c:
                    g.add((child_url, SKOS.definition, Literal(c['description'], lang="de")))
                
                if "children" in c:
                    for cc in c['children']:
                        #cc_url = URIRef(cc['id'])
                        #cc_url = URIRef(base_url + str(uuid.uuid4()))
                        cc_url = URIRef(base_url + cc['id'])
                        g.add((child_url, SKOS.narrower, cc_url))
                        g.add((cc_url, RDF.type, SKOS.Concept))
                        g.add((cc_url, SKOS.inScheme, base_url))
                        g.add((cc_url, SKOS.broader, child_url))
                        g.add((cc_url, SKOS.notation, Literal(cc['notation'])))
                        g.add((cc_url, SKOS.prefLabel, Literal(cc['title'], lang="de")))
                        if "description" in cc:
                            g.add((cc_url, SKOS.definition, Literal(cc['description'], lang="de")))
                        
                        if "children" in cc:
                            for ccc in cc['children']:
                                #ccc_url = URIRef(ccc['id'])
                                #ccc_url = URIRef(base_url + str(uuid.uuid4()))
                                ccc_url = URIRef(base_url + ccc['id'])
                                g.add((cc_url, SKOS.narrower, ccc_url))
                                g.add((ccc_url, RDF.type, SKOS.Concept))
                                g.add((ccc_url, SKOS.inScheme, base_url))
                                g.add((ccc_url, SKOS.broader, cc_url))
                                g.add((ccc_url, SKOS.notation, Literal(ccc['notation'])))
                                g.add((ccc_url, SKOS.prefLabel, Literal(ccc['title'], lang="de")))
                                if "description" in ccc:
                                    g.add((ccc_url, SKOS.definition, Literal(ccc['description'], lang="de")))
                                
                                if "children" in ccc:
                                        for cccc in ccc['children']:
                                            #cccc_url = URIRef(cccc['id'])
                                            #cccc_url = URIRef(base_url + str(uuid.uuid4()))
                                            cccc_url = URIRef(base_url + cccc['id'])
                                            g.add((ccc_url, SKOS.narrower, cccc_url))
                                            g.add((cccc_url, RDF.type, SKOS.Concept))
                                            g.add((cccc_url, SKOS.inScheme, base_url))
                                            g.add((cccc_url, SKOS.broader, ccc_url))
                                            g.add((cccc_url, SKOS.notation, Literal(cccc['notation'])))
                                            g.add((cccc_url, SKOS.prefLabel, Literal(cccc['title'], lang="de")))
                                            if "description" in cccc:
                                                g.add((cccc_url, SKOS.definition, Literal(cccc['description'], lang="de")))
            outfile_path = output_folder / ("iqb_" + data['title'] + '_' + dimension['id'] + ".ttl")
            g.serialize(str(outfile_path), format="turtle", base=base_url, encoding="utf-8")
    elif(data['children']):
        for c in data['children']:
            g = Graph()
            base_url = URIRef("https://w3id.org/iqb/" + url_id + "/" + c['id']  + "/") 
            g.add((base_url, RDF.type, SKOS.ConceptScheme))
            g.add((base_url, DCTERMS.creator, Literal("IQB - Institut zur Qualitätsentwicklung im Bildungswesen", lang="de")))
            title = data['title'] + '_' + c['title']
            g.add((base_url, DCTERMS.title, Literal(title, lang="de")))
            if "description" in data:
                g.add((base_url, DCTERMS.description, Literal(data['description'], lang="de")))
            g.bind("skos", SKOS)
            g.bind("dct", DCTERMS)
            g.bind("core", core)
            g.add((base_url, SKOS.prefLabel, Literal(c['title'], lang="de")))
            if "description" in c:
                g.add((base_url, DCTERMS.description, Literal(c['description'], lang="de")))
                
            if "children" in c:
                for cc in c['children']:
                    #cc_url = URIRef(cc['id'])
                    #cc_url = URIRef(base_url + str(uuid.uuid4()))
                    cc_url = URIRef(base_url + cc['id'])
                    g.add((base_url, SKOS.narrower,cc_url))
                    g.add((cc_url, RDF.type, SKOS.Concept))
                    g.add((base_url, SKOS.hasTopConcept, cc_url))
                    g.add((cc_url, SKOS.inScheme, base_url))
                    g.add((cc_url, SKOS.topConceptOf, base_url))
                    g.add((cc_url, SKOS.broader, base_url))
                    g.add((cc_url, SKOS.notation, Literal(cc['notation'])))
                    g.add((cc_url, SKOS.prefLabel, Literal(cc['title'], lang="de")))
                    if "description" in cc:
                        g.add((cc_url, SKOS.definition, Literal(cc['description'], lang="de")))
                        
                    if "children" in cc:
                        for ccc in cc['children']:
                            #ccc_url = URIRef(ccc['id'])
                            #ccc_url = URIRef(base_url + str(uuid.uuid4()))
                            ccc_url = URIRef(base_url + ccc['id'])
                            g.add((cc_url, SKOS.narrower, ccc_url))
                            g.add((ccc_url, RDF.type, SKOS.Concept))
                            g.add((ccc_url, SKOS.inScheme, base_url))
                            g.add((ccc_url, SKOS.broader, cc_url))
                            g.add((ccc_url, SKOS.notation, Literal(ccc['notation'])))
                            g.add((ccc_url, SKOS.prefLabel, Literal(ccc['title'], lang="de")))
                            if "description" in ccc:
                                g.add((ccc_url, SKOS.definition, Literal(ccc['description'], lang="de")))
                                
                            if "children" in ccc:
                                for cccc in ccc['children']:
                                    #cccc_url = URIRef(cccc['id'])
                                    #cccc_url = URIRef(base_url + str(uuid.uuid4()))
                                    cccc_url = URIRef(base_url + cccc['id'])
                                    g.add((ccc_url, SKOS.narrower, cccc_url))
                                    g.add((cccc_url, RDF.type, SKOS.Concept))
                                    g.add((cccc_url, SKOS.broader, ccc_url))
                                    g.add((cccc_url, SKOS.inScheme, base_url))
                                    g.add((cccc_url, SKOS.notation, Literal(cccc['notation'])))
                                    g.add((cccc_url, SKOS.prefLabel, Literal(cccc['title'], lang="de")))
                                    if "description" in cccc:
                                        g.add((cccc_url, SKOS.definition, Literal('description', lang="de")))
            #outfile_path = output_folder / ("iqb_" + data['title'] + '_' + c['id'] + ".ttl")
            outfile_path = os.path.join(output_folder, ("iqb_" + data['title'] + '_' + c['id'] + ".ttl"))
            serializer = OrderedTurtleSerializer(g)
            
            serializer.sorters = {
                ('.*?/[A-Za-z]+([0-9.]+)$', lambda x: float(x[0])),
                ('.', lambda x: 0.0),  # default
            }

            with open (outfile_path,'wb') as fp:
                serializer.serialize(fp)
            #g.serialize(str(outfile_path), format="turtle", base=base_url, encoding="utf-8")                   
