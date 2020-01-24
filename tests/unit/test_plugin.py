CHECK = 'snmptest'

def test_check_name(check_name):
    assert check_name == CHECK

def test_check_info(check_info):
    assert check_info

def test_parse_function(parse_function):
    assert parse_function

def test_inventory_function(inventory_function):
    assert inventory_function

def test_check_function(check_function):
    assert check_function

def test_has_perfdata(has_perfdata):
    assert has_perfdata is not None
