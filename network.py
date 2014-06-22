import networkx as nx

class Author:

    # Every BibJSON Document author has a name, id, or ref
    def __init__(self, alias, alias_key='id'):

        self.alias = alias

        for doc in list(COLLECTION.find({'author.' + alias_key : alias})):
            
            self.docs.append(Document(doc, alias_key))

class Document:

    def __init__(self, doc, author_alias_key='name'):

        # Internal Object from the ODM
        self._doc = doc
        self.authors = []

        for author in doc.authors:

            self.authors.append(Author(getattr(author, author_alias_key)))
        
class Neighborhood:

    def push_doc(self, doc):

        for author in doc.authors:

            if author.alias in self.graph[self.root_author.alias]:

                # Weight calculations
                self.graph[self.root_author.alias]['weight'] += 1
            else:
            
                self.graph.add_edge(self.root_author.alias, author.alias, weight=1)
                self.coauthors.append(author)

    def __init__(self, root_author, depth=1, explored_authors=[]):

        self.root_author = root_author
        self.depth = depth
        self.explored_authors = explored_authors.append(self.root_author)
        
        self.graph = nx.DiGraph()

        self.graph.add_nodes_from(map(lambda a: a.alias, self.coauthors.append(self.root_author)))

    def explore(self):

        for coauthor in filter(lambda a: a not in self.explored_authors, self.coauthors):

            i = 1
            while i <= self.depth:
                
                coauthor_neighborhood = Neighborhood(coauthor, self.depth - i, self.explored_authors)
                self.graph = nx.compose(self.graph, coauthor_neighborhood)
                i += 1
                
