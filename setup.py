from setuptools import setup

setup(
    name="Flask_Template",
    packages=["Flask_Template"],
    include_package_data=True,
    install_requires=[
        "flask",
        "python-dotenv",
    ],
)

# Rename the application
# - Folders 
# - name in setup 
# - name in views 
# - name in __init__
# - name in -flaskenv
# Add requirements to the install_requires
# Then "pip install -e .
# flask --app name run