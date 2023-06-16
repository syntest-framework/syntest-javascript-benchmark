import subprocess
import os

runs = 37 * 10 * 2
student = "diego"

os.mkdir(student)

project_properties = []
for i in range(1, runs + 1):
    name = "syntest-{}-{}".format(student, i)

    logs = subprocess.check_output(['docker', 'logs', name]).decode("utf-8")

    try:
        subprocess.check_output(['docker', 'cp', "{}:/app/syntest-javascript-benchmark/syntest".format(name), "{}/{}".format(student, name)])

        fid = os.listdir("{}/{}/".format(student, name))[0]

        with open("{}/{}/logs.txt".format(student, name), "w") as text_file:
            text_file.write(logs)

        properties_file_path = "{}/{}/{}/metrics/properties.csv".format(student, name, fid)
        if os.path.isfile(properties_file_path):
            with open(properties_file_path, "r") as text_file:
                if len(project_properties) == 0:
                    project_properties.append(text_file.read().splitlines()[0])
                project_properties.append(text_file.read().splitlines()[1])
    except:
         os.mkdir("{}/{}".format(student, name))
         with open("{}/{}/logs.txt".format(student, name), "w") as text_file:
            text_file.write(logs)

with open("{}/properties.csv".format(student), "w") as text_file:
    text_file.write("\n".join(project_properties))