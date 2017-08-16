from paver.easy import *
from paver.setuputils import setup
import multiprocessing
import os


setup(
    name = "VPTests",
    version = "0.1.0",
    author = "Stagwell",
    author_email = "support@browserstack.com",
    description = ("Behave Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-browserstack",
    packages=['features']
)

def run_behave_test():
    sh('behave features/features/vptests.feature')

@task
@consume_nargs(0)
def run():
    """Run single, local and parallel test using different config."""
    for i in range(2):
        os.environ['TASK_ID'] = str(i)
        run_behave_test()

@task
def test():
    """Run all tests"""
    sh("paver run single")
    sh("paver run local")
    sh("paver run parallel")

