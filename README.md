# pytest-cmk

This [pytest](https://pytest.org/) plugin for [Checkmk](https://checkmk.com) allows for Checkmk checks to be unit tested.
It runs within a Docker container based on [checkmk:check-mk-raw](https://hub.docker.com/r/checkmk/check-mk-raw) with
pytest and this plugin added. This allows the plugin to use the cmk and cmk_base python module to provide the checks with
there environment to work in.

## Run the tests

```bash
docker run --rm -ti -v <PATH TO THE REPO>:/src pytest-cmk
```

## Writing Unit Tests

pytest-cmk provides a number of fixtures to use within the test.

Fixture Name       | Fixture Description
-------------------|--------------------
check_name         | The name of the check under test
check_info         | The check_info of the check under test
parse_function     | The parse function of the check under test
inventory_function | The inventory function of the check under test
check_function     | The check function of the check under test
factory_settings   | The factory_settings of the check under test

The name of the check is taken from the filename of the test. `test_foo.py` tests the check named `foo`.

```python
def test_parse_function(parse_function):
    parsed = parse_function([['Name','Key1','Key2'],['Alice','Value1','Value']])
  
    assert parsed == {'Alice': {'Key1': 'Value1', 'Key2': 'Value2'}}
  
def test_inventory_function(inventory_function):
    items = list(inventory_function({'Alice': {'Key1': 'Value1', 'Key2': 'Value2'}})
    
    assert items == [('Alice': {})]
```
