from setuptools import setup, find_packages

setup(
    name='simple-sanic',
    version='0.1',
    description='A faster http.server using sanic',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sanic http.server',
    url='https://github.com/remusao/simple-sanic',
    author='remusao',
    license='MIT',
    py_modules=["simple-sanic"],
    install_requires=[
        'docopt',
        'sanic'
    ],
    include_package_data=True,
    zip_safe=False,
)
