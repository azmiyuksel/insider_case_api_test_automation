# API automation case for Insider

This repo is created for API automation for Insider. It includes Pet API CRUD tests. Endpoint: https://petstore.swagger.io/
This repo can be cloned using following command:

```bash
git clone https://github.com/azmiyuksel/insider_case_api_test_automation.git
```

## Installing Dependencies

After cloning the repo, related directory should be opened and dependencies should be installed with following command (Virtual environment can be used):

```bash
cd insider_case_api_test_automation
pip install -r requirements.txt
```

## Executing Tests

Tests can be executed  with following command:

```bash
pytest --alluredir=report --clean-alluredir
```

Test Report can be displayed with following command:

```bash
allure serve report
```

*pytest.log* file is created after test run to view run records.
