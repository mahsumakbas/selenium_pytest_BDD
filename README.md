# selenium_pytest_BDD
It is a BDD(Behavior Driven Development) framework template to automate Web UI test through Selenium Webdriver library; written in Python, using pytest and pytest-bdd libraries

To install plugins: pip install -r requirements.txt

to run test, go to main folder and run pytest: 
pytest --html=reports/report.htm --reruns 2 -n 4

parametres: 
--html to produce execution result file 
--reruns number of retry in case of test failed 
-n number of parallel running threads

You can create your feature files under "features" folder.
You can create your step definitions under "step_defs" folder and you MUST import that files in "test_bdd_features.py" file.