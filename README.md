# Hansen and Quinn Study Software
## About
This project was created by Lauren Hall '27, advised by Professor Olsen, in response to a lack of online study tools corresponding to Williams College's Introductory Greek classes (CLGR 101/102). Memorizing conjugations and declensions consitutues much of the early Ancient Greek learning stages, so this application focuses mainly on repetitive identification of these grammatical forms. Its content is tailored to the vocabulary and units of CLGR 101/102's primary textbook: *Greek: An Intensive Course* by Hardy Hansen and Gerald M. Quinn.

Please contact Lauren Hall (lkh3@williams.edu), Sarah Olsen (seo1@williams.edu), or the current professor of CLGR 101/102 if you see any errors.

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
