from flask import Flask, render_template, render_template_string, request, jsonify
import notion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page', methods=('GET',))
def page():
    url = request.args.get('notion_url')
    data = notion.get_page(url)
    if data["status"] == "success":
        return render_template_string(data["result"])
    else:
        return render_template("page.html")

@app.route('/deploy', methods=('POST',))
def deploy():
    res = request.json
    data = notion.deploy_page(res["notion_url"])
    if data["status"] == "success":
        print("deployed")
        return jsonify({ "status": 200, "result": data["result"] })
    else:
        print("deploy fail")
        return jsonify({ "status": 503, "result": data["result"] })
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)