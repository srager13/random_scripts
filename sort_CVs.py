#! usr/bin/env python

import os
import stat
from pyPdf import PdfFileReader
import shutil
#from pyPdf import PageObject

departments = ['Aerospace', 'Architectural', 'Bio', 'Chem', 'Civil', 'Computer', 'Environment', 'Electrical', 'Engineering Science', 'Industrial', 'Mechanical', 'Nuclear']


for i in range(len(departments)):
  dep_dir = './CV/%(dep)s' % {"dep":departments[i]}
  print "dep_dir = ", dep_dir
  print "departments[", i, "] = ", departments[i]
  if not os.path.exists( dep_dir ):
    print "trying to make ", dep_dir
    os.makedirs( dep_dir );

  for dirname, dirnames, filenames in os.walk('./CV/All_Resumes/'):
    for filename in filenames:
      #print filename
      if( "pdf" in filename ): 
        #print filename
        #  if it is a pdf, open it
        reader = PdfFileReader( file( './CV/All_Resumes/%s'%filename, 'r' ) )
        #print "number of pages = ", reader.getNumPages()
        # go through all pages of the pdf
        for j in range(reader.getNumPages()):
          page = reader.getPage(j)
          #print "reading page ", j, " of ", filename
          if( departments[i] in page.extractText() ):
            #print "found ", departments[i], "in ", filename
            # check if resume is in proper folder...if not, copy it there
            if not os.path.exists( './CV/%(dep)s/%(resume)s'%{"dep":departments[i], "resume":filename} ):
              shutil.copy2( './CV/All_Resumes/%s'%filename, './CV/%(dep)s/%(resume)s'%{"dep":departments[i], "resume":filename} )

