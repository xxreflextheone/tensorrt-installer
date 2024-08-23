# Steps based on the Nvidia documentation
#pip install cuda-python
#cuda toolkit 12.5: https://developer.download.nvidia.com/compute/cuda/12.5.0/local_installers/cuda_12.5.0_555.85_windows.exe
#python3 -m pip install --upgrade pip
#python3 -m pip install wheel
#python3 -m pip install --upgrade tensorrt

import os
import subprocess
import time
import os.path

restart = False

try:
    import cuda
except:
    print('Installing cuda-python module')
    os.system('pip install cuda-python')
    restart = True

try:
    import requests
except:
    print('Installing requests module')
    os.system('pip install requests')
    restart = True

try:
    from tqdm import tqdm
except:
    os.system('pip install tqdm')
    restart = True

if restart:
    os.system('py install.py')
    print('restarting...')
    quit()

def installCudaToolkit():
    print('Downloading Cuda Toolkit...')
    f = open("output.txt", "w")
    download_link = 'https://developer.download.nvidia.com/compute/cuda/12.5.0/local_installers/cuda_12.5.0_555.85_windows.exe'
    file_path = "cuda_12.5.0_555.85_windows.exe"

    
    response = requests.get(download_link, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            if chunk:
                file.write(chunk)
                
    progress_bar.close()

    print(f'Cuda Toolkit downloaded. Attempting to install..')
    f.write('Cuda Tooklkit downloaded')

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("Error downloading file.")
        return
    

    try:
        subprocess.run([file_path, '/silent', '/noreboot'], check=True)
        print('Cuda Toolkit installed')
        f.write('Cuda Toolkit installed successfully')

        restart = True
    except subprocess.CalledProcessError as e:
        print(f'Failed to install Cuda Toolkit due to: {e}')
        f.write('Cuda Toolkit installed successfully')

if not os.path.exists('output.txt'):
    installCudaToolkit()

if restart:
    os.system('py install.py')
    print('restarting...')
    quit()

try:
    print('Updating pip...')
    os.system('python -m pip install --upgrade pip')
except:
    print('Failed to upgrade pip')

try:
    print('Installing Python wheel...')
    os.system('python -m pip install wheel')
except:
    print('Failed to install Python wheel')

try:
    print('Installing TensorRT Python wheel...')
    os.system('python -m pip install --upgrade tensorrt')
except:
    print('Failed to install TensorRT Python wheel')

try:
    print('Installing TensorRT')
    os.system('pip install tensorrt')
except:
    print('Failed to install TensorRT')


print('done!')
time.sleep(5)
quit()
