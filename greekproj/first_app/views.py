from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.forms import CheckboxSelectMultiple
#import requests
import json
import random
from json import dumps
# Create your views here.

noun_choices = (
	("τέχνη", "τέχνη"),
	("λόγος", "λόγος"),
	("ἔργον", "ἔργον"),
	("θάλλατα", "θάλλατα"),
	("πολίτης", "πολίτης"),
	("φύλαξ", "φύλαξ"),
	("αἴξ", "αἴξ"),
	("ἐλπίς", "ἐλπίς"),
	("χάρις", "χάρις"),
	("σῶμα", "σῶμα"),
	("μήτηρ", "μήτηρ"),
	("ἀνήρ", "ἀνήρ"),
	("γένος", "γένος"),
	("Σωκράτης", "Σωκράτης"),
	("πόλις", "πόλις"),
	("βασιλεύς", "βασιλεύς"),
	("νοῦς", "νοῦς"),
	("ἄστυ", "ἄστυ"),
)

noun_gender_choices = (
	('masc', 'Masculine'),
	('fem', 'Feminine'),
	('neut', 'Neuter'),
)

noun_case_choices = (
	('nom', 'Nominative'),
	('gen', 'Genitive'),
	('dat', 'Dative'),
	('acc', 'Accusative'),
	('voc', 'Vocative'),
)

noun_number_choices = (
	('singular', 'Singular'),
	('plural', 'Plural'),
)

noun_unit_choices = (
	("unit_1", "Unit 1"),
	("unit_4", "Unit 4"),
	("unit_6", "Unit 6"),
	("unit_10", "Unit 10"),
	("unit_20", "Unit 20"),
)

all_units = ["unit_1", "unit_4", "unit_6", "unit_10", "unit_20"]
all_nouns = ["τέχνη", "λόγος", "ἔργον", "θάλλατα","πολίτης","φύλαξ","αἴξ","ἐλπίς","χάρις","σῶμα","μήτηρ","ἀνήρ","γένος","Σωκράτης","πόλις","βασιλεύς","νοῦς","ἄστυ"]

verb_tense_choices = (
	("present", "Present"),
	("future", "Future"),
	("imperfect", "Imperfect"),
	("aorist", "Aorist"),
	("perfect", "Perfect"),
	("pluperfect", "Pluperfect"),
)

verb_mood_choices = (
	("indic", "Indicative"),
	("subj", "Subjunctive"),
	("opt", "Optative"),
	("imper", "Imperative"),
	("infin", "Infinitive"),
)

verb_voice_choices = (
	("act", "Active"),
	("mid", "Middle"),
	("pass", "Passive"),
)

verb_choices = (
	("παιδεύω", "παιδεύω"),
)
units_available = []
nouns_available = []

on_units = True

class NounForm(forms.Form):
	noun_gender = forms.MultipleChoiceField(choices=noun_gender_choices, label="Gender", widget=forms.CheckboxSelectMultiple)
	noun_case = forms.MultipleChoiceField(choices=noun_case_choices, label="Case", widget=forms.CheckboxSelectMultiple)
	noun_number = forms.MultipleChoiceField(choices=noun_number_choices, label="Number", widget=forms.CheckboxSelectMultiple)

class unit_form(forms.Form):
	selected_items = forms.MultipleChoiceField(
		choices=noun_unit_choices,
		widget=forms.SelectMultiple,
		label="Select Units:")

class select_noun_form(forms.Form):
	selected_nouns = forms.MultipleChoiceField(
		choices=noun_choices,
		widget=forms.SelectMultiple,
		label="Select Nouns:")

class VerbForm(forms.Form):
	verb_choice = forms.MultipleChoiceField(choices=verb_choices, label="Verb", widget=forms.SelectMultiple)
	verb_tense = forms.MultipleChoiceField(choices=verb_tense_choices, label="Tense", widget=forms.SelectMultiple)
	verb_voice = forms.MultipleChoiceField(choices=verb_voice_choices, label="Voice", widget=forms.SelectMultiple)
	verb_mood = forms.MultipleChoiceField(choices=verb_mood_choices, label="Mood", widget=forms.SelectMultiple)

def get_random_noun(units_available):
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
		print(units_available)
		response = json.load(f)
		if (units_available == []):
			units_available = all_units
		selected_unit = random.choice(units_available)
		print("selected unit: ", selected_unit)
		data = response[selected_unit]['nouns']
		num_nouns = len(data)

		random_int = random.randint(0, num_nouns-1)
		data = data[random_int]

		# use random number to get random noun
		first_key = next(iter(data))
		first_value = data[first_key]
		forms = first_value["forms"]
		# get random thing in noun by generating random int between 0 and 9
		# retrieve its data 
		random_int = random.randint(0, len(forms)-1)
		selected_form = forms[random_int]
		verb_form = next(iter(selected_form))
		verb_data = selected_form[verb_form]
		print(verb_data)
		return verb_form, first_value["gender"], verb_data["case"], verb_data["number"]

def get_random_noun2(nouns_available):
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
		print(nouns_available)
		# select random unit
		# select random noun
		# check if noun is in the nouns available
		response = json.load(f)
		if (nouns_available == []):
			nouns_available = all_nouns
		selected_unit = random.choice(all_units)
		print("selected unit: ", selected_unit)
		data = response[selected_unit]['nouns']
		num_nouns = len(data)
		# selecting random noun within a unit
		random_int = random.randint(0, num_nouns-1)
		data = data[random_int]

		# use random number to get random noun
		first_key = next(iter(data))
		first_value = data[first_key]
		forms = first_value["forms"]
		while first_key not in nouns_available:
			selected_unit = random.choice(all_units)
			print("selected noun: ", first_key)
			print("nouns avail: ", nouns_available)
			data = response[selected_unit]['nouns']
			num_nouns = len(data)
			# selecting random noun within a unit
			random_int = random.randint(0, num_nouns-1)
			data = data[random_int]
			first_key = next(iter(data))
			first_value = data[first_key]
			forms = first_value["forms"]

		# use random number to get random noun
		first_key = next(iter(data))
		first_value = data[first_key]
		forms = first_value["forms"]
		# get random thing in noun by generating random int between 0 and 9
		# retrieve its data 
		random_int = random.randint(0, len(forms)-1)
		selected_form = forms[random_int]
		verb_form = next(iter(selected_form))
		verb_data = selected_form[verb_form]
		print(verb_data)
		return verb_form, first_value["gender"], verb_data["case"], verb_data["number"]


def nouns(request):
	# if the user submitted a form

	# if request.method == "POST":
	# 	form = NounForm(request.POST)
	# 	if form.is_valid():
	# 		noun_gender = form.cleaned_data["noun_gender"]
	# 		noun_case = form.cleaned_data["noun_case"]
	# 		noun_number = form.cleaned_data["noun_number"]

	# 	else:
	# 		return render(request, "first_app/nouns.html", {
	# 			"form": form
	# 			})
	# get random noun form from API
	print("hello")
	if request.method == "POST":
		if 'submit_form' in request.POST:
			if request.POST['submit_form'] == 'submitting_units':
				global on_units
				on_units = True
				form = unit_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_items']
					print("selected:", selected)
					global units_available
					if units_available == []:
						units_available = all_units
					units_available = selected
				verb_form, gender, case, number = get_random_noun(units_available)
				return render(request, "first_app/nouns.html", {
					"form": NounForm(),
					"verb_form" : verb_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": unit_form(),
					"noun_form": select_noun_form()
					})
			elif request.POST['submit_form'] == 'submitting_nouns':
				on_units = False
				form = select_noun_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_nouns']
					print("selected:", selected)
					global nouns_available
					if nouns_available == []:
						nouns_available = all_nouns
					nouns_available = selected
				verb_form, gender, case, number = get_random_noun2(nouns_available)
				return render(request, "first_app/nouns.html", {
					"form": NounForm(),
					"verb_form" : verb_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": unit_form(),
					"noun_form": select_noun_form()
					})
	# embed noun form
	# embed its information
	else:
		print("hello")
		#global units_available
		if units_available == []:
			units_available = all_units
		if nouns_available == []:
			nouns_available = all_nouns
		if on_units == True:
			verb_form, gender, case, number = get_random_noun(units_available)
		else:
			verb_form, gender, case, number = get_random_noun2(nouns_available)
		print(gender)
		print(case)
		print(number)
		return render(request, "first_app/nouns.html", {
			"form": NounForm(),
			"verb_form" : verb_form,
			"gender": gender,
			"case": case,
			"number": number,
			"unit_form": unit_form(),
			"noun_form": select_noun_form()
			})

#def get_random_verb_form():


	# if the method is post, check the form
def verbs(request):
	if request.method == "POST":
		form = VerbForm(request.POST)
		print(form)
		if form.is_valid():
			selected_verb = form.cleaned_data['verb_choice']
			selected_tense = form.cleaned_data['verb_tense']
			selected_voice = form.cleaned_data['verb_voice']
			selected_mood = form.cleaned_data['verb_mood']
			print("selected:", selected_verb)
			print("selected tense :", selected_tense)
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/verb_data.json') as f:
		#verb_data = dumps(f)
		return render(request, "first_app/verbs.html", {
			"form": VerbForm(), "verb_data": f
			})

def adjectives(request):
	return render(request, "first_app/adjectives.html")

def participles(request):
	return render(request, "first_app/participles.html")

def index(request):
	return render(request, "first_app/index.html")
