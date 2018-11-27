#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

"""Simple function to convert an RDF/XML document to JSON-LD.

@author: timathom@indiana.edu
"""

import rdflib

RDF = "../../project-data/gutenberg-iul-item.rdf"

def rdfxml2jsonld(d):
    g = rdflib.ConjunctiveGraph()        
    if d:        
        g.parse(data=d, format="application/rdf+xml")        
        return g.serialize(format="json-ld")
        
rdfxml = open(RDF, "r")

print(rdfxml2jsonld(rdfxml.read()).decode("utf-8", "ignore"))

rdfxml.close()

