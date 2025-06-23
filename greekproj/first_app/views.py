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

class NounForm(forms.Form):
	noun_gender = forms.ChoiceField(choices=noun_gender_choices, label="Gender")
	noun_case = forms.ChoiceField(choices=noun_case_choices, label="Case")
	noun_number = forms.ChoiceField(choices=noun_number_choices, label="Number")


def get_random_noun():
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greekdata.json') as f:
		response = json.load(f)
		data = response['first_declension']['nouns']
		# use random number to get random noun
		first_key = next(iter(data))
		first_value = data[first_key]

		# get random thing in noun by generating random int between 0 and 9
		# retrieve its data 
		random_int = random.randint(0, 9)
		if 0 <= random_int <= 4:
			n_number = "singular"
			verb_n = first_value["singular"]
			#final_case = "blah"
			#final_verb = "x"
			i = 0
			for key, value in verb_n.items():
				if i == random_int:
					return value, first_value["gender"], key, n_number
				i = i+1
		else:
			n_number = "plural"
			verb_n = first_value["plural"]
			final_case = "nom"
			final_verb = "tex"
			i = 0
			for key, value in verb_n.items():
				if i == (random_int % 5):
					return value, first_value["gender"], key, n_number
				i = i+1


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
	verb_form, gender, case, number = get_random_noun()
	# embed noun form
	# embed its information
	return render(request, "first_app/nouns.html", {
		"form": NounForm(),
		"verb_form" : verb_form,
		"gender": gender,
		"case": case,
		"number": number
		})
	# if the method is post, check the form

def index(request):
	return render(request, "first_app/index.html")
