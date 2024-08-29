import json
import asyncio
import os
import sys

from nio import AsyncClient
from bs4 import BeautifulSoup


async def __send_message_to_room(
    matrix_server, user_id, room_id, message_content, token=None, password=None
) -> None:
    try:
        client = AsyncClient(matrix_server, user_id)

        # login via token or password
        if token:
            client.access_token = token
        elif password:
            await client.login(password)
        else:
            raise ValueError("No password or token provided")

        # supports html formatted messages
        response = await client.room_send(
            room_id=room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "format": "org.matrix.custom.html",
                "body": BeautifulSoup(message_content, "html.parser").get_text(),
                "formatted_body": message_content,
            },
        )

        await client.close()

        if response.transport_response.status != 200:
            raise Exception(
                f"Sending message to room failed ({response.status_code}): {response.message}"
            )

    except Exception as e:
        # dont throw exception to not interrupt training
        print(f"Matrix Notification failed: {e}")
        return

    print("Message sent successfully")


async def main():

    message = sys.argv[1]
    credentials_file = sys.argv[2]

    if not os.path.isfile(credentials_file):
        print(f"Error: Credentials file {credentials_file} does not exist")
        return

    with open(credentials_file) as f:
        credentials = json.load(f)

    # Extract credentials (see README for more information)
    matrix_server = credentials["matrix_server"]
    user_id = credentials["user_id"]
    password = credentials["password"]
    access_token = credentials["access_token"]
    room_id = credentials["room_id"]

    await __send_message_to_room(
        matrix_server, user_id, room_id, message, token=access_token, password=password
    )


asyncio.run(main())
