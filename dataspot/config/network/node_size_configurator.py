from dataspot.config.configurator import Configurator


class NodeSizeConfigurator(Configurator):
    """
    A Node Size object...

    """

    def __init__(self,  config):
        """
        :param config: The config parameter is a dictionary containing all of the Dataspot basic configurations. An
                       example of the basic structure can be found in examples/dataspot_config_example.json
        :type config: dict
        """
        self.__config = config
        self.__node_size_config = None

    def set_config(self, config):
        """
        :param config: The config parameter is a dictionary containing all of the Dataspot basic configurations. An
                       example of the basic structure can be found in examples/dataspot_config_example.json
        :type config: dict
        """
        self.__config = config

    def get_config(self):
        """
        :return: The config parameter is a dictionary containing all of the Dataspot basic configurations. An
                 example of the basic structure can be found in examples/dataspot_config_example.json
        :rtype: dict
        """
        return self.__config

    def set_node_size_config(self, config):
        """
        :param config: The config parameter is a dictionary containing all of the Dataspot basic configurations. An
                       example of the basic structure can be found in examples/dataspot_config_example.json
        :type config: dict
        """
        if not isinstance(config, dict):
            raise TypeError("The configuration that has been provided is not of a dictionary type")

        if not isinstance(config['network_config'], list):
            raise TypeError("The network configuration should be provided in a list")

        if not isinstance(config['network_config'][0], dict):
            raise TypeError("The plot width configuration is not of a dictionary type")

        if 'node_size_config' not in config['network_config'][4].keys():
            raise KeyError("The plot width configuration is not present in the correct location")

        # if not isinstance(config['network_config'][4]['node_size_config'], dict):
        #     raise TypeError("The value of the node size config with should be of a dictionary type")

        node_size_config = config['network_config'][4]['node_size_config']
        self.__node_size_config = node_size_config

    def get_node_size_config(self):
        return self.__node_size_config

    def build(self):
        """
        The build function prepares all of the node size configuration components at once.

        """
        config = self.get_config()
        self.set_node_size_config(config=config)
