import os
from pyrogram import Client

# Function to generate the session string
def export_session_string():
    # Get API ID
    API_ID = "25177081"

    # Get API Hash
    API_HASH = "3864b3bf9d7898981e271e7932c436ac"

    # Get phone number
    PHONE_NUMBER = "+85577967351"

    SESSION_STRING = "my_session"

    try:
        app = Client(
            name=SESSION_STRING,
            api_id=API_ID, 
            api_hash=API_HASH, 
            phone_number=PHONE_NUMBER
            )

        with app:
            session_string = app.export_session_string()
            print("Session string generated successfully!\n")
            print("Your session string is:\n")
            print(session_string)

            # Define the session file path
        session_file = f"{SESSION_STRING}.session"
        
        # Check if the session file exists and delete it
        if os.path.exists(session_file):
            os.remove(session_file)
            print(f"\nSession file '{session_file}' has been deleted.")
        else:
            print(f"\nSession file '{session_file}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
if __name__ == "__main__":
    export_session_string()