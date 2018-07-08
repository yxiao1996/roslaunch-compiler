import parse
from xml.dom.minidom import Document

doc = Document()

# add root node
group = doc.createElement('group')
doc.appendChild(group)

def add_node(node_info, root):
    # create node
    node = doc.createElement('node')
    group.appendChild(node)

    # create attributes
    name = doc.createAttribute('name')
    pack = doc.createAttribute('pkg')
    execu = doc.createAttribute('type')

    # add attributes to node
    node.setAttributeNode(name)
    node.setAttributeNode(pack)
    node.setAttributeNode(execu)

    # set attributes' value
    node.setAttribute('name', node_info['name'])
    node.setAttribute('pkg', node_info['pack'])
    node.setAttribute('type', node_info['exec'])


if __name__ == "__main__":
    data = '''MODULE foo(  
                INPUT /a/c
                INPUT /e/f
                OUTPUT /b/d
                OUTPUT /g/h
                NODE(
                    NAME bar
                    INPUT /i
                    OUTPUT /j
                    PACK test0
                    EXEC test0.py
                )
                NODE(
                    NAME foo
                    INPUT /m
                    OUTPUT /n
                    PACK test1
                    EXEC test1.py
                )
                ASSIGN /c = /d
                ASSIGN /e = /f
            )'''

    result = parse.parse(data)
    node_0 = result['node'][0]
    add_node(node_0, group)
    with open('test.xml', 'wb') as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    print(result)

