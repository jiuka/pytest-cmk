TEST = 'dell_mdss'

import cmk_base.snmp as snmp
import cmk_base.snmp_utils as snmp_utils
from cmk_base.data_sources.snmp import SNMPDataSource


class MockSNMPDataSource(SNMPDataSource):

    def __init__(self, name, walk):
        super(MockSNMPDataSource, self).__init__('pytest', '127.127.127.127')

        self._name = name
        snmp._g_walk_cache[self._hostname] = walk
        self.run()

    def get_check_plugin_names(self):
        return [self._name]

    @property
    def _snmp_config(self):
        return snmp_utils.SNMPHostConfig(
            is_ipv6_primary=False,
            hostname=self._hostname,
            ipaddress='127.127.127.127',
            credentials=None,
            port=None,
            is_bulkwalk_host=None,
            is_snmpv2or3_without_bulkwalk_host=None,
            bulk_walk_size_of=None,
            timing=None,
            oid_range_limits=None,
            snmpv3_contexts=None,
            character_encoding=None,
            is_usewalk_host=True,
            is_inline_snmp_host=None,
        )

    def _read_cache_file(self):
        return False

    @property
    def sections(self):
        return self._host_sections.sections.get(self._name)

