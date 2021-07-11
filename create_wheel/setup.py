import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='drg2txt',
    version='0.3.0',
    url="https://github.com/banderlog/drg2txt",
    maintainer="Kabakov Borys",
    license='MIT',
    description="Map MS-DRG v38.1 DRG/MDC numeric codes to their text description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['drg2txt'],
    package_data={'drg2txt': ['*.pickle']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering',
    ],
)
