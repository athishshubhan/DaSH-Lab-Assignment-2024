import socket
import json
import google.generativeai as genai
import time

api_key = "AIzaSyB-qE6V29e4fqngFM49AjJzcz3-mypjzzA"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def handle_client_connection(client_socket):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            prompt = json.loads(request)
            start_time = time.time()
            try:
                response = model.generate_content(prompt['Prompt'])
                response_text = response.text if response else "No response"
            except Exception as e:
                response_text = f"Error: {str(e)}"
            end_time = time.time()

            response = {
                "Prompt": prompt['Prompt'],
                "Message": response_text.strip(),
                "TimeSent": int(start_time),
                "TimeRecvd": int(end_time),
                "Source": "Gemini"
            }
            
            client_socket.send(json.dumps(response).encode('utf-8'))
    except Exception as e:
        print(f"Error handling client connection: {str(e)}")
    finally:
        client_socket.close()

def start_server(host='localhost', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            client_socket, addr = server.accept()
            handle_client_connection(client_socket)
        except Exception as e:
            print(f"Error accepting connection: {str(e)}")

if __name__ == "__main__":
    start_server()
