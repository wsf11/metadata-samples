# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdfSparkActivity(Model):
    """AdfSparkActivity.

    :param datafactory_name:
    :type datafactory_name: str
    :param pipeline_name:
    :type pipeline_name: str
    :param spark_activity_name:
    :type spark_activity_name: str
    """

    _attribute_map = {
        'datafactory_name': {'key': 'datafactory_name', 'type': 'str'},
        'pipeline_name': {'key': 'pipeline_name', 'type': 'str'},
        'spark_activity_name': {'key': 'spark_activity_name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdfSparkActivity, self).__init__(**kwargs)
        self.datafactory_name = kwargs.get('datafactory_name', None)
        self.pipeline_name = kwargs.get('pipeline_name', None)
        self.spark_activity_name = kwargs.get('spark_activity_name', None)
