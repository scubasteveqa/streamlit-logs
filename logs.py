import streamlit as st
import logging
import sys
import io

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a stream to capture log output in memory
log_stream = io.StringIO()

# Handler for stdout (logs info and debug messages)
stdout_handler = logging.StreamHandler(log_stream)
stdout_handler.setLevel(logging.DEBUG)
stdout_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(stdout_formatter)

# Handler for stderr (logs error messages)
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

# Display the captured logs in the Streamlit app
st.write('### Logs:')
st.text(log_stream.getvalue())  # Display the logs from the in-memory stream

# Optionally, you can also show the original messages in the console
st.write('Logged an info message to stdout.')
st.write('Logged an error message to stderr.')
