#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###
# Name: Kristaaaa, Atabak
# Student ID: KristaIDHere, AtabakIDHere
# Email:  kristaEmailHere , AtabakEmail
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###
"""
import numpy as np
import pandas as pd
from abscplane import AbsComplexPlane


class ArrayComplexPlane(AbsComplexPlane):
    """This Class creates a plane based on complex numbers.

       Attributes:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        fs (list[function]) : function sequence to transform plane
    """
    def __create_plane(self, xmin, xmax, xlen, ymin, ymax, ylen):
        dx = np.linspace(xmin,xmax,xlen)
        dy = np.linspace(ymin,ymax,ylen)
        x , y = np.meshgrid(dx,dy)
        #plane_n = pd.DataFrame(x + y*1j)
        plane_n = x + y*1j
        return plane_n

    def __init__(self):
        self.xmin = 0.0
        self.xmax = 100.0
        self.xlen = 100
        self.ymin = 0.0
        self.ymax = 100.0
        self.ylen = 100
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen,
                                         self.ymin, self.ymax, self.ylen)
        fs = []

    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.fs = []
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen,
                                         self.ymin, self.ymax, self.ylen)

    def refresh(self):
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen,
                                         self.ymin, self.ymax, self.ylen)
        self.fs = []

    def apply(self, f):
        fv=np.vectorize(f)
        self.plane=fv(self.plane)
        self.fs.append(f)

    def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen,
                                         self.ymin, self.ymax, self.ylen)
        for f in self.fs:
            self.apply(f)

