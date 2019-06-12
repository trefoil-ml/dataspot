from dataspot.network.nodes.node_sizes_networker import NodeSizesNetworker
from dataspot.network.nodes.node_colors_networker import NodeColorsNetworker
from dataspot.network.nodes.node_labels_networker import NodeLabelsNetworker
from dataspot.network.nodes.node_list_networker import NodeListNetworker
from dataspot.network.nodes.node_scores_networker import NodeScoresNetworker


class NodeNetworkBuilder:

    def __init__(self):
        self.__nodes = None
        self.__node_labels = None
        self.__node_colors = None
        self.__node_root_scores = None
        self.__node_usage_scores = None
        self.__node_sizes = None

    def set_nodes(self, graph):
        node_list_networker = NodeListNetworker()
        node_list_networker.build(graph=graph)
        self.__nodes = node_list_networker.get_node()

    def get_nodes(self):
        return self.__nodes

    def set_node_labels(self, nodes, grouped_nodes, grouped_legend):
        node_labels_networker = NodeLabelsNetworker()
        node_labels_networker.build(nodes=nodes, grouped_nodes=grouped_nodes, grouped_legend=grouped_legend)
        self.__node_labels = node_labels_networker.get_node()

    def get_node_labels(self):
        return self.__node_labels

    def set_node_colors(self, nodes, grouped_nodes, grouped_colors):
        node_colors_networker = NodeColorsNetworker()
        node_colors_networker.build(nodes=nodes, grouped_nodes=grouped_nodes, grouped_colors=grouped_colors)
        self.__node_colors = node_colors_networker.get_node()

    def get_node_colors(self):
        return self.__node_colors

    def set_node_scores(self, nodes, relationships, grouped_weights):
        node_scores_networker = NodeScoresNetworker()
        node_scores_networker.build(nodes=nodes, relationships=relationships, grouped_weights=grouped_weights)
        self.__node_root_scores = node_scores_networker.get_node_root_scores()
        self.__node_usage_scores = node_scores_networker.get_node_usage_scores()

    def get_node_root_scores(self):
        return self.__node_root_scores

    def get_node_usage_scores(self):
        return self.__node_usage_scores

    def set_node_sizes(self, nodes, relationships, node_size_config, grouped_weights):
        node_sizes_networker = NodeSizesNetworker()
        node_sizes_networker.build(nodes=nodes, relationships=relationships, node_size_config=node_size_config,
                                   grouped_weights=grouped_weights)
        self.__node_sizes = node_sizes_networker.get_node()

    def get_node_sizes(self):
        return self.__node_sizes

    def build(self, graph, relationships, node_size_config, grouped_nodes, grouped_colors, grouped_weights,
              grouped_legend):
        self.set_nodes(graph=graph)

        nodes = self.__nodes
        self.set_node_sizes(nodes=nodes, relationships=relationships, node_size_config=node_size_config,
                            grouped_weights=grouped_weights)
        self.set_node_colors(nodes=nodes, grouped_nodes=grouped_nodes, grouped_colors=grouped_colors)
        self.set_node_labels(nodes=nodes, grouped_nodes=grouped_nodes, grouped_legend=grouped_legend)
        self.set_node_scores(nodes=nodes, relationships=relationships, grouped_weights=grouped_weights)