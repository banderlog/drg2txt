import setuptools


setuptools.setup(
    name='drg2text',
    version='0.1.0',
    url="",
    maintainer="Kabakov Borys",
    license='MIT',
    description="Map MS-DRG v38.1 DRG/MDC numeric codes to their text description",
    packages=['drg2text'],
    package_data={'drg2text': ['*.csv']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering',
    ],
)
