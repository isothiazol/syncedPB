# syncedPB
Synced progress bar for Python and Jupyter notebooks.


## Examples

Progress bar on a loop:

```python
for i in syncedPB(range(100)):
    time.sleep(0.1)
```

If you are working on a Jupyter notebook, and you want a cool popup display when your loop is done:

```python
for i in syncedPB(range(100), popup=True):
    time.sleep(0.1)
```

## How to get it

The latest wheel file can be found in the [https://github.com/javirrs/syncedPB/releases](release section) of the repo, or [https://github.com/javirrs/syncedPB/releases/download/v0.0.1/syncedPB-0.0.1-py3-none-any.whl](here)

Once downloaded you can install it by:

```
pip install *.whl
```

## Last words

Please report any bug (or any cool idea to implement) by opening an [https://github.com/javirrs/syncedPB/issues](issue). [https://github.com/javirrs/syncedPB/pulls](Pull requestai) and collaborators are welcome.
