from setuptools import setup

setup(
    name="Flask_Template",
    packages=["flaskr"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)

# Rename the application
# - Folders 
# - packages in setup 
# - name in views 
# - name in __init__
# - name in -flaskenv
# Add requirements to the install_requires
# Then "pip install -e .
# flask --app flaskr --debug run