import StringIO

__author__ = 'Alexander Weigl'

from flask import Flask, request, render_template, Response
from flask.ext.restful import Api, Resource, representations

from hf3lint.base import lint, Entry


UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'xml'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

api = Api(app)

from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


representations.json.settings["cls"] = MyEncoder


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def format_result(result_dict, format="html"):
    if format == "json":  # automatically done by restful
        return "application/json", result_dict
    elif format == "html":
        return "text/html", render_template("results.html", results=result_dict)
    elif format == "csv":
        return "text/csv", render_template("results.csv", results=result_dict)
    else:
        return "application/json", result_dict


class CheckService(Resource):
    def get(self):
        print 404, "GET Method not supported"

    def post(self):
        format = request.values.get('format', "json")
        if len(request.files):
            result = {}
            for key in request.files:
                file = request.files['file']
                if allowed_file(file.filename):
                    try:
                        r = lint('auto', file.stream)
                        result[file.filename] = r
                    except BaseException as e:
                        result[file.filename] = [Entry("E", "Exception occured: %s" % e, "")]
                else:
                    result[file.filename] = [Entry("F", "Unallowed file type", "")]
            mime, out = format_result(result, format)
            return Response(out, mimetype=mime)
        else:
            return 400, "No valid file was sent"

    def put(self):
        format = request.values.get('format', "json")
        content = request.data
        result = {}
        if content:

            stream = StringIO.StringIO(content)
            try:
                r = lint('auto', stream)
                result["-"] = r
            except BaseException as e:
                result[file.filename] = [Entry("E", "Exception occured: %s" % e, "")]
        else:
            return 400, "No valid file was sent"

        mime, out = format_result(result, format)
        return Response(out, mimetype=mime)


api.add_resource(CheckService, "/check")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=6160, debug=True)