from flask import Flask, render_template, render_template_string, request
import notion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page', methods=('GET', 'POST'))
def page():
    url = request.args.get('notion_url')
    data = notion.get_page(url)
    return render_template_string(data["html"])

if __name__=="__main__":
    # app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="5000", debug=True)