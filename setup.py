from setuptools import setup

setup(
    name='pass_gen',
    version='0.1.0',
    py_modules=['pass_gen'],
    install_requires=[
        'Click',
        'pyperclip',
        'alive_progress'
    ],
    entry_points={
        'console_scripts': [
            'pass_gen = pass_gen:menu'
        ]
    }
)