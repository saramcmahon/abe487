#!/usr/bin/env python3

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Parse BLAST tab')
    parser.add_argument('positional', metavar='file', help='BLAST tab output')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type=float, default=0)
    parser.add_argument('-e', '--evalue', help='',
                        metavar='float', type=float, default=None)
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
#   tab_arg = args.tab
    pi_arg = args.pct_id
    e_arg = args.evalue
    pos_arg = args.positional
    flds = 'qseqid sseqid pident some other stuff that we dont need evalue'.split()
 
    for line in open(pos_arg): 
      row = dict(zip(flds, line.split('\t')))
      number = float(row['pident'])
      number2 = float(row['evalue'])
      if number >= pi_arg and e_arg == None :
           print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])
      if not e_arg == None and pi_arg == 0:
           if number2 <= e_arg :
                print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])
      if not pi_arg == 0 and not e_arg == None:
           if number2 <= e_arg and number >= pi_arg:
                print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])

#   print('positional = "{}"'.format(pos_arg))
#    for line in open(pos_arg):
#        if line[0] == '#': 
#            continue
#    row = dict(zip(flds, line.split('\t')))
#    attrs = {}
#    
#    print(row)   
#  
#  if 'attribute' in row:
#        for fld in row['attribute'].split(';'):
#           if '=' in fld:
#               name, val = fld.split('=')
#               attrs[name] = val      
# --------------------------------------------------
if __name__ == '__main__':
    main()
