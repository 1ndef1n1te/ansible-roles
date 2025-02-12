import json 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Node facts in JSON format", required=True)
parser.add_argument("--output", help="Output file name with markdown table of node facts", required=True)
args = parser.parse_args()
input_json = args.input
output_md = args.output 

with open(input_json) as file:
    vms = json.load(file)

with open(output_md, "a") as file:
    heading = "|"
    for column in vms.get("vms")[0].keys():
      heading += f"{column}|"
    file.write(heading)
    file.write("\n")
    file.write(f"|" + "---|" * len(vms.get('vms')[0].keys()))
    file.write("\n")
    for vm in vms.get("vms"):
      vm_str = "|"
      for column in vm.values():
         vm_str += f"{column}|"
      file.write(vm_str + "\n")
         
        
       

        