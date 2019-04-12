from setuptools import setup, find_packages

setup(
    name='cabot-core',
    packages=find_packages(),
    version='0.1.2',
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
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
