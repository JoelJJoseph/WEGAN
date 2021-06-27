import graphene 
from graphql import GraphQLError
from graphene_django import DjangoObjectType
from .models import Causedby, Solution

class CausedbyType(DjangoObjectType):
    class Meta:
        model = Causedby
        fields = ("id", "title")


class SolutionType(DjangoObjectType):
    class Meta:
        model = Solution
        fields = ("id", "title", "causedby", "solution")

#For Queries
class Query(graphene.ObjectType):
    all_causedby = graphene.List(CausedbyType)

    def resolve_all_causedby(root, info):
        return Causedby.objects.all()

    all_solutions = graphene.List(SolutionType)

    def resolve_all_solutions(root, info):
        return Solution.objects.all()

    #For Detailed preview based own disease
    detailed_causedby = graphene.List(CausedbyType, title=graphene.String())
    detailed_solutions = graphene.List(SolutionType, causedby__title=graphene.String())
    
    def resolve_detailed_causedby(root, info, title):
        return Causedby.objects.get(title=title)

    def resolve_detailed_solutions(root, info, causedby__title):
        return Solution.objects.filter(causedby__title=causedby__title)
