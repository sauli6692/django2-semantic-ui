import setuptools

setuptools.setup(
    name="django2_semantic_ui",
    version="1.2.2",
    author="Franklin Sarmiento",
    author_email="franklinitiel@gmail.com",
    description="Library to easy install, configure and use Semantic UI framework with Django project (Python 3.x)",
    long_description="Removing Long description",
    long_description_content_type="text/markdown",
    url="https://github.com/franklintiel/django2-semantic-ui/wiki",
    license="MIT",
    classifiers=[
        #"Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
    keywords="semantic-ui semanticui semantic ui django-semantic-ui django-semanticui django-semantic-ui",
    project_urls={
        'Documentation': "https://github.com/franklintiel/django2-semantic-ui",
        'Source': "https://github.com/franklintiel/django2-semantic-ui",
        'Tracker': "https://github.com/franklintiel/django2-semantic-ui/issues"
    },
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires=">=3.*")
