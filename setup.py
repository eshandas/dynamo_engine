from distutils.core import setup


setup(
    name='dynamo_engine',
    packages=['dynamo_engine'],  # this must be the same as the name above
    version='0.1',
    description='An ORM for Amazon\'s DynamoDB',
    author='Eshan Das',
    author_email='eshandasnit@gmail.com',
    url='https://github.com/eshandas/dynamo_engine',  # use the URL to the github repo
    download_url='https://github.com/eshandas/dynamo_engine/archive/0.1.tar.gz',  # I'll explain this in a second
    keywords=['dynamo', 'dynamodb', 'aws', 'orm'],  # arbitrary keywords
    classifiers=[],
)
