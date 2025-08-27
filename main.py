from uml_parser import UMLDiagramGenerator
from drawio_xml_generator import generate_drawio_xml
from ieee_doc_generator import generate_ieee_doc

def process_python_code(code_text):
    gen = UMLDiagramGenerator(code_text)
    gen.parse()
    classes = gen.get_classes()
    xml_str = generate_drawio_xml(classes)
    ieee_doc = generate_ieee_doc(classes, code_text)
    return xml_str, ieee_doc

# Usage Example
if __name__ == "__main__":
    code_text = '''...your python code here...'''
    xml_out, ieee_out = process_python_code(code_text)
    with open("uml.drawio", "w") as f:
        f.write(xml_out)
    with open("documentation.md", "w") as f:
        f.write(ieee_out)
