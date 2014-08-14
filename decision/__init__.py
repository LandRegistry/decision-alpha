import os, logging
from flask import Flask
from raven.contrib.flask import Sentry

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))

app.logger.info("\nConfiguration\n%s\n" % app.config)

# Sentry exception reporting
if 'SENTRY_DSN' in os.environ:
    sentry = Sentry(app, dsn=os.environ['SENTRY_DSN'])

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

# Validate config 
for property_to_check in ['CASEWORK_URL', 'CHECK_URL']:
	if not app.config[property_to_check]:
		raise Exception('Missing %r configuation property.' % (property_to_check))
	