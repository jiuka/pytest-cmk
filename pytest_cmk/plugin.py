import pytest

import cmk_base.config as config
import cmk_base.check_api as check_api

from pytest_cmk.data_sources.snmp import MockSNMPDataSource
from pytest_cmk.data_sources.agent import MockAgentDataSource

@pytest.hookimpl()
def pytest_sessionstart(session):
    config_cache = config.get_config_cache()
    config_cache.initialize()
    print "cmk initialized"


@pytest.fixture
def check_name(request):
    return getattr(request.module, 'CHECK', request.module.__name__.rsplit('.',1)[-1][5:])

@pytest.fixture
def check_info(request, check_name):
    if not config._all_checks_loaded:
        print "Load all checks"
        config._initialize_data_structures()
        filelist = config.get_plugin_paths('/src/tests/fixtures/checks')
        config.load_checks(check_api.get_check_api_context, filelist)
        config._all_checks_loaded = True

    return config.check_info[check_name]

@pytest.fixture
def parse_function(check_info):
    return check_info['parse_function']

@pytest.fixture
def inventory_function(check_info):
    return check_info['inventory_function']

@pytest.fixture
def check_function(check_info):
    return check_info['check_function']

@pytest.fixture
def has_perfdata(check_info):
    return check_info['has_perfdata']


@pytest.fixture
def snmpwalk_attr(request):
    import textwrap
    if request.cls:
        if hasattr(request.cls, 'SNMPWALK'):
            return textwrap.dedent(getattr(request.cls, 'SNMPWALK'))
    if hasattr(request.module, 'SNMPWALK'):
        return textwrap.dedent(getattr(request.module, 'SNMPWALK'))

@pytest.fixture
def snmp_datasource(check_name, snmpwalk_attr):
    return MockSNMPDataSource(check_name, snmpwalk_attr.splitlines())

@pytest.fixture
def agentout_attr(request):
    import textwrap
    if request.cls:
        if hasattr(request.cls, 'AGENTOUTPUT'):
            return textwrap.dedent(getattr(request.cls, 'AGENTOUTPUT'))
    if hasattr(request.module, 'AGENTOUTPUT'):
        return textwrap.dedent(getattr(request.module, 'AGENTOUTPUT'))

@pytest.fixture
def agent_datasource(check_name, agentout_attr):
    return MockAgentDataSource(check_name, agentout_attr)
