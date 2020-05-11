from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

# run file in terminal: python setup.py build_ext --inplace
# add: include_dirs=[numpy.get_include()]
# to avoid error: fatal error: numpy/arrayobject.h: No such file or directory...compilation terminated

setup(
     ext_modules=cythonize("heat_cy.pyx", annotate=True, language_level=3),
     include_dirs=[numpy.get_include()]
)
