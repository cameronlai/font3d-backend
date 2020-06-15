from flask import send_file
from subprocess import call
import os

from flask import Flask
from flask import request
from tempfile import NamedTemporaryFile
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def http():
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

    return send_file(tmpStl, as_attachment=True, attachment_filename='{0}.stl'.format(word))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
