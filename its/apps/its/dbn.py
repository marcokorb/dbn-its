"""DBN helper module."""
import pyAgrum as gum

from .models import Course


class DBNModel(object):
    """DBN util."""

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

    def add_probabilities(self, probabilities):
        """Add a new probability table to the network."""
        for probability in probabilities:
            if "relations" in probability:
                for relation in probability["relations"]:
                    condition = {
                        code["code"]: int(code["status"])
                        for code in relation["codes"]
                    }
                    self.twodbn.cpt(probability["code"])[condition] = relation[
                        "values"
                    ]
            else:
                self.twodbn.cpt(probability["code"]).fillWith(
                    probability["values"]
                )

    def setup_arcs(self):
        """Set up network arcs."""
        for network_subject in self.network_subjects:

            # Todo: We should cache the evidences to avoid double queries.
            #  It is used here and in setup_nodes.
            evidences = network_subject.evidences.all()
            parent_subjects = network_subject.network_subjects.all()

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

    def setup_probabilities(self):
        """Set up probabilities."""
        for network_subject in self.network_subjects:

            probabilities = network_subject.probabilities.get()

            self.add_probabilities(
                probabilities=probabilities.subjects_probabilities
            )
            self.add_probabilities(
                probabilities=probabilities.evidences_probabilities
            )

    def setup(self):
        """Set up dbn."""
        self.setup_nodes()
        self.setup_arcs()
        self.setup_probabilities()

    def inference(self, evidences, subject):
        """Do inference for given subject according to evidences."""
        ie = gum.VariableElimination(self.twodbn)
        ie.setEvidence(evidences)
        ie.makeInference()

        return ie.posterior(subject)


class DBN(object):
    """DBN class."""

    def __init__(self, course=None):
        course = Course.objects.get(id=1)

        DBNModel(network=course.network)

        from IPython import embed

        embed()
