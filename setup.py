from setuptools import setup

setup(
    name='scrapy-beautifulsoup',
    version='0.0.1',
    description='Simple Scrapy middleware to process non-well-formed HTML with BeautifulSoup',
    long_description=open('README.rst').read(),
    keywords='scrapy beautifulsoup html html-parsing web-scraping',
    license='New BSD License',
    author="Alexander Afanasyev",
    author_email='afanasieffav@gmail.com',
    url='https://github.com/alecxe/scrapy-beautifulsoup',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'scrapy_beautifulsoup',
    ],
    install_requires=[
        'beautifulsoup4'
    ],
)
