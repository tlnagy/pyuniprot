# -*- encoding: utf-8 -*-
# This is the configuration file for PyUniprot3
# 
# Please write proper python!




# Name of output file
output = 'output'

# Parameters for Uniprot Query. See http://www.uniprot.org/faq/28 for building 
# queries. Note specifying the format will not work because the current 
# version of PyUniprot3 simply overwrites this attribute. I'm considering
# changing this in the future.
params = {
    'columns':'id,entry name,reviewed,protein names,sequence',
    'query':'sonic hedgehog AND organism:human'
    }