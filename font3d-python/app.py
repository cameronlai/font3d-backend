from flask import Flask, request, abort, send_file, make_response, jsonify
from subprocess import call
import os
from tempfile import NamedTemporaryFile

app = Flask(__name__)

@app.route('/generate', methods=['POST', 'OPTIONS'])
def main():
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        print(headers)
        return ('', 204, headers)

    # Load data from body
    if not request.json:
        abort(400)
    body = request.get_json()
    word = body["word"]

    print("here")
    font_dir = os.getcwd() + '/font3d-scad/'
    print(font_dir)
    tmpScad = NamedTemporaryFile(suffix='.scad')
    tmpScad.write('include <{0}font3d.scad>\n'.format(font_dir).encode())
    tmpScad.write('font3d("{0}", "basic");\n'.format(word).encode())

    # Generate STL file    
    tmpScad.seek(0)
    for line in tmpScad:
        print(line)
            
    tmpScad.seek(0)
    tmpStl = NamedTemporaryFile(suffix='.stl')
    cmd = 'openscad -o ' + tmpStl.name + ' ' + tmpScad.name
    call(cmd, shell=True)
    tmpScad.close()
        
    tmpStl.seek(0)

    response = make_response(send_file(tmpStl.name, as_attachment=True, attachment_filename='{0}.stl'.format(word)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
