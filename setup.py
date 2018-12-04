import setuptools

setuptools.setup(
    name='ncs_face_detection',
    scripts=['ncs_face'],
    version='0.1.3',
    license="licenses.txt",
    author="Tuan LM",
    author_email="tuanlm@greenglobal.vn",
    description="Movidius Video Object Scalable",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gg-tuanlm/python_packaging_demo",
    include_package_data=True,
    packages=setuptools.find_packages(),
    data_files=[
    	("/ncs_face_detection/graphs", ["graphs/ssd-face.graph"]),
    ],
    install_requires=[
        "numpy",
        "mvnc"
    ],
    classifiers=[
        "Programming Language:: Python :: 3"
        "License :: OSI Approved :: MIT License",
        "Operating system :: OS Independent",
    ],
)
