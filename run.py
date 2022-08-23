import os
import pytest


if __name__ == '__main__':
    pytest.main()
    os.system('allure generate C:\\PycharmProjects\\realization\\report\\temp -o '
              'C:\\PycharmProjects\\realization\\report\\html --clean')
    os.system("allure open report/html -p 7778")
    
