from pytest_cmk.data_sources.snmp import MockSNMPDataSource

CHECK='snmptest'

SNMPWALK = '''
.1.42.0 1.42.0
.1.42.1.1.0 0
.1.42.1.1.1 1
.1.42.1.2.0 one
.1.42.1.2.1 two
.1.42.1.3.0 eins
.1.42.1.3.1 zwei
'''

class TestCLassAttrWalk:
    SNMPWALK = """\
        .1.42.0 1.42.0
        .1.42.1.1.0 0
        .1.42.1.1.1 1
        .1.42.1.2.0 foo
        .1.42.1.2.1 bar
        .1.42.1.3.0 alice
        .1.42.1.3.1 bob
        """

    def test_sections(self, snmp_datasource):
        print snmp_datasource._host_sections.sections
        assert len(snmp_datasource.sections) == 2
        assert snmp_datasource.sections[0] == [u'0', u'0', u'alice']
        assert snmp_datasource.sections[1] == [u'1', u'1', u'bob']

def test_snmp_datasource(snmp_datasource):
    assert len(snmp_datasource.sections) == 2
    assert snmp_datasource.sections[0] == [u'0', u'0', u'eins']
    assert snmp_datasource.sections[1] == [u'1', u'1', u'zwei']

def test_manual():

    ds = MockSNMPDataSource('snmptest', [
'.1.42.0 1.42.1',
'.1.42.1.1.0 1.0',
'.1.42.1.1.1 1.1',
'.1.42.1.2.0 2.0',
'.1.42.1.2.1 2.1',
'.1.42.1.3.0 3.0',
'.1.42.1.3.1 3.1',
    ])

    assert len(ds.sections) == 2
    assert ds.sections[0] == [u'0', u'1.0', u'3.0']
    assert ds.sections[1] == [u'1', u'1.1', u'3.1']
