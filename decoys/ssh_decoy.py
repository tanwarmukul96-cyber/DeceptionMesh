import socket
import threading

from services.event_collector import collect_event


HOST = "0.0.0.0"
PORT = 2222


def handle_client(client, address):
    source_ip, source_port = address

    print(
        f"[DECOY] SSH connection from "
        f"{source_ip}:{source_port}"
    )

    collect_event(
        source_ip=source_ip,
        decoy="fake-ssh",
        action="connection_attempt",
        tool="ssh"
    )

    client.sendall(
        b"SSH-2.0-OpenSSH_8.9\r\n"
    )

    try:
        data = client.recv(4096)

        if data:
            collect_event(
                source_ip=source_ip,
                decoy="fake-ssh",
                action="identification_received",
                tool="ssh",
                interaction_depth=2,
                success=True
            )

    except Exception as error:
        print(f"[DECOY] Connection error: {error}")

    finally:
        client.close()


def start_decoy():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen(20)

    print(
        f"[DECOY] Fake SSH listening on port {PORT}"
    )

    while True:
        client, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client, address),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":
    start_decoy()