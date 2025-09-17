import os

tree_files = [filename for filename in os.listdir('.') if filename.endswith('.tre')]

nexus_content = "BEGIN Trees;\n"

for i, tree_file in enumerate(tree_files):
    with open(tree_file, 'r') as f:
        tree_content = f.read().strip()[:-1]
        nexus_content += f"Tree gt{i}={tree_content};\n"

nexus_content += "END;"

with open('infer_Network_MPL.nexus', 'w') as f:
    f.write(nexus_content)
