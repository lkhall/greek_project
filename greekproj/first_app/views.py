from django.http import HttpResponse
from django.shortcuts import render
from django import forms
#import requests
import json
import random
# Create your views here.

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
	("unit_10", "Unit 10"),
	("unit_20", "Unit 20"),
)

units_available = []

class NounForm(forms.Form):
	noun_gender = forms.ChoiceField(choices=noun_gender_choices, label="Gender")
	noun_case = forms.ChoiceField(choices=noun_case_choices, label="Case")
	noun_number = forms.ChoiceField(choices=noun_number_choices, label="Number")

class unit_form(forms.Form):
	selected_items = forms.MultipleChoiceField(
		choices=noun_unit_choices,
		widget=forms.SelectMultiple,
		label="Select Units:")

def get_random_noun(units_available):
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
		print(units_available)
		response = json.load(f)
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
		form = unit_form(request.POST)
		print(form)
		if form.is_valid():
			selected = form.cleaned_data['selected_items']
			print("selected:", selected)
			global units_available
			units_available = selected

		# get data only from selected units
		verb_form, gender, case, number = get_random_noun(units_available)
		return render(request, "first_app/nouns.html", {
			"form": NounForm(),
			"verb_form" : verb_form,
			"gender": gender,
			"case": case,
			"number": number,
			"unit_form": unit_form()
			})
	# embed noun form
	# embed its information
	else:
		#global units_available
		if units_available == []:
			units_available = ["unit_1"]
		verb_form, gender, case, number = get_random_noun(units_available)
		return render(request, "first_app/nouns.html", {
			"form": NounForm(),
			"verb_form" : verb_form,
			"gender": gender,
			"case": case,
			"number": number,
			"unit_form": unit_form()
			})
	# if the method is post, check the form

def index(request):
	return render(request, "first_app/index.html")
