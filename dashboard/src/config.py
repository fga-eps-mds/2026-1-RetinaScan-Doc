import os

REPO_BASE_NAME = 'fga-eps-mds-2026-1-RetinaScan-'
REPOS_LANGUAGE = {
    'Web': 'ts',
    'Api': 'py',
}

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(os.path.dirname(_CURRENT_DIR))

SONAR_FILES_PATH = os.path.join(_REPO_ROOT, 'analytics', 'raw-data', 'fga-eps-mds-*.json')
ISSUES_FILES_PATH = os.path.join(_REPO_ROOT, 'analytics', 'raw-data', 'GitHub_API-Issues-*.json')

SONAR_METRIC_LIST = [
    'files', 'functions', 'complexity', 'comment_lines_density', 
    'duplicated_lines_density', 'coverage', 'ncloc', 'tests', 
    'test_errors', 'test_failures', 'test_execution_time', 'security_rating'
]

WEIGHT_PSC1, WEIGHT_PSC2 = 1, 1
WEIGHT_PC1, WEIGHT_PC2 = 0.5, 0.5
WEIGHT_CODE_QUALITY = [0.33, 0.33, 0.33]   
WEIGHT_TESTING_STATUS = [0.25, 0.25, 0.50] 
