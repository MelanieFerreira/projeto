# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:29:09 2018

@author: Mélanie Ferreira
"""

import csv
import xml.etree.ElementTree as ET

ET.register_namespace('', "http://www.sbml.org/sbml/level2/version4")
ET.register_namespace('dc', "http://purl.org/dc/elements/1.1/")
ET.register_namespace('html', "http://www.w3.org/1999/xhtml")
ET.register_namespace('vCard', "http://www.w3.org/2001/vcard-rdf/3.0#")
ET.register_namespace('dcterms', "http://purl.org/dc/terms/")
ET.register_namespace('bqmodel', "http://biomodels.net/biology-qualifiers/")
ET.register_namespace('drugbank', "http://www.drugbank.ca/")
ET.register_namespace('rdf', "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ET.register_namespace('bqbiol', "http://biomodels.net/biology-qualifiers/")

tree = ET.parse('Human_cancer.xml')
root = tree.getroot()


stoichiometry_csv = open("AA__Breast_human_cancer.csv", 'r')
reader = list(csv.reader(stoichiometry_csv, delimiter=';'))
stoic_dict = {}
for line in reader[1:]:
    stoic_dict[line[0]] = line[1] 

for reaction in root[0][3]:
    if reaction.attrib['id'] == 'R_BIOMASS':
        for reactant in reaction[1]:
#            if reactant.attrib['species'] == 'M_asp_L_c':
#                reactant.attrib['stoichiometry'] = "0.345"
#                print(reactant.attrib['stoichiometry'])
            
            if reactant.attrib['species'] in stoic_dict:
                reactant.attrib['stoichiometry'] = stoic_dict[reactant.attrib['species']]
                print(reactant.attrib['stoichiometry'])
                

tree.write('Breast_human_cancer.xml')