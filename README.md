# Le Barista Automatique

This is a quite simple wrapper to enable Slack notifications in an easy way for my projects, but you should be able to use it without any modifications.


## Usage

- Configure (see below).
- Use.
  
  ```
  import lebarista
  lebarista.notify(":tada: Job done! :tada:")
  ```


## Configuration

The only additional file you would need is a configuration file.

Create a `~/.lebarista.yaml` or `.lebarista.yaml` and it will get detected and loaded during the import of the module.

```
slack:
  channel: '#general'
  token: <Slack OAuth token for LeBaristaAutomatique>

```

# Adding package to PyPI

You don't need to know this, unless you are developing a package based on this, or any other Python Package that you would like to submit to the PyPI.

Just follow the conventions of Python packages (or use any template you want) and apply the configuration and processes described below.


## Configuration

You need a `~/.pypirc` configuration file to indicate your credentials and the repositories to use.

Currently, this is the setup that works for me (I had some issues with the repository URLs indicated in some tutorials due to the migration of the API).

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username:<username>
password:<password>

[pypitest]
repository:https://test.pypi.org/legacy/
username:<username>
password:<password>
```

The username and password pairs are the ones you create for your accounts in:

* PyPI: [http://pypi.python.org/pypi?%3Aaction=register_form](http://pypi.python.org/pypi?%3Aaction=register_form)
* PyPI Test: [http://testpypi.python.org/pypi?%3Aaction=register_form](http://testpypi.python.org/pypi?%3Aaction=register_form)

## Process

Tagging before uploading is always a good idea:

```
git tag x.y.z -m "Version description"
git push --tags origin master
```

To test:

```
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
```

To upload to PyPI Live:

```
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```