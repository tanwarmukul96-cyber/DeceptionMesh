import socket
import time


TARGET_HOST = "127.0.0.1"
TARGET_PORT = 2222


def connect_to_ssh_decoy():
    print("[ATTACKER] Starting simulation...")
    print(f"[ATTACKER] Connecting to {TARGET_HOST}:{TARGET_PORT}")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)

    try:
        client.connect((TARGET_HOST, TARGET_PORT))

        banner = client.recv(1024).decode(errors="ignore")

        print(f"[ATTACKER] Received banner: {banner.strip()}")

        time.sleep(1)

        client.sendall(
            b"SSH-2.0-DeceptionMesh-TestClient\r\n"
        )

        print("[ATTACKER] Sent identification string")

    except Exception as error:
        print(f"[ATTACKER] Simulation error: {error}")

    finally:
        client.close()
        print("[ATTACKER] Simulation finished")


if __name__ == "__main__":
    connect_to_ssh_decoy()