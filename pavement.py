from paver.easy import *
from paver.setuputils import setup
import multiprocessing

setup(
    name = "VictoryPassport",
    version = "0.1.0",
    author = "Stagwell",
    author_email = "sumit@stagwell.tech",
    description = ("VP Automated Tests"),
    license = "Stagwell",
    url = "https://give.int.victorypassport.com/stripeaan/one-payout/",
    packages=['features']
)

def run_behave_test(config, feature, task_id=0):
    sh('CONFIG_FILE=config/%s.json TASK_ID=%s behave features/%s.feature' % (config, task_id, feature))

@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    if args[0] in ('single', 'local'):
        run_behave_test(args[0], args[0])
    else:
        jobs = []
        for i in range(4):
            p = multiprocessing.Process(target=run_behave_test, args=(args[0], "single", i))
            jobs.append(p)
            p.start()

@task
def test():
    """Run all tests"""
    sh("paver run single")
    sh("paver run local")
    sh("paver run parallel")
