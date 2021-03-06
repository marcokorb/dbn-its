"""DBNVT module."""
import pyAgrum as gum

from .models import Course


class DBNModel(object):
    """DBN class."""

    def __init__(self, network):

        self.network = network

        self.network_subjects = network.subjects.all()
        self.twodbn = gum.BayesNet()

        self.arcs_by_code = []
        self.arcs_by_id = []
        self.nodes = []

        self.setup()

    @staticmethod
    def code_as_number(code):
        """Convert a text code to numeric value."""
        return sum(ord(s) for s in code)

    def add_arc(self, parent, child):
        """Add a new arc to the network."""
        self.twodbn.addArc(parent, child)
        self.arcs_by_code.append((parent, child))
        self.arcs_by_id.append(
            (self.code_as_number(parent), self.code_as_number(child))
        )

    def add_node(self, code):
        """Add a new node to the network."""
        node = self.twodbn.add(
            gum.LabelizedVariable(code, code, 2), self.code_as_number(code)
        )

        self.nodes.append(node)

        return node

    def setup_arcs(self):
        """Set up network arcs."""
        for network_subject in self.network_subjects:

            evidences = network_subject.evidences.all()
            parent_subjects = network_subject.subjects.all()
            subject = network_subject.subject

            subjec_code0 = f"{subject.code}0"
            subjec_codet = f"{subject.code}t"

            self.add_arc(subjec_code0, subjec_codet)

            for parent_subject in parent_subjects:

                parent_subjec_code0 = f"{parent_subject.code}0"
                parent_subjec_codet = f"{parent_subject.code}t"

                self.add_arc(parent_subjec_code0, subjec_code0)
                self.add_arc(parent_subjec_codet, subjec_codet)

            for evidence in evidences:

                self.add_arc(subjec_code0, f"{evidence.code}0")
                self.add_arc(subjec_codet, f"{evidence.code}t")

    def setup_nodes(self):
        """Set up network nodes."""
        for network_subject in self.network_subjects:

            evidences = network_subject.evidences.all()
            subject = network_subject.subject

            self.add_node(f"{subject.code}0")
            self.add_node(f"{subject.code}t")

            for evidence in evidences:

                self.add_node(f"{evidence.code}0")
                self.add_node(f"{evidence.code}t")

    def setup(self):
        """Set up dbn."""
        self.setup_nodes()


class DBN(object):
    """DBN class."""

    def __init__(self, course=None):

        course = Course.objects.get(id=1)

        DBNModel(network=course.network)

        from IPython import embed

        embed()
