from blockchainetl.jobs.exporters.converters.simple_item_converter import SimpleItemConverter

class ChainIdConverter(SimpleItemConverter):

    def __init__(self, chain_id):
        self.chain_id = chain_id

    def convert_item(self, item):
        if('chain_id' not in item.keys()):
            item['chain_id'] = self.chain_id
        return item