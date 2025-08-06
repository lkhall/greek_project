# Hansen and Quinn Study Software
## About
This project was created by Lauren Hall (Williams College '27), advised by Professor Olsen, through the Class of 1957 Summer Research Program for Divisions I & II. It was created in response to a lack of online study tools corresponding to CLGR 101/102, which uses the textbook "Greek: An Intensive Course" by Hardy Hansen and Gerald M. Quinn. Memorizing verb conjugation and noun and adjective declension consitutues much of the early learning stages of Ancient Greek, so this application focuses mainly on repetition and exposure to those forms.

## Running the software locally
Clone the repository
```
git clone https://github.com/lkhall/greek_project.git
```

Activate the virtual environment
```
cd greek_project
source .venv/bin/activate
```

Install the dependencies
```
pip install -r greekproj/requirements.txt
```

Set debug=True in greekproj/settings.py on line 29
```
debug=True
```

In greekproj/first_app/views.py, replace each reference to a json file with its path on your machine
For example, replace
```
with open('first_app/noun_data.json') as f:
```
on line 207 with 
```
with open('/Users/lauren/gp_testing/greek_project/greekproj/first_app/noun_data.json') as f:
```

Activate the venv again, run the server, and go to the link provided
```
source .venv/bin/activate
python3 greekproj/manage.py runserver
```
