#!/usr/bin/env python

# Copyright (c) 2014 Tamas Nagy <tamas@tamasnagy.com>. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

"""
pyuniprot is a Python wrapper around Uniprot/Swiss-Prot's REST API.

It outputs a CSV file with the requested columns of information. It uses pure 
Python with no external packages needed.

Examples
--------

>>> ./pyuniprot.py

This will run pyuniprot and it will default to using the `conf.py` file in
the local directory

>>> echo '{"columns": "id,entry name,reviewed,protein names,sequence", 
"output": "output", "query": "sonic hedgehog AND organism:human"}' |
./pyuniprot.py

pyuniprot will use the json file provided to query Uniprot. This allows it
to be used in a larger toolchain.

"""

import sys
import os
PY3K = True
if sys.hexversion < 0x03000000:
    PY3K = False
if PY3K:
    import urllib.request as request
    import urllib.parse as parse
else:
    import urllib as parse
    import urllib2 as request
import csv
import argparse
import json
    
baseurl = 'http://www.uniprot.org/'

def _retrieveFromUniProt(params, service='uniprot/'):
    """
    Retrieves sequences from UniProt according to the parameters supplied. The 
    parameters should be in a dictionary of strings mapped to strings. Service
    is the sub-url of the Uniprot database, e.g. "uniprot/" or "mapping/". See 
    conf.py and http://www.uniprot.org/faq/28 for building queries. Returns a 
    tuple of the raw data and the header.
    """
    data = parse.urlencode(params).encode('utf-8')
    url_request = request.Request(baseurl + service, data)
    url_request.add_header('User-Agent', 'Python')
    
    print("Making request...")    
    response = request.urlopen(url_request)
    print("Request complete.")
    return response.read().decode('utf-8'), response.info()

def _usage():
    print(__doc__)

def main():
    print("pyuniprot v0.01")
    try:
        params, output = {}, 'output'
        try:
            if not os.isatty(0):
                print("Stdin input detected. Attempting to load")
                params = json.loads(sys.stdin.read())
            else:
                print("Attempting load from config file")
                try:
                    import conf
                except ImportError:
                    print("Missing config file")
                params = conf.params
            if any([param not in params.keys() for param in ['columns','query', 
                                                     'output']]):
                raise KeyError('Required parameter missing from input.')
            output = params['output']
        except KeyError as err:
            _usage()
            raise err
            sys.exit(1)
        print("Loaded.")
        params.update({'format':'tab'})
        tab_results = _retrieveFromUniProt(params)
    
        cleaned_tab_result = [x.split('\t') for x in tab_results[0].split('\n') ]
        
        if 'colnames' in params:
            colnames = params['colnames'].split(',')
            if len(colnames) is not len(cleaned_tab_result[0]):
                raise Exception('Too many or too few provided new column names')
            cleaned_tab_result[0] = colnames
        file_name = '../%s_%s.csv'%(output, tab_results[1]['X-UniProt-Release'])
        print("Writing to %s"%file_name)        
        with open(file_name,'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(cleaned_tab_result)
        print("Complete!")
            
    except KeyboardInterrupt:
        print("\nAborting...")
        
if  __name__ =='__main__':main()
