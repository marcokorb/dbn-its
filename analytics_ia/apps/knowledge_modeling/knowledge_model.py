from pgmpy.estimators import BayesianEstimator
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel

from networkx.algorithms.dag import ancestors, descendants

import numpy as np
import pickle

class KnowledgeModel:
    """
    Bayesian network graph representation of student model
    """
    
    def __init__(self):
        """
        Load graph from file and initialize model
        """
        # # Bayesian network graph (evidence and prerequisites)
        # self.graph = BayesianModel([('Seno', 'Passo_Conceito_Seno'), ('Principio_Multiplicativo', 'Passo_Principio_Multiplicativo'),
        #                         ('Multiplicacao', 'Principio_Multiplicativo'), ('Multiplicacao', 'Passo_Multiplicacao_Decimais'),
        #                         ('Cosseno', 'Passo_Conceito_Cosseno')])
                                
        # # CPDs
        # cpd_seno = TabularCPD('Seno', 2, [[0.5, 0.5]])
        # cpd_multiplicacao = TabularCPD('Multiplicacao', 2, [[0.5, 0.5]])
        # cpd_principio_multiplicativo = TabularCPD('Principio_Multiplicativo', 2, [[0.9, 0.5],
        #                                                                           [0.1, 0.5]],
        #                                         evidence=['Multiplicacao'], evidence_card=[2])
        # cpd_passo_conceito_seno = TabularCPD('Passo_Conceito_Seno', 2, [[0.8, 0.1],
        #                                                                 [0.2, 0.9]],
        #                                         evidence=['Seno'], evidence_card=[2])
        # cpd_passo_principio_multiplicativo = TabularCPD('Passo_Principio_Multiplicativo', 2, [[0.8, 0.1],
        #                                                                                       [0.2, 0.9]],
        #                                         evidence=['Principio_Multiplicativo'], evidence_card=[2])
        # cpd_passo_multiplicacao_decimais = TabularCPD('Passo_Multiplicacao_Decimais', 2, [[0.8, 0.1],
        #                                                                                   [0.2, 0.9]],
        #                                         evidence=['Multiplicacao'], evidence_card=[2])
        
        # cpd_cosseno = TabularCPD('Cosseno', 2, [[0.5, 0.5]])
        # cpd_passo_conceito_cosseno = TabularCPD('Passo_Conceito_Cosseno', 2, [[0.8, 0.1],
        #                                                         [0.2, 0.9]], evidence=['Cosseno'], evidence_card=[2])
                                                                
        # # Add probabilities to model
        # self.graph.add_cpds(cpd_seno, cpd_multiplicacao, cpd_principio_multiplicativo, 
        #                 cpd_passo_conceito_seno, cpd_passo_principio_multiplicativo,
        #                 cpd_passo_multiplicacao_decimais, cpd_cosseno, cpd_passo_conceito_cosseno)
        
        # pickle.dump(self.graph, open('its/student_module/graph2.dat', 'wb'))
        
        # Deserialize graph file
        self.graph = pickle.load(open('its/student_module/graph3.dat', 'rb'))
        # Initialize bayesian inference model for graph
        self.inference = VariableElimination(self.graph)
        
        self.graph.check_model()
        
    def get_predecessors(self, node):
        """
        Return all predecessors of a given node within the graph
        """
        return list(ancestors(self.graph, node))
        
    def get_successors(self, node):
        """
        Return all successors of a given node within the graph
        """
        return list(descendants(self.graph, node))
        
    def query_evidence(self, concept, evidences={}):
        """
        Return probability of node given evidence set
        """
        return self.inference.query([concept], evidence=evidences)[concept].values[1]
        
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