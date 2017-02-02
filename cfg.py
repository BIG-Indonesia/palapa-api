APP_BASE = "/opt/gspalapa-api/"
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'PALAPA_ini_PALAPA_ini_PALAPA_ini_PALAPA'
WTF_CSRF_ENABLED = False
SECURITY_TOKEN_MAX_AGE = 365 * 24 * 60 * 60 * 1000
SECRET_KEY = 'PALAPA ini PALAPA ini PALAPA ini PALAPA'
SQLALCHEMY_DATABASE_URI = 'postgres://palapa:palapa@palapa.agrisoft-cb.com/palapa'
SQLALCHEMY_BINDS = {
    'dbdev': 'postgres://palapa:palapa@palapa.agrisoft-cb.com/palapa_dev',
    'dbprod': 'postgres://palapa:palapa@palapa.agrisoft-cb.com/palapa_prod',
    'dbpub': 'postgres://palapa:palapa@palapa.agrisoft-cb.com/palapa_pub',
    'services': 'postgres://palapa:palapa@palapa.agrisoft-cb.com/palapa'
}
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATASTORE = 'postgres://palapa:palapa@palapa.agrisoft-cb.com/'
GEOSERVER_REST_URL = 'http://palapa.agrisoft-cb.com:8080/geoserver/rest/'
GEOSERVER_WMS_URL = 'http://palapa.agrisoft-cb.com:8080/geoserver/wms?'
GEOSERVER_WFS_URL = 'http://palapa.agrisoft-cb.com:8080/geoserver/wfs?'
GEOSERVER_WMS_OUT = 'http://palapa.agrisoft-cb.com:8080/geoserver/wms?'
GEOSERVER_WFS_OUT = 'http://palapa.agrisoft-cb.com:8080/geoserver/wfs?'
GEOSERVER_USER = 'palapa'
GEOSERVER_PASS = 'palapa'
GEOSERVER_THUMBNAILS = '/var/www/html/assets/thumbnails/'
GEOSERVER_DATA_DIR = '/var/lib/tomcat/webapps/geoserver/data/'
GEOSERVER_LAYERS_PROP = '/var/lib/tomcat/webapps/geoserver/data/security/layers.properties'
GEOSERVER_SERVICES_PROP = '/var/lib/tomcat/webapps/geoserver/data/security/services.properties'
DATASTORE_HOST = 'palapa.agrisoft-cb.com'
DATASTORE_PORT = '5432'
DATASTORE_USER = 'palapa'
DATASTORE_PASS = 'palapa'
DATASTORE_DB = 'palapa'
UPLOAD_FOLDER = '/mnt/uploads/'
RASTER_FOLDER = '/mnt/data/'
RASTER_STORE = '/mnt/store/'
DOCUMENTS_FOLDER = '/mnt/docs/'
DOWNLOADS_FOLDER = '/mnt/downloads/'
ALLOWED_EXTENSIONS = set(['zip', 'ZIP'])
ALLOWED_VECTOR = set(['shp', 'SHP'])
ALLOWED_RASTER = set(['tiff', 'tif', 'TIF', 'TIFF'])
CSW_URL = 'http://palapa.agrisoft-cb.com/csw'
PALAPA_FOLDER = '/var/www/html/palapa/'