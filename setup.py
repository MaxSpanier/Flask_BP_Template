from setuptools import setup

setup(
    name="Flask_Template",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask",
        "Flask-WTF",
    ],
)

# Add requirements to the install_requires
# Then "pip install -e .
# flask --app flaskr --debug run
# access to config variables: app.config["name"]

# set the environment variables with: (Windows is set instead of export)
# export SECRET_KEY="your secret key"
# export DATABASE_URI="postgresql://username:password@host:port/database_name"

