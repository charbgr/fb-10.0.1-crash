
import sys
with open(sys.argv[1]+".java", 'w') as f:
    f.write('package com.aaronstacy.fbcrash;\n')
    f.write('public class ' + sys.argv[1] + '{\n')
    for i in range(10001):
        f.write('public void foo'+str(i)+'() {}\n')
    f.write('}')
f.close()
