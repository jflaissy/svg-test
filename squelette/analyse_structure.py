#!/usr/bin/python
# -*- coding: utf-8 -*-

import structure_example

ind = '  '

def print_tests(s):
    for test in s:
        print 'Test'
        print ind, 'type', test['type']
        print ind, 'execs'
        for ex in test['execs']:
            print ind*2, 'exec'
            print ind*2, 'browser', ex['browser']
            print ind*2, 'preprocessing'
            for pre in ex['preprocessing']['filters']:
                print ind*3, 'name', pre['name']
                print ind*3, 'parameters', pre['parameters']
            print ind*2, 'capture'
            cap = ex['capture']
            print ind*3, 'name', cap['name']
            print ind*3, 'interactions', cap['interactions']
            print ind*3, 'parameters', cap['parameters']
            print ind*2, 'postprocessing'
            for post in ex['postprocessing']['filters']:
                print ind*3, 'name', post['name']
                print ind*3, 'parameters', post['parameters']
        print ind, 'diagnostic'
        diag = test['diagnostic']
        print ind*2, 'name', diag['name']
        print ind*2, 'parameters', diag['parameters']
        print ind*2, 'reference', diag['reference']
        print '---'

s = structure_example.tests
print_tests(s)

