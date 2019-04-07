from setuptools import setup

setup(
    name='caBot',
    packages=['cabot'],
    version='0.1.0',
    license='MIT',
    description='A modular chat bot.',
    author='Joseph Hanna',
    author_email='josephhanna@centennialarts.com',
    url='https://github.com/centennialarts/cabot',
    download_url='https://github.com/centennialarts/cabot/archive/master.zip',
    keywords=['Chatbot', 'IRC', 'API'],
    install_requires=[
        'irc',
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
