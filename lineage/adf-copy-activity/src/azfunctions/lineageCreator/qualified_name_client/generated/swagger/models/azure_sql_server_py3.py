# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureSqlServer(Model):
    """AzureSqlServer.

    :param uri:
    :type uri: str
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, *, uri: str=None, **kwargs) -> None:
        super(AzureSqlServer, self).__init__(**kwargs)
        self.uri = uri
