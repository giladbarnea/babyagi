def requirements_to_setup(requirements_path):
    with open(requirements_path, 'r') as f:
        requirements = f.readlines()
    
    # Remove newlines
    requirements = [req.strip() for req in requirements if req.strip()]

    setup_content = f"""
from setuptools import setup, find_packages

setup(
    name='babyagi',
    version='0.1.0',
    packages=find_packages(),
    install_requires={requirements}
)
"""
    with open("setup.py", 'w') as f:
        f.write(setup_content)

    print("Generated setup.py!")

# Example usage:
requirements_to_setup('requirements.txt')
