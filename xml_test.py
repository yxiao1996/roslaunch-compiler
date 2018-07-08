#import xml.etree.ElementTree as ET

#a = ET.Element('launch', {'test': 'true'})
#b = ET.SubElement(a, 'node', {'name' : 'foo', 'package': 'foo'})
#c = ET.SubElement(a, 'node', {'name' : 'bar', 'package': 'bar'})
#ET.dump(a)
#et = ET.ElementTree(a)
#et.write('test.xml', 'utf-8')
from xml.dom.minidom import Document

doc = Document()

# root node

orderlist = doc.createElement('orderlist')

doc.appendChild(orderlist)

# first layer

order = doc.createElement('order')

orderlist.appendChild(order)

# attribute

att = doc.createAttribute('test_att')

order.setAttributeNode(att)

order.setAttribute('test_att', 'test')

# new element

customer = doc.createElement('customer')

customer_text = doc.createTextNode('foo')

customer.appendChild(customer_text)

order.appendChild(customer)

with open('test.xml', 'wb') as f:
    f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
