username = ''
password = ''
franchise = ''
subscriber = ''
department = ''
debug = True

from mrw.picking import *
from mrw.utils import services

print "MRW services"
services = services()
print services

with API(username, password, franchise, subscriber, department, debug=debug) as mrw_api:
    print "Test connection"
    print mrw_api.test_connection()

with Picking(username, password, franchise, subscriber, department, debug=debug) as picking_api:
    print "Send a new shipment"

    data = {}
    #~ data['codigo_direccion'] = ''
    #~ data['codigo_via'] = ''
    data['via'] = 'Doctor Fleming, 28'
    #~ data['numero'] = ''
    #~ data['resto'] = ''
    data['codigo_postal'] = '08720'
    data['poblacion'] = 'Vilafranca del Penedes'
    #~ data['provincia'] = ''
    data['nif'] = 'B64425879'
    data['nombre'] = 'Zikzakmedia'
    data['telefono'] = '938902108'
    data['contacto'] = 'Raimon Esteve Cusine'
    data['atencion_de'] = 'Raimon Esteve Cusine'
    data['observaciones'] = 'Test MRW envio'
    #~ data['fecha'] = ''
    data['referencia'] = '123456789'
    data['codigo_servicio'] = '0800'
    #~ data['bultos'] = ''
    #~ data['peso'] = ''
    data['reembolso'] = 'O'
    data['importe_reembolso'] = '12,45'

    reference, error = picking_api.create(data)
    print reference

    if error:
        print error

    print "Get PDF label"
    data = {}
    data['numero'] = reference
    #~ data['separador_numero'] = ''
    #~ data['inicio_fecha'] = ''
    #~ data['fin_envio'] = ''
    #~ data['etiqueta_envio'] = ''
    #~ data['top_margin'] = ''
    #~ data['left_margin'] = ''

    label = picking_api.label(data)
    if label:
        filename = '/tmp/mrw-%s-label.pdf' % reference
        with open(filename,"wb") as f:
            f.write(label)
        print "Generated PDF label in %s" % filename
    else:
        print "Error get pdf file"
