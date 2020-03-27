import sys
sys.path.append('/opt/gspalapa-api')

from gs_api_ws import app as application

if __name__ == "__main__":
    application.run()
