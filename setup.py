import os
from setuptools import setup, find_packages
from io import open

# Module dependencies
requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(requirements_file, 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='propulsion-training-monitor',
    version='0.0.1',
    description='Get notified of the status of your training',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/propulsion-ai/propulsion-training-monitor',
    author='Propulsion',
    author_email='opensource@propulsionhq.com',
    license='Apache 2.0',
    packages=find_packages(),
        entry_points={
            'console_scripts': [
                'propulsion_training_monitor = propulsion_training_monitor.__main__:main'
            ]
    },
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=requirements_file
)
