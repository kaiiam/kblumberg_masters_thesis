#!/usr/bin/python

import statistics

#in degree

in_degree = []
in_degree.extend([0]*154)
in_degree.extend([1]*55)
in_degree.extend([2]*23)
in_degree.extend([3]*12)
in_degree.extend([4]*6)
in_degree.extend([5]*1)
in_degree.extend([6]*3)
in_degree.extend([7]*2)
in_degree.extend([10]*2)
in_degree.extend([15]*1)
in_degree.extend([19]*1)
in_degree.extend([24]*2)
in_degree.extend([25]*1)
in_degree.extend([33]*1)
in_degree.extend([44]*1)

print "in degree median:", statistics.median(in_degree)
print "in degree mean:", statistics.mean(in_degree)



#out degree

out_degree = []
out_degree.extend([0]*42)
out_degree.extend([1]*108)
out_degree.extend([2]*64)
out_degree.extend([3]*41)
out_degree.extend([4]*7)
out_degree.extend([5]*3)

print "out degree median:", statistics.median(out_degree)
print "out degree mean:", statistics.mean(out_degree)


#shortest path length

spl = []
spl.extend([1]*338)
spl.extend([2]*336)
spl.extend([3]*246)
spl.extend([4]*88)
spl.extend([5]*47)
spl.extend([6]*8)
spl.extend([7]*1)

print "shortest path length median:", statistics.median(spl)
print "shortest path length mean:", statistics.mean(spl)



#make the file name to write to
outstring = 'in_degree_distribution.csv'
#create output csv file
f = open(outstring, 'w')
#write headers
f.write('values\n')
#write results
for x in in_degree:
   f.write( str(x) + '\n' )




#make the file name to write to
outstring = 'out_degree_distribution.csv'
#create output csv file
f = open(outstring, 'w')
#write headers
f.write('values\n')
#write results
for x in out_degree:
   f.write( str(x) + '\n' )




#make the file name to write to
outstring = 'shortest_path_length_distribution.csv'
#create output csv file
f = open(outstring, 'w')
#write headers
f.write('values\n')
#write results
for x in spl:
   f.write( str(x) + '\n' )
