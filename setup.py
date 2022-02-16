import setuptools

setuptools.setup(
    name="Femut",
    version="1.0.3",
    license='MIT',
    author="Chantore",
    author_email="wnrnrxla@gmail.com",
    description="It is a package that allows you to estimate the height of the owner of the femur using the femur.",
    keywords=['Archaeology', 'Physical-Anthropology'],
    url="https://github.com/ChanToRe/Femut",
    install_requires=['pandas', 'numpy'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)