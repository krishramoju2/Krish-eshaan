def generate_drawio_class_diagram(classes):
    xml = '''<mxGraphModel><root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    '''
    x, y = 50, 50
    class_ids = {}
    for idx, cls in enumerate(classes):
        class_id = str(idx + 2)
        class_ids[cls.name] = class_id
        # Class box
        value = f"<b>{cls.name}</b><br/>"
        if cls.parents:
            value += f"<i>Inherits: {', '.join(cls.parents)}</i><br/>"
        if cls.attributes:
            value += "Attributes:<br/>" + "<br/>".join(cls.attributes) + "<br/>"
        if cls.methods:
            value += "Methods:<br/>" + "<br/>".join(cls.methods)
        xml += f'''
        <mxCell id="{class_id}" value="{value}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;" vertex="1" parent="1">
            <mxGeometry x="{x}" y="{y+idx*130}" width="240" height="120" as="geometry"/>
        </mxCell>
        '''
    # Draw inheritance arrows
    arrow_id = len(classes) + 2
    for cls in classes:
        for parent in cls.parents:
            if parent in class_ids:
                xml += f'''
                <mxCell id="{arrow_id}" style="endArrow=block;endFill=1;strokeColor=#000000;" edge="1" parent="1" source="{class_ids[cls.name]}" target="{class_ids[parent]}">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                '''
                arrow_id += 1
    xml += '</root></mxGraphModel>'
    return xml
