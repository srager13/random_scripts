#! usr/bin/env python

import numpy
import pylab
import csv
import os
import stat
from optparse import OptionParser

use = "Usage:  %prog [-z noPlotZeros] [-p plotRangeStart] [-q plotRangeEnd] [-v verbose] [-a save_fig]\n"

parser = OptionParser(usage = use)

parser.add_option( "-z", "--noPlotZeros", action="store_true", dest="no_plot_zeros", default=False, help="Ignore errors of zero on plot." )
parser.add_option( "-l", "--logPlot", action="store_true", dest="log_plot", default=False, help="Use log-scale on y-axis." )
parser.add_option( "-p", "--plotRangeStart", action="store", dest="plot_range_start", default=-1, type="int", help="no description" )
parser.add_option( "-q", "--plotRangeEnd", action="store", dest="plot_range_end", default=-1, type="int", help="no description" )
parser.add_option( "-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print extra information" )
parser.add_option( "-a", "--save", action="store_true", dest="save_fig", default=False, help="Save figure instead of showing" )

(options, args) = parser.parse_args()

# either set plot range from command line or to default values (-20, 20)
if( options.plot_range_start != -1 ):
  min_error = options.plot_range_start;
else:
  min_error = -20;
if( options.plot_range_end != -1 ):
  max_error = options.plot_range_end;
else:
  max_error = 20;

alg_type = ['DistAlg', 'DelayedInfo'];

for alg_type_index in range(len(alg_type)):
  for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
      if( 'ir_' in dirname and dirpath == '.' ):
        for dp1, dn1, f1 in os.walk( dirname ):
          for fileindex in f1:
            if( 'QueueErrors_{}'.format(alg_type[alg_type_index]) in fileindex ):

	      stat_file = './{}/QueueErrors_{}.csv'.format( dirname, alg_type[alg_type_index] );

	      if( options.verbose ):
		print "\t\tOpening ", stat_file

	      try:
		ifile = open( stat_file )
	      except IOError:
		print "Could not open ", stat_file, "...continuing."
		exit()
	      reader = csv.reader(ifile)

	      stats = [[0 for i in range(25)] for j in range(30000)]
	      colnum = 0
	      rownum = 0
	      for row in reader:
		colnum = 0
		for col in row:
		  #print col
		  if( col != ' ' ):
		    stats[rownum][colnum] = int(col)
		  colnum += 1
		rownum +=1

	      num_nodes = colnum

              if options.no_plot_zeros:
	        array_size = max_error - min_error
              else:
	        array_size = max_error - min_error + 1

	      xVals = [0 for i in range(array_size)]
	      i = 0 
	      j = min_error
	      while i < array_size:
                if options.no_plot_zeros == False or j != 0:
		  xVals[i] = j
                  #print "xVals = ", j
		j+=1
		i+=1

	      histogram = [0 for i in range(array_size)]

	      i = 0
	      while i < rownum:
		j = 0
		while j < colnum:
		  #print 'value = ', stats[i][j]
		  #print 'value + offset = ', stats[i][j]+abs(min_error)
                  if options.no_plot_zeros:
                    if stats[i][j] == 0:
                      j += 1
                      continue
                    else:
		      if( stats[i][j] >= min_error and stats[i][j] <= max_error ):
                        if( stats[i][j] < 0 ):
		          histogram[stats[i][j]+abs(min_error)] += 1
                        else:
		          histogram[stats[i][j]+abs(min_error)-1] += 1
                      j += 1
                      continue
		  if( stats[i][j] >= min_error and stats[i][j] <= max_error ):
		    histogram[stats[i][j]+abs(min_error)] += 1
		  j += 1
		i += 1

              if options.log_plot:
	        pylab.semilogy( xVals, histogram, label="{}".format(dirname) );
              else:
	        pylab.plot( xVals, histogram, label="{}".format(dirname) );
	      #pylab.bar( xVals, histogram );

  font_size = 12
  pylab.xlabel( 'Error', fontsize=font_size )
  pylab.ylabel( 'Number of Occurrences', fontsize=font_size )
  pylab.legend( loc=1, prop={'size':18} )

  plot_name = './{}QueueErrorDist'.format( alg_type[alg_type_index] )
  if options.no_plot_zeros:
    plot_name = plot_name + '_NoZeros'
  if options.log_plot:
    plot_name = plot_name + '_Log'
  
  plot_name = plot_name + '.pdf'

  if options.save_fig:
    pylab.savefig( plot_name )
  else:
    pylab.show()
  pylab.clf();

