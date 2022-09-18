from setuptools import setup

setup(
    name="Flask_Template",
    packages=["flaskr"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)

# Add requirements to the install_requires
# Then "pip install -e .
# flask --app flaskr --debug run
# access to config variables: app.config["name"]
