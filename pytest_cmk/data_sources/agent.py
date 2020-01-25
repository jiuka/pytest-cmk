from cmk_base.data_sources.abstract import CheckMKAgentDataSource


class MockAgentDataSource(CheckMKAgentDataSource):

    def __init__(self, name, agent):
        super(MockAgentDataSource, self).__init__('pytest', '127.127.127.127')

        self._name = name
        self._agent = agent
        self.run()

    def _execute(self):
        return self._agent

    def id(self):
        return "agent"

    def describe(self):
        return "MockTCP: pytest"

    def _read_cache_file(self):
        return False

    def _write_cache_file(self, raw_data):
        pass

    @property
    def sections(self):
        return self._host_sections.sections.get(self._name)
