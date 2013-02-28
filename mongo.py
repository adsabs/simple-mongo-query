'''
Created on Feb 28, 2013

@author: jluker
'''

import sys
import pymongo
import simplejson
from optparse import OptionParser

WANTED_FIELDS = ['title', 'abstract', 'keyword', 'full', 'aff']

if __name__ == '__main__':
    
    op = OptionParser()
    op.add_option('-m','--mongohost', dest="host", action="store", type=str, 
            help="mongo instance host", default="127.0.0.1")
    op.add_option('-p','--mongoport', dest="port", action="store", type=int, 
            help="mongo instance port", default=27017)
    op.add_option('-v','--verbose', dest="verbose", action="store_true",
            help="print stuff")
    opts, args = op.parse_args() 
        
    m = pymongo.MongoClient(opts.host, opts.port)
    db = m['solr4ads']
    
    def biblist():
        bibs = len(args) and open(args) or sys.stdin
        for bib in bibs:
            yield bib.strip()
        
    wanted = dict([(x, 1) for x in WANTED_FIELDS])
    wanted['_id'] = 0
    
    for bib in biblist():
        if opts.verbose:
            print "Looking up %s" % bib
        doc = db.docs.find_one({'bibcode': bib}, wanted)
        if doc:
            if opts.verbose:
                print "Dumping %s" % bib
            outfile = open('./%s.json' % bib, 'w')
            simplejson.dump(doc, outfile, indent=True)
            
    if opts.verbose:
        print "Done."
        
        
        
        
    