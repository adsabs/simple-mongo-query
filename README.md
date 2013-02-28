simple-mongo-query
==================

=== mongo.py ===

For usage execute `./mongo.py -h`

This script accepts as input a list of ADS [bibcodes](http://doc.adsabs.harvard.edu/abs_doc/help_pages/data.html#Bibliographic_Identifiers), either as a file (1st argument) or via stdin. Bibcodes are looked up in our ADS `docs` collection and fields listed in `WANTED_FIELDS` are dumped to a file, serialized as json.
