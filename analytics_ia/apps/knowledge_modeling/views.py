# -*- coding: utf-8 -*-

__all__ = ['inference_view']

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .bayesian_network import BayesianNetwork
from .models import (
    Alternative,
    Question,
    Subject,
    UserEvidence,
    Evidence,
    UserSubject,
    UserQuestionHistory,
    QuestionEvidence
)
from .serializers import QuestionSerializer


@api_view(['POST'])
def inference_view(request):
    bayesian_network = BayesianNetwork()

    node = request.data['node']
    evidences = request.data['evidences']

    phi_query = bayesian_network.query(
        node=node,
        evidences=evidences
    )

    values = phi_query[node].values

    return Response({'False': values[0], 'True': values[1]})

def create_edges(subjects, parent=None):

    edges = []

    for subject in subjects:

        if parent is not None:
            edges.append((parent.name, subject.name))

        if subject.children.exists() is True:
            edges += create_edges(
                subjects=subject.children.filter(),
                parent=subject
            ) 

    return edges

@api_view(['GET'])
def user_question(request):

    # from .models import Subject

    # subjects = Subject.objects.filter(level=1)

    # edges = list(set(create_edges(subjects=subjects)))

    # from IPython import embed; embed()

    user, created = User.objects.get_or_create(username=request.query_params['username'])

    if not UserQuestionHistory.objects.filter(user=user).exists():

        question = Question.objects.order_by('number').first()

    else:

        questions_count = Question.objects.count()

        history = UserQuestionHistory.objects.filter(user=user).latest('pk')

        history_number = history.question.number

        if history_number < questions_count:

            question = Question.objects.get(number=history_number + 1)

        else:

            question = Question.objects.get(number=1)

    return Response(QuestionSerializer(question).data)


@api_view(['POST'])
def user_answer(request):

    # {"question_id": 2, "alternative_id": 1}

    user = User.objects.get(username=request.query_params['username'])

    with transaction.atomic():

        question = Question.objects.get(pk=request.data['questionId'])

        alternative = Alternative.objects.get(pk=request.data['alternativeId'])

        evidences = question.get_evidences(status=alternative.status)

        bayesian_network = BayesianNetwork()

        UserQuestionHistory.objects.create(
            question=question,
            user=user,
            status=alternative.status
        )

        print(evidences)

        for new_evidence, status in evidences.items():

            evidence = QuestionEvidence.objects.get(name=new_evidence)

            user_evidence, _ = UserEvidence.objects.get_or_create(
                user=user,
                evidence=evidence
            )

            user_evidence.status = status
            user_evidence.save()

            current_evidences = {}

            for predecessor in bayesian_network.get_predecessors(new_evidence):

                # Iteration through all successors of each predecessor
                for successor in bayesian_network.get_successors(predecessor):

                    if UserEvidence.objects.filter(evidence__name=successor, user=user).exists():

                        # Add to the evidence set
                        current_evidences.update({successor: int(UserEvidence.objects.get(evidence__name=successor, user=user).status)})

                print(current_evidences)

                if Subject.objects.filter(name=predecessor).exists():

                    subject = Subject.objects.get(name=predecessor)

                    updated_value = bayesian_network.query_evidence(
                        predecessor,
                        current_evidences
                    )

                    user_subject, _ = UserSubject.objects.get_or_create(
                        user=user,
                        subject=subject
                    )

                    user_subject.value = updated_value
                    user_subject.time_index += 1

                    user_subject.save()

                print(updated_value, predecessor, current_evidences)

                # Clear the evidence set for the next iteration
                current_evidences.clear()

    return Response({
        'alternative_status': alternative.status,
    })


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# {"node": "Catetos", "evidences": {"Classificacao_Angulos": 1}}
# {"node": "Pitagoras", "evidences": {"Catetos": 1, "Hipotenusa": 0}}
# {"node": "Hipotenusa", "evidences": {"Classificacao_Angulos": 1}}

