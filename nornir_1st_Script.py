from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.functions.text import print_result
#from nornir.plugins.tasks.files import write_file

from nornir.plugins.tasks import text, files
import re

def grab_mac(task):


    task.run(
    task=netmiko_send_command, use_timing = True,
    command_string="cisco"
)

    output = task.run(task=netmiko_send_command, use_timing = True, command_string="show mac-address-table")

    
    mac_extraction = output.result

    macregex = re.compile(r'Showing \d+ out of \d+ entries')
    regexout = macregex.search(mac_extraction)
    mac_count = regexout.group() + "\n"

    print(mac_count)

 #   output1 = task.run(task=netmiko_send_command, use_timing = True, command_string="show lan-dcn arp")


    task.run(
        task=files.write_file,
        filename= 'show_mac.txt',
        content = mac_count,
        append = True)

 #   print(output[0])

#    print(type(output[0]))



def main():
    

    nr = InitNornir(inventory={
            "plugin": "nornir.plugins.inventory.csv_plugin.read_csv"})


    result = nr.run(
    task=grab_mac,
    num_workers=500)


    nr.close_connections()

    print(result)


if __name__ == "__main__":

    main()


#print(nr)

#print(nr.inventory.hosts)


    
 #   print(result['10.197.11.68'])

 #   print(result['10.197.11.68'][3])

"""    

    target = nr.filter(hostname="10.197.22.182")

    target.run(
    task=netmiko_send_command, use_timing = True,
    command_string="ericsson"
)

    targrt.run(
    task=grab_info,
 #   command_string="show lan-dcn arp",
    num_workers=400)

    global dict1
    
    dict1 = {}

    

    for key, value in result.items():

        dict1[key]={'1st': result[key][2], '2nd': result[key][3]}
        

        print(key)
        print("####" * 20)
        print(value)

        print("####" * 20)

        print(dict1)

        print(dict1[key]['2nd'])




"""

#print(nr.inventory.groups)
