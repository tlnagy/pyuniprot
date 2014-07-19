pyuniprot
=======

A simple and easy-to-use Python frontend for [UniProt](http://www.uniprot.org)'s REST API. It outputs a CSV file populated with the requested columns and information from Uniprot. 

## Features

- Accepts either JSON piped via command-line or a configuration file for requests
- Automatic conversion from Uniprot's tab format to the more widely used csv format

## Installation

Either clone it to your computer or download it as a zip file. To run it you will need a Python interpreter installed (I highly recommend the free [Anaconda](https://store.continuum.io/cshop/anaconda/) package manager for this) and the following command: 
```bash
python pyuniprot.py
```
The other option is to run `chmod +x pyuniprot.py` so you can then use it like so:
```bash
./pyuniprot.py
```

## Usage

A request can either be given via stdin as a JSON file or via the `conf.py` file. Requests should be formatted in the following manner:
```
request = {
    'columns':'id,entry name,reviewed,protein names,sequence',
    'query':'sonic hedgehog AND organism:human',
    'output':'output'
}
```
where `columns` is a comma-separated list of the columns of information that you would like Uniprot, `query` is the Uniprot query, i.e. what you would type into the search bar on <http://www.uniprot.org>, and `output` is the name of the output file. The release date of Uniprot version accessed will be appended to this name, e.g. output_2014_07.csv.

The following are some examples of the possible columns:

- clusters
- database (usage: database(PDB) )
- domains
- id
- existence
- families
- features
- genes
- go-id
- keywords
- last-modified
- length
- protein names
- sequence
- taxon
- virus hosts

Please see <http://www.uniprot.org/faq/28> for the complete list of available columns and detailed information on building queries. 

## License 

BSD