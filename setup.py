"""The setup script."""

from pathlib import Path
from setuptools import setup, find_packages

# Package meta-data.
NAME = "flasc"
DESCRIPTION = "FLASC provides a rich suite of analysis tools for SCADA data filtering & analysis, wind farm model validation, field experiment design, and field experiment monitoring."
URL = "https://github.com/NREL/flasc"
EMAIL = "paul.fleming@nrel.gov"
AUTHOR = "NREL National Wind Technology Center"

# What packages are required for this module to be executed?
REQUIRED = [
    'bokeh>=3.1.1',
    'floris>=3.4',
    'feather-format',
    'ipympl>=0.9.3',
    'matplotlib>=3.6.3',
    'numpy',
    'pandas>=1.5',
    'pyproj',
    'pytest',
    'SALib',
    'scipy',
    'sqlalchemy',
    'streamlit',
    'tkcalendar',
    'seaborn',
    'polars>=0.19.0'
]

EXTRAS = {
    "docs": {
        "jupyter-book<=0.13.3",
        "sphinx-book-theme",
        "sphinx-autodoc-typehints",
        "sphinxcontrib-autoyaml",
        "sphinxcontrib.mermaid",
    },
    "develop": {
        "pytest",
        "pre-commit",
        "ruff",
        "isort",
    },
}

ROOT = Path(__file__).parent
with open(ROOT / "flasc" / "version.py") as version_file:
    VERSION = version_file.read().strip()

with open('README.md') as readme_file:
    README = readme_file.read()

setup_requirements = [
    # Placeholder
]

test_requirements = [
    # Placeholder
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['flasc*']),
    entry_points={
        'console_scripts': [
            'flasc=flasc.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='flasc',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
