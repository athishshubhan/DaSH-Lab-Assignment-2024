import socket
import json
import sys

def send_prompt_to_server(prompt, client_id, server_host='localhost', server_port=9999):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_host, server_port))

        request = json.dumps({"Prompt": prompt})
        client.send(request.encode('utf-8'))

        response = client.recv(4096).decode('utf-8')
        response_data = json.loads(response)
        
        response_data['ClientID'] = client_id

        with open(f'client_{client_id}_output.json', 'a') as outfile:
            json.dump(response_data, outfile, indent=4)
            outfile.write('\n')  

        client.close()
    except Exception as e:
        print(f"Error: {str(e)}")

def process_input_file(file_path, client_id):
    try:
        with open(file_path, "r") as file:
            for line in file:
                prompt = line.strip()
                if not prompt:
                    continue
                send_prompt_to_server(prompt, client_id)
    except Exception as e:
        print(f"Error processing input file: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <input_file> <client_id>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    client_id = sys.argv[2]
    
    process_input_file(input_file_path, client_id)
