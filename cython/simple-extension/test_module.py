from cyt_module import subtract

"""
As the C-extension implements the fully dynamic Python code (just using the Python C-API), transforming the pure Python 
module into C-extension gives normally only very modest speed-ups. However, as we will discuss in the following steps, 
by adding Cython language extensions into the code (.pyx?, so it is no longer valid Python code) it is possible to achieve much 
more significant performance improvements.

Uses the cyt_module.cp37-win_amd64.pyd C-extension.
"""

z = subtract(5, 2)
print(z)
