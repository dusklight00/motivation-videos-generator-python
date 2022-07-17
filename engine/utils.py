import os
import shutil
import requests
import uuid

def downlaod_file(url, output_file_path):
    response = requests.get(url)
    with open(output_file_path, "wb") as f:
        f.write(response.content)

def download_file_to_temp(url, output_temp_path):
    output_file_path = os.path.join("temp", output_temp_path)
    downlaod_file(url, output_file_path)

def download_file_to_temp_dir(url, temp_dir_path, output_filename):
    output_file_path = os.path.join("temp", temp_dir_path, output_filename)
    downlaod_file(url, output_file_path)

def create_temp_dir(dir_name):
    temp_dir_path = os.path.join("temp", dir_name)
    os.makedirs(temp_dir_path, exist_ok=True)
    return temp_dir_path

def delete_temp_dir(dir_name):
    temp_dir_path = os.path.join("temp", dir_name)
    if os.path.exists(temp_dir_path):
        shutil.rmtree(temp_dir_path)
        return True
    return False

def create_unique_id():
    return str(uuid.uuid4())

