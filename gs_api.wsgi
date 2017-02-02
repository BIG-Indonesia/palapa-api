import sys
sys.path.append('/opt/gspalapa-api')

from gs_api_ws import app as application
if __name__ == '__main__':
    app.run(debug=True, port=5001, threaded=True, passthrough_errors=False)

