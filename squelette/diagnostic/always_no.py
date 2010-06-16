# -*- coding: utf-8 -*-
"""Un module de diagnostic qui dit toujours oui."""

def go(comparison, output_prefix, diagnostic):
    print 'Diagnostic Always_no. '
    comparison['result'] = { 'valid' : False, 'message' : '' }
    return None
