from distutils.core import setup, Extension
from Cython.Build import cythonize

# run file in terminal: python setup.py build_ext --inplace
setup(
     ext_modules=cythonize("fib_cyt.pyx", annotate=True, language_level=3)
)
