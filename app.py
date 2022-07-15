#Server flask web app
from flask import Flask, request, jsonify
import os
from jinja2 import Template

app = Flask(__name__)

@app.route('/report-data',methods=['POST'])
def record_ssh_attempts():
    data = request.json
    f = open("alpha_clients/" + data["node_hostname"] + ".txt", "w")
    f.write(data['ssh_attempts'] + " ssh log-in attempts were made at " + data["node_hostname"])
    f.close()
    print(data)
    return jsonify(data)

@app.route('/get-data',methods=['POST'])
def display_ssh_attempts():
    node_files = os.listdir("alpha_clients")
    data_list=[]
    for file in node_files:
        f = open("alpha_clients/" + file)
        data_list.append(f.read())
        f.close()
    metrics_template = Template("{% for data in data_list %}{{data}}\n {% endfor %}")
    return metrics_template.render(data_list=data_list)

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)