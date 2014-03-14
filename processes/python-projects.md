#Python Processes

This is basically a summarization of Jeff Knupp's ["Open Sourcing Python Projects the Right Way"](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/).

## Project layout

 - top level files: `README.md`, `setup.py`, `requirements.txt`, `LICENSE`, maybe `TODO.md`
 - `$project_name` directory: `__init__.py`, files, `test/`, with `test_$name.py` files
 - `docs/` directory, with .rst files



## setuptools, setup.py

 - `setuptools` is an enhancement of `distutils`
 - uses `setup.py` (see example in `frameworks/setuptools/`)


## git, GitHub

 - use git-flow (see `processes/git-flow.md`)
 - `README.md`: include 

        [ ] description, 
        [ ] link to ReadTheDocs page, 
        [ ] TravisCI button, 
        [ ] Quickstart documentation
        [ ] List of non-Python dependencies and how to install them

 - maintain issues, be quick to respond


## virtualenv, virtualenvwrapper

 - `mkvirtualenv $project` for initialization
 - `deactivate` to leave, `workon <name>` to resume
 - once code is working, generate `requirements.txt` by running `pip freeze > requirements.txt`, maybe change every `==` to `>=`
 - add packages from `requirements.txt` to `distutils.setup` in `setup.py`


## py.test

 - extends `unittest`
 - test files need to be `test_`-prefixed
 - coverage: `pip install pytest-cov`, `py.test --cov=path/to/package --cov-report=term --cov-report=html`
 - …


## tox (test standardizing)

 - make sure everything runs under different Python versions
 - `tox.ini`: put in same directory as `setup.py`

         [tox]
         envlist = py26,py27
         [testenv]
         deps=pytest       # install pytest in the venvs
         commands=py.test  # or 'nosetests' or ...

 - just run `tox`
    

## Sphinx (documentation)

 - comments in rst: """ Description \n:param name: alkjfd\n:type name: :class:`project.module.Module`\n:rtype bool, for more see `frameworks/sphinx.md`
 - install Sphinx in the virtualenv!, aswell as sphinx-apidoc 
 - generate: `sphinx-apidoc -F -o docs <package name>`
 - package needs to be locally installed: `python setup.py develop`

        import pkg_resources
        try:
            release = pkg_resources.get_distribution('sandman').version
        except pkg_resources.DistributionNotFound:
            print 'To build the documentation, The distribution information of sandman'
            print 'Has to be available.  Either install the package into your'
            print 'development environment or run "setup.py develop" to setup the'
            print 'metadata.  A virtualenv is recommended!'
            sys.exit(1)
        del pkg_resources
        
        version = '.'.join(release.split('.')[:2])

 - maybe change `html_theme` from `default` to `nature` or something


## Deploying to PyPI

 - install `cheesecake`, let it score the project. Best run before each upload.
 - first upload: `python setup.py register`
 - then: `python setup.py sdist upload`
 - versions: see `languages/python/pep440_versioning.md`
 - workflow:

        [ ] edit stuff
        [ ] make sure everything runs and is fine
        [ ] freeze by doing a release-branch-merge (git-flow)
        [ ] update __version__ in __init__.py
        [ ] run `python setup.py sdist upload`


## TravisCl (continuous integration)

 - each time when pushing: check if things broke, activate on travis-ci.org
 - generate a .travis.yml

        language: python
        python:
            - "2.7"
        install: 
            - "pip install -r requirements.txt --use-mirrors"
        script:
            - "python setup.py test"
    

## ReadTheDocs (continuous documentation integration)
 - log in, configure


## Cookiecutter (automation of the above)
