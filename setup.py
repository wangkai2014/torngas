from setuptools import setup, find_packages
setup(
    name="torngas",
    version="0.2.4",
    description="torngas based on tornado",
    author="qingyun meng",
    url="http://github.com/mqingyn/torngas",
    license="LGPL",
    packages= find_packages(),
    package_data={'torngas': ['resource/app/*.*',
                              'resource/app/settings/*.*',
                              'resource/app/Main/*.*',
                              'resource/app/Main/models/*.*',
                              'resource/app/templates/*.*',
                              'resource/app/Main/views/*.*',
                              'resource/exception.html',
                              'scripts/create_torngas.py']},
    author_email = "maingyn@gmail.com",
    requires=['Tornado','futures'],
    scripts=["torngas/scripts/create_torngas.py"],
    )
