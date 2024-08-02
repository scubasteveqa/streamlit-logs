import streamlit as st
import logging
import sys

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Handler for stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(stdout_formatter)

# Handler for stderr
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)
stderr_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stderr_handler.setFormatter(stderr_formatter)

# Add handlers to the logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Streamlit app
st.title('Streamlit Logging Example')

# Log messages to stdout and stderr
logger.info('This is an info message logged to stdout')
logger.error('This is an error message logged to stderr')

st.write('Logged an info message to stdout.')
st.write('Logged an error message to stderr.')
st.write('Check the console for log messages.')
