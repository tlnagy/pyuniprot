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

import sys
if sys.hexversion < 0x03000000:
    raise Exception("Please use Python 3.0+")
import urllib.request, urllib.parse, csv
try:
    import conf
except ImportError:
    print("Missing config file")

def retrieveFromUniProt(params):
    """
    Retrieves sequences from UniProt according to the parameters supplied. The 
    parameters should be in a dictionary of strings mapped to strings. See 
    conf.py and http://www.uniprot.org/faq/28 for building queries. Returns a 
    tuple of the raw data and the header.
    """
    url = 'http://www.uniprot.org/uniprot/'
    data = urllib.parse.urlencode(params).encode('utf-8')
    request = urllib.request.Request(url, data)
    request.add_header('User-Agent', 'Python')
    
    print("Making request...")    
    response = urllib.request.urlopen(request)
    print("Request complete.")
    return response.read().decode('utf-8'), response.info()

def main():
    """
    PyUniprot3 is no nonsense frontend for Uniprot/Swiss-Prot. It outputs a
    CSV file with the requested columns of information. It uses pure Python 3
    with no external packages needed.
    """
    print("PyUniprot3 v0.01")
    try:
        params, output = ({}, 'output')
        try:
            print("Loading configuration")
            params = conf.params
            output = conf.output
        except:
            raise Exception("Error loading config file. Make sure conf.py " +\
            "is setup correctly and in the local directory.")
            sys.exit(1)
        print("Loaded.")
        params.update({'format':'tab'})
        tab_results = retrieveFromUniProt(params)
    
        cleaned_tab_result = [x.split('\t') for x in tab_results[0].split('\n') ]

        file_name = '%s_%s.csv'%(output, tab_results[1]['X-UniProt-Release'])
        print("Writing to %s"%file_name)        
        with open(file_name,'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(cleaned_tab_result)
        print("Complete!")
            
    except KeyboardInterrupt:
        print("\nAborting...")
        
if  __name__ =='__main__':main()