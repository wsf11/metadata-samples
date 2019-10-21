# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureSqlTable(Model):
    """AzureSqlTable.

    :param azure_sql_server_uri:
    :type azure_sql_server_uri: str
    :param database_name:
    :type database_name: str
    :param azure_sql_table_name:
    :type azure_sql_table_name: str
    """

    _attribute_map = {
        'azure_sql_server_uri': {'key': 'azure_sql_server_uri', 'type': 'str'},
        'database_name': {'key': 'database_name', 'type': 'str'},
        'azure_sql_table_name': {'key': 'azure_sql_table_name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureSqlTable, self).__init__(**kwargs)
        self.azure_sql_server_uri = kwargs.get('azure_sql_server_uri', None)
        self.database_name = kwargs.get('database_name', None)
        self.azure_sql_table_name = kwargs.get('azure_sql_table_name', None)
