test = {   'name': 'q1_2_2',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> # Make sure a string is assigned to `most_stem`;\n>>> assert type(most_stem) == str\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Make sure the string assigned to `most_stem` is actually in the Stem column;\n>>> assert most_stem in vocab_table.column('Stem')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}