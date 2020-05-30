# -*- coding: utf-8 -*-

__all__ = ['api_root']

from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes((AllowAny, ))
def api_root(request):
    return Response({
        'inference': reverse(
            'knowledge_modeling:inference',
            request=request
        ),
        'question': reverse(
            'knowledge_modeling:question',
            request=request
        ),
        'user_answer': reverse(
            'knowledge_modeling:user_answer',
            request=request
        ),
        'user_question': reverse(
            'knowledge_modeling:user_question',
            request=request
        ),
        'concepts_form': reverse(
            'conceptual_map:concepts_form',
            request=request
        ),
        'concepts': reverse(
            'conceptual_map:concepts',
            request=request
        ),
        'users_concepts': reverse(
            'conceptual_map:users_concepts',
            request=request
        ),
        'users_from_concepts': reverse(
            'conceptual_map:users_from_concepts',
            request=request
        )
    })
