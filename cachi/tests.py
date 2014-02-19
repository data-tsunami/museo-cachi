# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import base64

#from django.test import TestCase


# Create your tests here.
TEST_IMAGE = "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"  #@IgnorePep8


def get_test_image():
    return base64.b64decode(TEST_IMAGE)