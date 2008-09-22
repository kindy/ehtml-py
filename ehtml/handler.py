#!/usr/bin/python
#coding: utf-8

import sys, os
from time import time as time_time

from genshi.template import TemplateLoader
from helper import TplHelper, DomHelper

env = os.environ
DOCUMENT_ROOT = env['DOCUMENT_ROOT']
TPL_FILENAME = env['PATH_INFO'].lstrip('/')
QUERY_STRING = env['QUERY_STRING']


tplLoader = TemplateLoader(
    DOCUMENT_ROOT,
    auto_reload=False
)

def main ():
    time_1 = time_time()
    
    output = "Content-Type: text/html\n"
    
    ctxt = {"env": env,
            "location": {"href": "", "search": QUERY_STRING and ('?' + QUERY_STRING) or ''},
            "dom": TplHelper(),
            "tpl": DomHelper()
        }
    
    try:
        rslt = tplLoader.load(TPL_FILENAME, relative_to=DOCUMENT_ROOT).generate(**ctxt).render('xhtml', doctype='xhtml-transitional')
        
        output += "TmplRender-Time: %f s\n\n" % (time_time() - time_1)
        output += rslt
        
        del time_1
        del rslt
    except:
        output = "Content-Type: text/plain\n\n"
        output += str(sys.exc_info()[1]).replace(DOCUMENT_ROOT, '$DOCUMENT_ROOT$')
    
    print output
    del output


if __name__ == "__main__":
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
    main()
