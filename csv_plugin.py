from nornir.core.deserializer.inventory import Inventory


class read_csv(Inventory):

    def __init__(self, devices_filename,**kwargs):


#    def read_devices (self, devices_filename):
        

        
        hosts = {}
        with open (devices_filename) as devices_file:

            for device_line in devices_file:
                
                device_info = device_line.strip().split(',')
                device = {'NE_Name': device_info[5],
                          
                          'type': device_info[4],
                          'username': device_info[9],
                          'password': device_info[10],
                          'hostname': device_info[13],
                          'groups': [device_info[11]]
                             }
                hosts[device['NE_Name']] = device

  #      print ('\n---------devices---------------\n')

        hosts.pop('NE Name')

        print(hosts)

        groups = {}
        defaults = {} 

        super().__init__(hosts=hosts, groups=groups, defaults=defaults, **kwargs)

#    pprint(devices)
     #   return devices

        
output = read_csv(r"C:\Users\user\AppData\Local\Programs\Python\Python38\inventory\Book1.csv")

#output = read_csv()

#devices = output.read_devices(r"C:\Users\user\AppData\Local\Programs\Python\Python38\inventory\Book1.csv")
