pyuniprot
=======

A simple and easy-to-use Python frontend for UniProt's REST API. It outputs a CSV file populated with the requested columns and information from Uniprot. 

## Installation

Either clone it to your computer or download it as a zip file. To run it you will need Python 3+ installed and the following command: 
```
python pyuniprot.py
```
I'm assuming that you have the python command mapped to the Python 3 interpreter. If you don't then use `python3` inplace of `python`. The other option is to run `chmod +x pyuniprot.py` so you can then use it like so:
```
./pyuniprot
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

## To-do

- Make the code more flexible so that it can support all the Uniprot output formats. 
- ~~Make it accept command-line argument for piping~~
- Add support for Uniprot's useful ID mapping service
