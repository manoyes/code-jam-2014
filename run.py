#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: python run.py < A-small-practice.in > result.txt
if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
