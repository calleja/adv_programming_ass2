#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:47:44 2018

@author: lechuza
"""

import pymongo
import pandas as pd
import numpy as np

#exposed port on the docker mongo container: 27017
#sudo docker run -it -p 81:27017 mongo