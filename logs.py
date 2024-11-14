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

# Create a text input for the user to add custom log messages
log_input = st.text_area("Enter log message", "", height=100)

# Button to log the message entered by the user
if st.button("Log Message"):
    if log_input:
        logger.info(log_input)  # Log the input message as an info message
        st.success("Message logged successfully!")
    else:
        st.warning("Please enter a log message.")

# Function to continually update and display the logs
def update_logs():
    # Initially, capture the logs and display them in the text_area
    new_logs = log_stream.getvalue()  # Read the current log content
    log_display.text_area("Log Output", new_logs, height=300, key="log_output")  # Set unique key
    
    # Continuously capture and update logs every second
    while True:
        time.sleep(1)  # Update the log every second
        new_logs = log_stream.getvalue()  # Get the current log content
        log_display.text_area("Log Output", new_logs, height=300, key=f"log_output_{time.time()}")  # Update the logs

# Call the function to update the logs
if __name__ == '__main__':
    update_logs()
