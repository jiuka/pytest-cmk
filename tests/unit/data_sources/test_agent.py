from pytest_cmk.data_sources.agent import MockAgentDataSource

CHECK='df'

AGENTOUTPUT = '''
<<<check_mk>>>
Version: 1.6.0p5
AgentOS: linux
Hostname: vm-operator
AgentDirectory: /etc/check_mk
DataDirectory: /var/lib/check_mk_agent
SpoolDirectory: /var/lib/check_mk_agent/spool
PluginsDirectory: /usr/lib/check_mk_agent/plugins
LocalDirectory: /usr/lib/check_mk_agent/local

<<<df>>>
tmpfs                tmpfs      817660    1100    816560       1% /run
none                 tmpfs           4       0         4       0% /sys/fs/cgroup
none                 tmpfs        5120       0      5120       0% /run/lock
none                 tmpfs     4088296      88   4088208       1% /run/shm
none                 tmpfs      102400      16    102384       1% /run/user
<<<postfix_mailq_status:sep(58)>>>
postfix/:the Postfix mail system is running:PID:42
'''

class TestClassAttrAgent:
    AGENTOUTPUT = '''
    <<<check_mk>>>
    Version: 1.6.0p5
    AgentOS: linux
    Hostname: vm-operator
    AgentDirectory: /etc/check_mk
    DataDirectory: /var/lib/check_mk_agent
    SpoolDirectory: /var/lib/check_mk_agent/spool
    PluginsDirectory: /usr/lib/check_mk_agent/plugins
    LocalDirectory: /usr/lib/check_mk_agent/local
    
    <<<df>>>
    tmpfs                tmpfs      817660    1100    816560       1% /run
    none                 tmpfs     4088296      88   4088208       1% /run/shm
    none                 tmpfs      102400      16    102384       1% /run/user
    <<<postfix_mailq_status:sep(58)>>>
    postfix/:the Postfix mail system is running:PID:42
    '''

    def test_sections(self, agent_datasource):
	assert len(agent_datasource.sections) == 3

def test_snmp_datasource(agent_datasource):
    assert len(agent_datasource.sections) == 5
    assert len(agent_datasource.sections[0]) == 7

def test_manual():

    ds = MockAgentDataSource('postfix_mailq_status', AGENTOUTPUT)

    print ds.sections

    assert ds.sections == [[u'postfix/', u'the Postfix mail system is running', u'PID', u'42']]
