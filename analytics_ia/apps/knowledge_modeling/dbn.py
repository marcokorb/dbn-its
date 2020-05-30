# -*- coding: utf-8 -*-

__all__ = [
    'BayesianNetwork'
]

from networkx.algorithms.dag import ancestors, descendants
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel, DynamicBayesianNetwork


class DNB(object):

    def __init__(self):

        self.dbn = DBN()
        self.dbn.add_edges_from(
            [
                (('CA', 0), ('C', 0)),
                (('CA', 0), ('C', 0)),
                (('CT', 0), ('H', 0)),
                (('CA', 0), ('H', 0)),
                (('C', 0), ('P', 0)),
                (('H', 0), ('P', 0)),
                (('CA', 0), ('CA', 1))
            ]
        )

        self.model = DynamicBayesianNetwork()

        self.model.add_edges_from(
            [
                (('Classificacao_Angulos', 0), ('Catetos', 0)),
                (('Classificacao_Triangulos', 0), ('Hipotenusa', 0)),
                (('Classificacao_Angulos', 0), ('Hipotenusa', 0)),
                (('Catetos', 0), ('Pitagoras', 0)),
                (('Hipotenusa', 0), ('Pitagoras', 0))
            ]
        )

        self.model = BayesianModel(
            [
                ('Classificacao_Angulos', 'Catetos'),
                ('Classificacao_Triangulos', 'Hipotenusa'),
                ('Classificacao_Angulos', 'Hipotenusa'),
                ('Catetos', 'Pitagoras'),
                ('Hipotenusa', 'Pitagoras'),
            ]
        )

        x = 4

        cpd_classificao_angulos = TabularCPD(
            variable='Classificacao_Angulos',
            variable_card=2,
            values=[[0.4], [0.6]]
        )

        print(cpd_classificao_angulos)
        print('\n' * x)

        cpd_classificao_triangulos = TabularCPD(
            variable='Classificacao_Triangulos',
            variable_card=2,
            values=[[0.3], [0.7]]
        )

        print(cpd_classificao_triangulos)
        print('\n' * x)

        cpd_catetos = TabularCPD(
            variable='Catetos',
            variable_card=2,
            values=[[0.9, 0.2], [0.1, 0.8]],
            evidence=['Classificacao_Angulos'],
            evidence_card=[2]
        )

        print(cpd_catetos)
        print('\n' * x)

        cpd_hipotenusa = TabularCPD(
            variable='Hipotenusa',
            variable_card=2,
            values=[[0.9, 0.2, 0.3, 0.1],
                    [0.1, 0.8, 0.7, 0.9]],
            evidence=['Classificacao_Angulos', 'Classificacao_Triangulos'],
            evidence_card=[2, 2]
        )

        print(cpd_hipotenusa)
        print('\n' * x)

        cpd_pitagoras = TabularCPD(
            variable='Pitagoras',
            variable_card=2,
            values=[[0.9, 0.3, 0.3, 0.1],
                    [0.1, 0.7, 0.7, 0.9]],
            evidence=['Catetos', 'Hipotenusa'],
            evidence_card=[2, 2]
        )

        print(cpd_pitagoras)
        print('\n' * x)

        self.model.add_cpds(
            cpd_classificao_angulos,
            cpd_classificao_triangulos,
            cpd_catetos,
            cpd_hipotenusa,
            cpd_pitagoras
        )

        self.model.check_model()

        self.inference = VariableElimination(self.model)

    def query(self, node, evidences):

        return self.inference.query([node], evidence=evidences)

    def get_predecessors(self, node):
        """
        Return all predecessors of a given node within the graph
        """
        return list(ancestors(self.model, node))

    def get_successors(self, node):
        """
        Return all successors of a given node within the graph
        """
        return list(descendants(self.model, node))

    def query_evidence(self, concept, evidences=None):
        """
        Return probability of node given evidence set
        """
        if evidences is None:
            evidences = {}
        return self.inference.query(
            [concept],
            evidence=evidences
        )[concept].values[1]

    def query_all_concepts(self, concept_list):
        """
        Return probabilities of all given nodes
        :param concept_list: list of nodes to query
        """
        new_concept_list = []
        # concept_names = [concept.name for concept in concept_list]
        for concept, probability in self.inference.query(concept_list).items():
            new_concept_list.append((concept, probability.values[1]))
        return new_concept_list
