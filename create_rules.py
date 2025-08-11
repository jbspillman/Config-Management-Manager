"""
Global Policies for All Platforms
    > Apply to everything, unless setting applied at lower level.

Regional Policies (Geographic or Other Special Requirements)
    > NAMR, EMEA, APAC, SPECIAL

Site based Policies ( Geographic or Other Special Requirements)
    > Data Center, Small Site, etc.

Environment Designation Policies
    > PRD, UAT, TST, LAB, SPECIAL

Use Case or Work Load Policies
    > Application, User, Worm, Archive, Special

Product-Platform Specific Policies
    > Product A, Product B, Product C ( have to diverge at some point )

RBAC ( Roll Based Access Controls )
    > Security is largely based on Product, Use Case, Environment, etc.

Cluster Configuration Rules
    > Cluster specific settings based on Product, etc.

Namespace Configuration Rules
    > Namespace specific settings based on Cluster, Use Case, Env, etc.

Storage Path Configuration Rules
     > Volume or Path specific settings.
"""
import json
import os

script_folder = os.path.dirname(os.path.abspath(__file__))
config_rules = os.path.join(script_folder, 'config_rules')
os.makedirs(config_rules, exist_ok=True)

""" configuration rules files """
cfg_globals = os.path.join(script_folder, 'config_rules', 'globals.json')
cfg_regionals = os.path.join(script_folder, 'config_rules', 'regionals.json')
cfg_sites = os.path.join(script_folder, 'config_rules', 'sites.json')
cfg_environments = os.path.join(script_folder, 'config_rules', 'environments.json')
cfg_patterns = os.path.join(script_folder, 'config_rules', 'patterns.json')
cfg_platforms = os.path.join(script_folder, 'config_rules', 'platforms.json')

cfg_clusters = os.path.join(script_folder, 'config_rules', 'clusters.json')
cfg_namespaces = os.path.join(script_folder, 'config_rules', 'namespaces.json')
cfg_storage_paths = os.path.join(script_folder, 'config_rules', 'storage_paths.json')

cfg_platform_rbac = os.path.join(script_folder, 'config_rules', 'platform_rbac.json')
cfg_other_configs = os.path.join(script_folder, 'config_rules', 'other_configs.json')


""" put these in the order of desired enforcement priority. """
weighted_configuration_list = [
    {'id': 'globals', 'name': 'Global', 'description': 'Organization-wide baseline policies', 'file': f'{cfg_globals}'},
    {'id': 'regionals', 'name': 'Regional', 'description': 'Geographic region policies', 'file': f'{cfg_regionals}'},
    {'id': 'sites', 'name': 'Site', 'description': 'Geographic site or datacenter policies', 'file': f'{cfg_sites}'},
    {'id': 'environments', 'name': 'Environment', 'description': 'Environment specific policies', 'file': f'{cfg_environments}'},
    {'id': 'platforms', 'name': 'Platform', 'description': 'Storage platform policies', 'file': f'{cfg_patterns}'},
    {'id': 'patterns', 'name': 'Pattern', 'description': 'Pattern based policies', 'file': f'{cfg_platforms}'},
    {'id': 'clusters', 'name': 'Cluster', 'description': 'Cluster specific policies', 'file': f'{cfg_clusters}'},
    {'id': 'namespaces', 'name': 'Namespace', 'description': 'Namespace specific policies', 'file': f'{cfg_namespaces}'},
    {'id': 'storage_paths', 'name': 'Storage Path', 'description': 'Storage Path specific policies', 'file': f'{cfg_storage_paths}'},
    {'id': 'security_rbac', 'name': 'RBAC', 'description': 'Role Based Access Control policies', 'file': f'{cfg_platform_rbac}'},
    {'id': 'other_configs', 'name': 'Other', 'description': 'Other random policies', 'file': f'{cfg_other_configs}'}
]

def update_key_everywhere(the_data, target_key, new_value):
    """
    Recursively updates the value of a target_key everywhere it appears
    in a nested dictionary or list structure.

    Args:
        the_data (dict or list): The dictionary or list to traverse.
        target_key (str): The key whose value needs to be updated.
        new_value: The new value to set for the target_key.
    """
    if isinstance(the_data, dict):
        for the_key, the_value in the_data.items():
            if the_key == target_key:
                the_data[the_key] = new_value
            else:
                update_key_everywhere(the_value, target_key, new_value)
    elif isinstance(the_data, list):
        for the_item in the_data:
            update_key_everywhere(the_item, target_key, new_value)


''' load the configuration files based on the list. '''
print("Changing weights based on order and number of items in the list.")
all_data = {}
the_weight = 0
weight_step = 500
for item in weighted_configuration_list:
    the_weight += weight_step
    with open(item['file'], 'r', encoding="utf-8") as file:
        data = json.load(file)
    update_key_everywhere(data, "priority", the_weight)
    all_data.update(data)
p_all_data = json.dumps(all_data, indent=4)
# print(p_all_data)
cfg_combined =  os.path.join(script_folder, 'config_rules', '9999_All_Weighted_Configuration_Rules.json')
with open(cfg_combined, 'w', encoding="utf-8") as f:
    f.write(p_all_data)

