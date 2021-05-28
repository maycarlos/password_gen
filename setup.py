from setuptools import setup, find_packages

setup(
    name='pass_gen',
    version='0.1.0',
    description='Pequeno projeto para criar e guardar passwords',
    url='https://github.com/maycarlos/password_gen',
    author='maycarlos',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pyperclip',
        'alive_progress'
    ],
    entry_points={
        'console_scripts': [
            'pass_gen = pass_gen.pass_gen:menu'
        ]
    }
)