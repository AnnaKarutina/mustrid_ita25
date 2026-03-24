from realtionship import Relationship

class Research:
    def __init__(self, relationships):
        for relation in relationships.relations:
            if relation[0].name == "John" and relation[1] == Relationship.PARENT:
                print(f"John has a child called {relation[2].name}")
