import graphviz

# Create a tree visualization for Exercise 2
tree = graphviz.Digraph(format="png", filename="exercise2_tree")

# Adding nodes and edges based on the XML structure
tree.node("person", "person")
tree.node("name", "name: John Smith")
tree.node("occupation", "occupation: Graphic Designer")
tree.node("address", "address")
tree.node("street", "street: 456 Elm Street")
tree.node("city", "city: Metropolis")
tree.node("state", "state: CA")
tree.node("zipcode", "zipcode: 90210")
tree.node("hobbies", "hobbies")
tree.node("hobby1", "hobby: Sketching")
tree.node("hobby2", "hobby: Cycling")
tree.node("hobby3", "hobby: Cooking")

# Connect nodes to represent hierarchy
tree.edges([
    ("person", "name"),
    ("person", "occupation"),
    ("person", "address"),
    ("address", "street"),
    ("address", "city"),
    ("address", "state"),
    ("address", "zipcode"),
    ("person", "hobbies"),
    ("hobbies", "hobby1"),
    ("hobbies", "hobby2"),
    ("hobbies", "hobby3"),
])

# Render the tree
tree.render(cleanup=False)
"exercise2_tree.png"
