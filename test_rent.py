#!/usr/bin/env python

####################################################
# File name: homework2_rent.py                     #
# Author: Parth Mehta, Vidya Venkiteswaran         #
# Email: pm2877@columbia.edu, vv2269@columbia.edu  #
# Date created: 02/26/2017                         #
# Usage: python homework2_rent.py                  #
# Python Version: 3.4, 3.5, 3.6                    #
# Instructor: Prof. Andreas Mueller                #
####################################################


from homework2_rent import score_rent

def test_rent():
    """Run test to check accuracy
    """

    accuracy = score_rent()
    assert accuracy >= 0.42