import rdflib

from rdflib import Graph

from rdflib.namespace import Namespace, NamespaceManager

EX = Namespace('http://example.com/')

namespace_manager = NamespaceManager(Graph())

namespace_manager.bind('ex', EX, override=False)

g = Graph()

g.namespace_manager = namespace_manager

all_ns = [n for n in g.namespace_manager.namespaces()]

assert ('ex', rdflib.term.URIRef('http://example.com/')) in all_ns