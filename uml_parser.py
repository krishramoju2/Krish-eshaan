import ast

class UMLClass:
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.methods = []
        self.parents = []

class UMLParser(ast.NodeVisitor):
    def __init__(self, code_str):
        self.code_str = code_str
        self.classes = []

    def visit_ClassDef(self, node):
        uml_class = UMLClass(node.name)
        # Handle inheritance
        uml_class.parents = [base.id for base in node.bases if isinstance(base, ast.Name)]
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                uml_class.methods.append(item.name)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        uml_class.attributes.append(target.id)
            elif isinstance(item, ast.AnnAssign):
                if isinstance(item.target, ast.Name):
                    uml_class.attributes.append(item.target.id)
        self.classes.append(uml_class)
        self.generic_visit(node)

    def parse(self):
        tree = ast.parse(self.code_str)
        self.visit(tree)
        return self.classes
