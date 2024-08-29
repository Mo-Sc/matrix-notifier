import subprocess
import os
import argparse


def notify(message, credentials_file="config/credentials.json"):
    """
    Send a message to the matrix room without using async function
    """

    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.path.join("src", "matrix_message.py"),
    )
    subprocess.run(["python", script_path, message, credentials_file], check=True)


def main():

    parser = argparse.ArgumentParser(description="Matrix Message Notifier")
    parser.add_argument("message", type=str, help="the message to send")
    parser.add_argument(
        "--config",
        type=str,
        default=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config/credentials.json"
        ),
        help="path to the config json file",
    )

    args = parser.parse_args()

    message = args.message
    credentials_file = args.config

    notify(message, credentials_file)


if __name__ == "__main__":
    main()
