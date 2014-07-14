pyuniprot
=======

A simple Python frontend for UniProt's REST API. Either clone it to your computer or download it as a zip file. To run it you will need Python 3+ installed and the following command: 
```
python pyuniprot.py
```
I'm assuming that you have the python command mapped to the Python 3 interpreter. If you don't then use `python3` inplace of `python`. The other option is to run `chmod +x pyuniprot.py` so you can then use it like so:
```
./pyuniprot
```
Configure your request by modifying the `conf.py` file or by passing a JSON file containing the necessary information. See <http://www.uniprot.org/faq/28> for more examples and detailed information on building queries. 

## To-do

- Make the code more flexible so that it can support all the Uniprot output formats. 
- ~~Make it accept command-line argument for piping~~
- Add support for Uniprot's useful ID mapping service
