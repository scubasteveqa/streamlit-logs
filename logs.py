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

# Streamlit app title
st.title('Streamlit Logging Example')

# Streamlit display for logs
st.write('### Logs:')

# Create an empty placeholder for log output
log_display = st.empty()

# Function to continually update and display the logs
def update_logs():
    while True:
        # Get the current log content from the log stream
        new_logs = log_stream.getvalue()

        # Update the displayed logs in the text area with the new logs
        log_display.text_area("Log Output", new_logs, height=300, key="log_output")
        
        # Pause for a second to simulate periodic log updates
        time.sleep(1)

# Test logging during setup and application runtime
logger.info("Starting application setup...")
logger.debug("Setting up environment...")
logger.error("Environment setup error: Something went wrong")

# Call the function to update the logs and display them continuously
if __name__ == '__main__':
    update_logs()
