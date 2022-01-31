# Nmap con Python 3

Nmap es una utilidad gratuita para descubrimiento de redes y auditar la seguridad de las mismas. Se puede utilizar para monitorizar los dispositivos de red, comprobar su estado y el estado de sus servicios en funcionamiento, inventariarlos, etc.

Esta utilidad se puede descargar desde su web en [https://nmap.org](https://nmap.org) y se puede usar desde la terminal o símbolo del sistema usando los parámetros y valores adecuados, y a través de una interfaz GUI gracias a Zenmap, utilidad que ayuda en la construcción del comando, parámetros y valores y que muestra el resultado en un entorno gráfico.

Comentaros que lo que voy a explicar es para que podáis usarlo en vuestras redes o con permiso escrito del propietario de la misma ya que en algunos países, el uso de estas herramientas en una red que no es vuestra, podría considerarse un delito. Daros por tanto por advertidos.

Si no disponéis de una red de dispositivos, siempre es posible utilizar algún software como VirtualBox o VMware Player para montar un laboratorio donde configurar una switch virtual e instalar máquinas virtuales conectadas a este switch.

En cualquier caso, lo que a nosotros nos interesa es poder usarlo con Python, por lo que tras su instalación en nuestro sistema operativo usando la información disponible en su web, haremos uso de un módulo que nos permitirá hacerlo y que se llama Python-nmap. Para comenzar a usarlo debemos instalarlo y esto lo conseguiremos escribiendo el siguiente comando en la terminal o símbolo del sistema de nuestro sistema operativo:

`pip3 install python-nmap`  
Para su funcionamiento básico primero hemos de importar el módulo, cosa que hacemos escribiendo:

`import nmap`  
Vamos a mostrar que versión del módulo estamos usando haciendo uso del método `__version__`.

\>>> `nmap.__version__`  
>'0.6.1'  
Si queremos ver los métodos que existen en el módulo nmap usamos dir() de la siguiente forma:

\>>> `dir(nmap)`  
>['ET', 'PortScanner', 'PortScannerAsync', 'PortScannerError', 'PortScannerHostDict', 'PortScannerYield', 'Process', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__last_modification__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'convert_nmap_output_to_encoding', 'csv', 'io', 'nmap', 'os', 're', 'shlex', 'subprocess', 'sys']

Para mostrar el funcionamiento del módulo nos interesa el método PortScanner ya que es el que usaremos para realizar un escaneo de puertos en los dispositivos de nuestra red.

Vamos a ver los métodos disponibles usando dir() de nuevo.

\>>> `dir(nmap.PortScanner)`
>['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'all_hosts', 'analyse_nmap_xml_scan', 'command_line', 'csv', 'get_nmap_last_output', 'has_host', 'listscan', 'nmap_version', 'scan', 'scaninfo', 'scanstats']

Entre otros los métodos que nos interesan ahora son nmap_version que nos mostrará la versión de nmap que estamos usando, scan, que realizará el escaneo de puertos, command_line que nos mostrará el comando y parámetros usados en nuestro escaneo y scaninfo para ver la información producida por el escaneo.

Escanearemos los puertos 80 (http), 443 (https) buscando servidores web disponibles, el puerto 21 (ftp), 22 (ssh) y 3389 (rdp) para ver que equipos tienen configurado y accesible el escritorio remoto.

Vamos a ver que versión de nmap tenemos instalada.

\>>> `nmap.PortScanner().nmap_version()`  
>(7, 91)  

Y comenzamos creando un objeto del tipo nmap.PortScanner con el siguiente comando:

`ep = nmap.PortScanner()`  
Y vamos a lanzar el escaneo usando el método scan de `nmap.PortScanner()`

`ep.scan(‘192.168.0.1’,’21,22,80,443,3389’,’-v’)`  
Hemos usado la opción verbose (-v) para mostrar el resultado en la consola, sin esta opción no se habría mostrado ningún resultado. Así podemos ver que lo que el resultado del escaneo es un diccionario con claves como command_line, scaninfo, services, etc.

Vamos a observar el comando utilizado para realizar el escaneado con command_line() el cual nos muestra lo que se ha pasado a nmap para obtener ese resultado. 

\>>> `ep.command_line()` 
`nmap -oX - -p 21,22,80,443,3389 -v 192.168.0.1`  
Para ver una lista de todos los hosts involucrados en el escaneo usamos el método all_hosts(), en este caso concreto solo hay uno.

\>>> `ep.all_hosts()`  
>['192.168.0.1']  
Pero esta lista sería diferente si nuestro escaneo hubiera sido otro, por ejemplo: 

`ep.scan(‘192.168.0.1-10’,’21,22,80,443,3389’)`  
 En ese caso habríamos obtenido una lista con los siguientes resultados 

>['192.168.0.1', '192.168.0.10', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5', '192.168.0.6', '192.168.0.7', '192.168.0.8', '192.168.0.9'].  

Dejando de lado este último dato y volviendo al anterior, podríamos ver el diccionario obtenido para ese host escribiendo lo siguiente:

\>>> `ep[‘192.168.0.1’]`  
El resultado sería algo parecido a esto que contiene información de los puertos, nombres, estados, razones, etc.

>{'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '192.168.0.1'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'syn-ack'}, 'tcp': {21: {'state': 'closed', 'reason': 'conn-refused', 'name': 'ftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 443: {'state': 'open', 'reason': 'syn-ack', 'name': 'https', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3389: {'state': 'closed', 'reason': 'conn-refused', 'name': 'ms-wbt-server', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}  

Aquí está toda la información para ese host. Por ejemplo podemos saber si el host está vivo revisando el estado del host con state().

\>>> `ep['192.168.0.1'].state()`   
>'up'  

Los protocolos usados:

\>>> `ep['192.168.0.1'].all_protocols()`  
>['tcp']  

Podemos revisar el estado del puerto tcp 80.

\>>> `ep[‘192.168.0.1’]['tcp'][80]`  
>{'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}  

Leído al revés se entiende mejor, puerto 80, protocolo tcp del host 192.168.0.1.

También vamos a mirar el estado del puerto 80.

\>>> `ep[‘192.168.0.1’]['tcp'][80]['state']`  
>'open'  

La razón de su estado, que indica el método usado para averiguar si está abierto.

\>>> `ep[‘192.168.0.1’]['tcp'][80]['reason']`  
>'syn-ack'  

Y el nombre del servicio.

\>>> `ep[‘192.168.0.1’]['tcp'][80]['name']`  
>'http'  

Si quisiéramos obtener todos estos datos en un formato mas legible podríamos usar el método csv de la siguiente forma.

\>>> `ep.csv()`
>'host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe\r\n  192.168.0.1;;;tcp;21;ftp;closed;;;conn-refused;;3;\r\n  192.168.0.1;;;tcp;22;ssh;open;;;syn-ack;;3;\r\n  192.168.0.1;;;tcp;80;http;open;;;syn-ack;;3;\r\n  192.168.0.1;;;tcp;443;https;open;;;syn-ack;;3;\r\n  192.168.0.1;;;tcp;3389;ms-wbt-server;closed;;;conn-refused;;3;\r\n'  

El resultado podríamos importarlo en cualquier hoja de cálculo.

| host | hostname | hostname_type | protocol | port	name | state | product | extrainfo | reason | version | conf | cpe |
| --- | --- | --- | --- | --- |	--- | --- | --- | --- | --- | --- | --- |
| 192.168.0.1 | | | tcp | 21 | ftp | closed | | | conn-refused | | 3 |
| 192.168.0.1 | | | tcp | 22 | ssh | open | | | syn-ack | | 3 |
| 192.168.0.1 | | | tcp | 80 | http | open | | | syn-ack | | 3 |
| 192.168.0.1 | | | tcp | 443 | https | open | | | syn-ack | | 3 |
| 192.168.0.1 | | | tcp | 3389 | ms-wbt-server | closed | | | conn-refused  | | 3 |
