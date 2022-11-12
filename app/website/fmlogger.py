# Python3 module for logging HTTP requests and responses, as well as as ForwardMetric web application actions
# CODEOWNER: DavidHoenisch

import logging
import configparser
import os
import sys

# log file paths
application_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'application.log')
http_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'http.log')

# log file handlers
application_log_handler = logging.FileHandler(application_log)
http_log_handler = logging.FileHandler(http_log)

# log file formatters
application_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configure Logging
application_log_handler.setFormatter(application_log_formatter)
http_log_handler.setFormatter(application_log_formatter)


# Application Logging
def log_application_action(action):
    application_logger = logging.getLogger('application')
    application_logger.addHandler(application_log_handler)
    application_logger.setLevel(logging.INFO)

# HTTP Logging
def log_http_request(request):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('REQUEST: %s', request)

def log_http_response(response):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('RESPONSE: %s', response)

def log_http_error(error):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('ERROR: %s', error)

def log_http_exception(exception):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('EXCEPTION: %s', exception)

def log_http_redirect(redirect):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('REDIRECT: %s', redirect)

def log_http_stream(stream):
    http_logger = logging.getLogger('http')
    http_logger.addHandler(http_log_handler)
    http_logger.setLevel(logging.INFO)
    http_logger.info('STREAM: %s', stream)
