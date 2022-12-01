import os
import subprocess


# Check if it's running on Windows
if os.name == 'nt':
    out = os.path.dirname(os.path.realpath('run_all_tests.py'))

    print("Testing model: accounts.py")
    subprocess.run(['cmd', '/c', 'pytest', out + '/unit/test_model_accounts.py'])
    print("Testing model: products.py")
    subprocess.run(['cmd', '/c', 'pytest', out + '/unit/test_model_products.py'])
    print("Testing resource: accounts.py")
    subprocess.run(['cmd', '/c', 'pytest', out + '/functional/test_accounts.py'])
    print("Testing resource: products.py")
    subprocess.run(['cmd', '/c', 'pytest', out + '/functional/test_products.py'])
    print("Testing resource: session.py")
    subprocess.run(['cmd', '/c', 'pytest', out + '/functional/test_session.py'])

else:
    out = os.path.dirname(os.path.realpath('run_all_tests.py'))

    print("Testing model: accounts.py")
    subprocess.run(['pytest', out + '/unit/test_model_accounts.py'])
    print("Testing model: products.py")
    subprocess.run(['pytest', out + '/unit/test_model_products.py'])
    print("Testing resource: accounts.py")
    subprocess.run(['pytest', out + '/functional/test_accounts.py'])
    print("Testing resource: products.py")
    subprocess.run(['pytest', out + '/functional/test_products.py'])
    print("Testing resource: session.py")
    subprocess.run(['pytest', out + '/functional/test_session.py'])