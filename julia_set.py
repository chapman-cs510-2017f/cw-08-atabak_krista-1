#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###
# Name:  Atabak
# Email:  pouya[at]chapman[dot]edu
# Course: CS510 Fall 2017
# Assignment: Homework 6
###
"""
from cplane_np import ArrayComplexPlane
import csv
import numpy as np
import matplotlib.pyplot as plt
import numba as nb


def julia(c, max=100):
    @nb.vectorize([nb.int32(nb.complex128)])
    def f(z):
        if abs( z ) <= 2:
            n = 0
            while abs(z)<=2:
                z = z**2 + c
                if n >= max:
                    n = 1
                    break
                n+=1
            n -= 1
        else:
            n = 1
        return n

    return f



class JuliaPlane(ArrayComplexPlane):
    def __init__(self, xmin,xmax,xlen,ymin,ymax,ylen,c):
        self.c = c
        super().__init__(xmin,xmax,xlen,ymin,ymax,ylen)
        super().apply(julia(self.c))


    def refresh(self, c):
        super().refresh()
        julia(self.plane)

    def toCSV(self, filename):
        writer = csv.writer(open(filename+".csv", 'w'))
        writer.writerow(self.plane)

    def fromCVS(self, filename):
        pass

    def show(self):
        plt.imshow(self.plane, interpolation='bicubic', cmap='hot',origin='lower', extent=[-2,2,-2,2],)
       