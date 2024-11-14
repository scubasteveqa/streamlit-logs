import streamlit as st
import logging
import sys
import io
import time

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

# Streamlit display for logs
st.write('### Logs:')

# Create a text area widget to display the entire log content
log_display = st.text_area("Log Output", "", height=300)

# Function to continually update and display the logs
def update_logs():
    while True:
        time.sleep(1)  # Update the log every second
        new_logs = log_stream.getvalue()  # Read the current log content
        log_display = st.text_area("Log Output", new_logs, height=300)  # Update the displayed log

# Call the function to update the logs (ensure this part doesn't block the UI)
if __name__ == '__main__':
    update_logs()
