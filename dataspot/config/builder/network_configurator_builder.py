from dataspot.config.network.plot_height_configurator import PlotHeightConfigurator
from dataspot.config.network.plot_width_configurator import PlotWidthConfigurator
from dataspot.config.network.xrange_configurator import XRangeConfigurator
from dataspot.config.network.yrange_configurator import YRangeConfigurator
from dataspot.config.network.node_size_configurator import NodeSizeConfigurator
from dataspot.config.network.golden_sources_configurator import GoldenSourcesConfigurator


class NetworkConfiguratorBuilder:

    def __init__(self):
        self.__plot_width = None
        self.__plot_height = None
        self.__x_range = None
        self.__y_range = None
        self.__node_size_config = None
        self.__golden_sources = None

    def set_plot_width(self, config):
        plot_width_configurator = PlotWidthConfigurator()
        plot_width_configurator.build(config=config)
        self.__plot_width = plot_width_configurator.get_config()

    def get_plot_width(self):
        return self.__plot_width

    def set_plot_height(self, config):
        plot_height_configurator = PlotHeightConfigurator()
        plot_height_configurator.build(config=config)
        self.__plot_height = plot_height_configurator.get_config()

    def get_plot_height(self):
        return self.__plot_height

    def set_x_range(self, config):
        x_range_configurator = XRangeConfigurator()
        x_range_configurator.build(config=config)
        self.__x_range = x_range_configurator.get_config()

    def get_x_range(self):
        return self.__x_range

    def set_y_range(self, config):
        y_range_configurator = YRangeConfigurator()
        y_range_configurator.build(config=config)
        self.__y_range = y_range_configurator.get_config()

    def get_y_range(self):
        return self.__y_range

    def set_node_size_config(self, config):
        node_size_configurator = NodeSizeConfigurator()
        node_size_configurator.build(config=config)
        self.__node_size_config = node_size_configurator.get_config()

    def get_node_size_config(self):
        return self.__node_size_config

    def set_golden_sources(self, config):
        golden_sources_configurator = GoldenSourcesConfigurator()
        golden_sources_configurator.build(config=config)
        self.__golden_sources = golden_sources_configurator.get_config()

    def get_golden_sources(self):
        return self.__golden_sources

    def build(self, config):
        self.set_plot_width(config=config)
        self.set_plot_height(config=config)
        self.set_x_range(config=config)
        self.set_y_range(config=config)
        self.set_node_size_config(config=config)
        self.set_golden_sources(config=config)

