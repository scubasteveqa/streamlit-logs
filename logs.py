import streamlit as st
import subprocess
import json

# Streamlit app title
st.title('DynamoDB Logs Viewer')

# Create a text input for the user to enter the content ID
content_id = st.text_input("Enter Content ID", "")

# Button to fetch logs from DynamoDB
if st.button("Fetch Logs"):

    # Validate if content_id is provided
    if content_id:
        try:
            # Run the AWS CLI command to query DynamoDB and get logs
            command = f"aws dynamodb query --table-name vivid-logs-staging-content-logs --key-condition-expression \"log_channel = :v1\" --expression-attribute-values '{{\":v1\":{{\"S\":\"{content_id}\"}}}}' | jq '.Items[]|[.log_level.S, .message.S]|@tsv' -rc"
            
            # Execute the command using subprocess
            result = subprocess.check_output(command, shell=True, text=True)
            
            # Display the result (logs) in the Streamlit app
            if result:
                logs = result.splitlines()  # Split the output into lines
                logs_display = "\n".join(logs)  # Join the logs with line breaks
                st.text_area("Log Output", logs_display, height=300)  # Display logs in a text area
            else:
                st.warning("No logs found for the provided content ID.")
        
        except subprocess.CalledProcessError as e:
            st.error(f"Error fetching logs: {e}")
    else:
        st.warning("Please enter a valid content ID.")
