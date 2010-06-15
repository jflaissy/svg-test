# -*- coding: utf-8 -*-
"""Un module de diagnostic qui dit toujours oui."""

def go(comparison, output_prefix, parameters):
    print 'Diagnostic Always_yes. '
    comparison['result'] = { 'valid' : True, 'message' : '' }
    return None
