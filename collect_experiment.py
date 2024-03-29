import subprocess
import os
import sys

config = sys.argv[1]
iterations = int(sys.argv[2])
configurations = int(sys.argv[3])

runs = 109 * iterations * configurations

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
                lines = text_file.read().splitlines()

                if len(lines) < 2:
                    print(f'empty file: {properties_file_path}')
                    break

                if len(project_properties) == 0:
                    project_properties.append(lines[0])

                project_properties.append(lines[1])
    except:
        os.mkdir("{}/{}".format(config, name))
        with open("{}/{}/logs.txt".format(config, name), "w") as text_file:
            text_file.write(logs)

with open("{}/properties.csv".format(config), "w") as text_file:
    text_file.write("\n".join(project_properties))