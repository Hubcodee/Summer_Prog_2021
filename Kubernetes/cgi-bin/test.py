# kubeconfig
# rename admin.conf to conf
# move conf to /root/.minikube

import rand_name as rn
import subprocess
import time

action_launch = ["launch", "run", "create"]
images = ["httpd", "centos", "ubuntu", "vimal13/apache-webserver-php"]
pods = ["pos", "po", "pods", "pod"]
deploy = ["deployment", "deploy"]
svc = ["service", "services", "svc"]
scale = ["scale", "increase", "add"]
names = []


def process_str(st):
    stop_words = st.split()

# launching PODS AND DEPLOYEMNT
    def launch_resource(res, cmd):
        for i in images:
            if i in stop_words:
                id = images.index(i)
                image = images[id]
        name = rn.words_fetch().lower()
        names.append(name)
        if res == "pods":
            op = subprocess.getoutput(
                f"sudo kubectl {cmd} {name} --image={image} ")
            print(f"<h1>creating {res} using {image} and name : {name}</h1>")
        elif res == "deploy":
            op = subprocess.getoutput(
                f"sudo kubectl {cmd} {res} {name} --image={image} ")
            print(f"<h1>creating {res} using {image} and name : {name}</h1>")
        print(op)
        time.sleep(20)
        display = subprocess.getoutput(
            f"sudo kubectl get {res} {name} --kubeconfig admin.conf")
        print(display)
        return True

# filtering commands using any() and executing relevant query
    if any(item in action_launch for item in stop_words):
        if any(item in pods for item in stop_words):
            res = "pods"
            cmd = "run"
            launch_resource(res, cmd)

        elif any(item in deploy for item in stop_words):
            res = "deploy"
            cmd = "create"
            launch_resource(res, cmd)

        else:
            print(
                "<h3 style='color:red'>Keyword doesnt match !\nTry different combination</h3>")

# filtering for scaling
    def scale(replicas, name):
        if any(item in deploy for item in stop_words):
            op = subprocess.getoutput(
                f"sudo kubectl scale deployment {name} --replicas={replicas} ")
            print(
                f"<h1>Scaling deployement {name} by {replicas}.</h1>")
            print(op)

    if any(item in scale for item in stop_words):
        for x in stop_words:
            if isinstance(x, int):
                print(x)
                replicas = x
        if len(names) == 0:
            print("No deployment created yet!")
        else:
            # scale deployement
            flag = 0
            index = 0
            for x in names:
                if x in stop_words:
                    flag = 1
                    index = stop_words.index(x)
            if flag == 1:
                scale(replicas, name=stop_words[index])
            else:
                print("Deployment with specified name is not present")
