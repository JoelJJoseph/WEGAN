import graphene
import Disease.schema

class Query(Disease.schema.Query):
    pass


schema = graphene.Schema(query=Query)