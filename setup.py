import os

from setuptools import find_packages, setup


setup(
    name='django-pygmentify',
    version='0.3.5',
    description='A Django template tag to highlight code with Pygments',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Richard Cornish',
    author_email='rich@richardcornish.com',
    url='https://github.com/richardcornish/django-pygmentify',
    license='BSD License',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'pygments',
        'beautifulsoup4',
    ],
    test_suite='pygmentify.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
