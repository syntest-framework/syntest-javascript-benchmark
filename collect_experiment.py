import subprocess
import os
import sys

config = sys.argv[1]

runs = 37 * 10 * 2

os.mkdir(config)

project_properties = []
for i in range(1, runs + 1):
    name = "syntest-{}-{}".format(config, i)

    logs = subprocess.check_output(['docker', 'logs', name]).decode("utf-8")

    try:
        subprocess.check_output(['docker', 'cp', "{}:/app/syntest-javascript-benchmark/syntest".format(name), "{}/{}".format(config, name)])

        fid = os.listdir("{}/{}/".format(config, name))[0]

        with open("{}/{}/logs.txt".format(config, name), "w") as text_file:
            text_file.write(logs)

        properties_file_path = "{}/{}/{}/metrics/properties.csv".format(config, name, fid)
        if os.path.isfile(properties_file_path):
            with open(properties_file_path, "r") as text_file:
                if len(project_properties) == 0:
                    project_properties.append(text_file.read().splitlines()[0])
                project_properties.append(text_file.read().splitlines()[1])
    except:
         os.mkdir("{}/{}".format(config, name))
         with open("{}/{}/logs.txt".format(config, name), "w") as text_file:
            text_file.write(logs)

with open("{}/properties.csv".format(config), "w") as text_file:
    text_file.write("\n".join(project_properties))