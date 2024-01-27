from setuptools import setup

setup(
    name="crime-town",
    py_modules=["crime_town"],
    install_requires=[
        "flake8==6.1.0",
        "isort==5.10.1",
        "black==23.7.0",
        "isort==5.10.1",
        "autopep8==1.6.0",
        "yamllint==1.32.0",
        "pylint==2.17.5",
        "mypy==1.5.0",
        "pre-commit==3.3.3",

        "uvicorn==0.23.2",
        "fastapi_versioning==0.10.0",
        "fastapi==0.101.0",
        "sqlalchemy==2.0.19",
        "pydantic==2.1.1",
        "pytest==7.4.0",
        "assertpy==1.1",
        "coloredlogs==15.0.1",
        "pandas==2.0.3",
        "cryptography==41.0.3",

        "pymysql==1.1.0",

        "mkdocs==1.5.2",

        "pyyaml==6.0.1",
        "omegaconf==2.1.1",
    ],
    extras_require=[],
)
