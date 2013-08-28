#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

common_setup = """\
import numpy
"""
setup = common_setup

vb_random = []
# Simple generators
for f in (('normal', ''), ('uniform', ''), ('weibull', "1, "),
          ('binomial', "10,0.5, "), ('poisson', "10,")):
    cmd = 'numpy.random.%s(%ssize=(100,100))' % f
    vb_random.append(Benchmark(cmd, setup, name=cmd))

# shuffle
vb_random_shuffle100000 = Benchmark("numpy.random.shuffle(a)", setup + "a=numpy.arange(100000)")

#print [x.name for x in vb_random], vb_random_shuffle100000.name
