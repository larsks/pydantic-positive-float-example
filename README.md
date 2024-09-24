This repository is part of <https://stackoverflow.com/a/78999259/147356>.

My preferred way of doing things using [pipenv](https://pipenv.pypa.io/en/latest/):

```
pipenv install -r requirements.txt
pipenv run pytest
```

Or using containers to test against different versions of Python:

```
for python_version in 3.10 3.11 3.12 3.13.0rc2; do
  podman run --rm -v "$PWD:/src:z" -w /src python:"${python_version}" \
    bash -c 'pip install --root-user-action=ignore -r requirements.txt && pytest' || { echo "FAILED!"; break; }
done
```
