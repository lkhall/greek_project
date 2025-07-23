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
all_verb_tenses = ["present","future","imperfect","aorist","perfect","pluperfect"]
verb_mood_choices = (
	("indic", "Indicative"),
	("subj", "Subjunctive"),
	("opt", "Optative"),
	("imper", "Imperative"),
	("infin", "Infinitive"),
)
all_verb_moods = ["indic","subj","opt","imper","infin"]
verb_voice_choices = (
	("act", "Active"),
	("mid", "Middle"),
	("pass", "Passive"),
)
all_verb_voices = ["act","mid","pass"]
verb_person = (
	("first", "First"),
	("second", "Second"),
	("third", "Third"),
)

verb_choices = (
	("παιδεύω", "παιδεύω"),
	("λείπω", "λείπω"),
	("δίδωμι", "δίδωμι"),
	("τίθημι","τίθημι"),
	("ἵστημι","ἵστημι"),
	("εἰμί","εἰμί"),
	("εἶμι","εἶμι")
)
units_available = []
nouns_available = []

on_units = True

on_units_adj = True
units_available_adjectives = []
adjectives_available = []

adjective_unit_choices = (
	("unit_4", "Unit 4"),
	("unit_8", "Unit 8"),
	("unit_10", "Unit 10"),
	("unit_16", "Unit 16"),
	("unit_17", "Unit 17"),
)

all_adjective_units = ["unit_4", "unit_8", "unit_10", "unit_16", "unit_17"]
adjective_choices = (
	("ἀγαθός, ἀγαθή, ἀγαθόν", "ἀγαθός, ἀγαθή, ἀγαθόν"),
	("ἄδικος, ἄδικον", "ἄδικος, ἄδικον"),
	("πᾶς, πᾶσα, πᾶν", "πᾶς, πᾶσα, πᾶν"),
	("εὐδαίμων, εὔδαιμον", "εὐδαίμων, εὔδαιμον"),
	("εὐγενής, εὐγενές", "εὐγενής, εὐγενές"),
	("πολύς, πολλή, πολύ", "πολύς, πολλή, πολύ"),
	("μέγας, μεγάλη, μέγα", "μέγας, μεγάλη, μέγα"),
	("ἡδύς, ἡδεῖα, ἡδύ", "ἡδύς, ἡδεῖα, ἡδύ"),
)
all_adjective_choices = ["ἀγαθός, ἀγαθή, ἀγαθόν", "ἄδικος, ἄδικον", "πᾶς, πᾶσα, πᾶν", "εὐδαίμων, εὔδαιμον", "εὐγενής, εὐγενές", "πολύς, πολλή, πολύ", "μέγας, μεγάλη, μέγα", "ἡδύς, ἡδεῖα, ἡδύ"]

verbs_avail = []

participle_choices = (
	("παιδεύω", "παιδεύω"),
)
participles_avail = []

participle_tense_choices = (
	("present", "Present"),
	("future", "Future"),
	("aorist", "Aorist"),
	("perfect", "Perfect"),
)

noun_on_unit = True
adjective_on_unit = True

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

class select_adj_form(forms.Form):
	selected_adjs = forms.MultipleChoiceField(
		choices=adjective_choices,
		widget=forms.SelectMultiple,
		label="Select Adjectives:")

class VerbForm(forms.Form):
	verb_choice = forms.MultipleChoiceField(choices=verb_choices, label="Verb", widget=forms.SelectMultiple)
	verb_tense = forms.MultipleChoiceField(choices=verb_tense_choices, label="Tense", widget=forms.SelectMultiple)
	verb_voice = forms.MultipleChoiceField(choices=verb_voice_choices, label="Voice", widget=forms.SelectMultiple)
	verb_mood = forms.MultipleChoiceField(choices=verb_mood_choices, label="Mood", widget=forms.SelectMultiple)

class ParticipleForm(forms.Form):
	participle_choice = forms.MultipleChoiceField(choices=participle_choices, label="Participle", widget=forms.SelectMultiple)
	participle_tense = forms.MultipleChoiceField(choices=participle_tense_choices, label="Tense", widget=forms.SelectMultiple)
	participle_voice = forms.MultipleChoiceField(choices=verb_voice_choices, label="Voice", widget=forms.SelectMultiple)

class ParticipleFormSubmit(forms.Form):
	participle_tense_submit = forms.MultipleChoiceField(choices=participle_tense_choices, label="Tense", widget=forms.CheckboxSelectMultiple)
	participle_voice_submit = forms.MultipleChoiceField(choices=verb_voice_choices, label="Voice", widget=forms.CheckboxSelectMultiple)
	participle_gender_submit = forms.MultipleChoiceField(choices=noun_gender_choices, label="Gender", widget=forms.CheckboxSelectMultiple)
	participle_case_submit = forms.MultipleChoiceField(choices=noun_case_choices, label="Case", widget=forms.CheckboxSelectMultiple)
	participle_number_submit = forms.MultipleChoiceField(choices=noun_number_choices, label="Number", widget=forms.CheckboxSelectMultiple)

# work on this 
class VerbFormSubmit(forms.Form):
	verb_tense_submit = forms.MultipleChoiceField(choices=verb_tense_choices, label="Tense", widget=forms.CheckboxSelectMultiple)
	verb_voice_submit = forms.MultipleChoiceField(choices=verb_voice_choices, label="Voice", widget=forms.CheckboxSelectMultiple)
	verb_mood_submit = forms.MultipleChoiceField(choices=verb_mood_choices, label="Mood", widget=forms.CheckboxSelectMultiple)
	verb_person = forms.MultipleChoiceField(choices=verb_person, label="Person", widget=forms.CheckboxSelectMultiple)
	verb_number = forms.MultipleChoiceField(choices=noun_number_choices, label="Number", widget=forms.CheckboxSelectMultiple)

class adjective_unit_form(forms.Form):
	selected_adj_units = forms.MultipleChoiceField(
		choices=adjective_unit_choices,
		widget=forms.SelectMultiple,
		label="Select Units:")

def get_random_noun(units_available):

	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
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
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/greek_data_by_unit.json') as f:
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
		# first_key = next(iter(data))
		# first_value = data[first_key]
		# forms = first_value["forms"]
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
				global nouns_available
				nouns_available = []
				global noun_on_unit
				noun_on_unit = True
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
					"noun_form": select_noun_form(),
					"noun_on_unit": noun_on_unit,
					"units_available": units_available,
					"nouns_available":nouns_available
					})
			elif request.POST['submit_form'] == 'submitting_nouns':
				units_available = []
				on_units = False
				noun_on_unit = False
				form = select_noun_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_nouns']
					print("selected:", selected)
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
					"noun_form": select_noun_form(),
					"noun_on_unit": noun_on_unit,
					"units_available": units_available,
					"nouns_available":nouns_available
					})
	# embed noun form
	# embed its information
	else:
		print("noun on unit: ", noun_on_unit)
		print("hello")
		global units_available
		if units_available == []:
			units_available = ["unit_1"]
		global nouns_available
		if nouns_available == []:
			nouns_available = ["τέχνη"]
		if on_units == True:
			nouns_available = []
			verb_form, gender, case, number = get_random_noun(units_available)
		else:
			units_available = []
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
			"noun_form": select_noun_form(),
			"noun_on_unit": noun_on_unit,
			"units_available": units_available,
			"nouns_available":nouns_available
			})

#def get_random_verb_form():


	# if the method is post, check the form
def verbs(request):
	if request.method == "POST":
		if 'submit_form' in request.POST:
			# if the user submits the form selecting what things they want to be quizzed on
			# extract choices, see if they are available in data
			if request.POST['submit_form'] == 'submitting_type_selection':
				print("POSTTTT TO VERBS");
				form = VerbForm(request.POST)
				print(form)
				if form.is_valid():
					selected_verb = form.cleaned_data['verb_choice']
					selected_tense = form.cleaned_data['verb_tense']
					selected_voice = form.cleaned_data['verb_voice']
					selected_mood = form.cleaned_data['verb_mood']
					print("selected:", selected_verb)
					print("selected tense :", selected_tense)
					# global variable for acombo works
					# big combosdontwork array
					# big comboswork array
					total_acomboworks = False
					total_combosdontwork = []
					total_comboswork = []

					for item in selected_verb:
						acomboworks, combosdontwork, comboswork = check_form_combos(item, selected_tense, selected_voice, selected_mood)
						total_acomboworks = total_acomboworks or acomboworks
						total_combosdontwork = total_combosdontwork + combosdontwork
						total_comboswork = total_comboswork + comboswork

					tense_not_used,voice_not_used,mood_not_used,tense_used,voice_used,mood_used,tenses_used,voices_used,moods_used = combosnotused(total_comboswork)
					print("tense used: ",tense_used)
					print("mood used: ",mood_used)
					print("voice used: ",voice_used)
					print("tenses_not_used: ", tense_not_used)
					print("acomboworks: ", total_acomboworks)
					print("combosdontwork: ", total_combosdontwork)
					# if no combo works
					if not total_acomboworks:
						errormessage = "None of the forms submitted exist. Please resubmit."
						formsdontwork = ",".join(str(x) for x in combosdontwork)
						return render(request, "first_app/verbs.html", {
						"form": VerbForm(), "verb_form_submit": VerbFormSubmit(), "errormessage" : errormessage, "formsdontwork" : formsdontwork})
					# if some combos work but some donts
					global verbs_avail
					verbs_avail = total_comboswork
					if combosdontwork != []:
						errormessage = "Some of the selected forms do not exist."
						formsdontwork = ",".join(str(x) for x in total_combosdontwork)
						verb_form, tense, voice, mood, person, number = generate_random_verb(verbs_avail)
						return render(request, "first_app/verbs.html", {
							"form": VerbForm(),
							"verb_form" : verb_form,
							"tense": tense,
							"voice": voice,
							"mood": mood,
							"person": person,
							"number": number,
							"errormessage" : errormessage,
							"verb_form_submit": VerbFormSubmit(),
							"tense_not_used":tense_not_used,
							"voice_not_used":voice_not_used,
							"mood_not_used":mood_not_used,
							"tense_used":tense_used,
							"mood_used":mood_used,
							"voice_used":voice_used,
							"tenses_used":tenses_used,
							"moods_used":moods_used,
							"voices_used":voices_used,
							"verbs_used":selected_verb,
							"formsdontwork":formsdontwork,
							})
					# if all combos work
					else:
						verb_form, tense, voice, mood, person, number = generate_random_verb(verbs_avail)

						return render(request, "first_app/verbs.html", {
							"form": VerbForm(),
							"verb_form" : verb_form,
							"tense": tense,
							"voice": voice,
							"mood": mood,
							"person": person,
							"number": number,
							"verb_form_submit": VerbFormSubmit(),
							"tense_not_used":tense_not_used,
							"voice_not_used":voice_not_used,
							"mood_not_used":mood_not_used,
							"tense_used":tense_used,
							"mood_used":mood_used,
							"voice_used":voice_used,
							"tenses_used":tenses_used,
							"moods_used":moods_used,
							"voices_used":voices_used,
							"verbs_used":selected_verb,
							"errormessage": "False"
							})


					#verb_data = dumps(f)
					# if a combo works, generate a form
					# if combosdontwork is not empty, give a message
					#if a combo doesnt work give a message
					return render(request, "first_app/verbs.html", {
						"form": VerbForm(), "verb_form_submit": VerbFormSubmit()
						})
	else:
		if verbs_avail == []:
			verbs_avail = [["παιδεύω", "present","act","indic"]]
		verb_form, tense, voice, mood, person, number = generate_random_verb(verbs_avail)
		tense_not_used,voice_not_used,mood_not_used,tense_used,voice_used,mood_used,tenses_used,voices_used,moods_used = combosnotused(verbs_avail)
		selected_verb = selected_verbs(verbs_avail)
		return render(request, "first_app/verbs.html", {
			"form": VerbForm(),
			"verb_form" : verb_form,
			"tense": tense,
			"voice": voice,
			"mood": mood,
			"person": person,
			"number": number,
			"verb_form_submit": VerbFormSubmit(),
			"tense_not_used":tense_not_used,
			"voice_not_used":voice_not_used,
			"mood_not_used":mood_not_used,
			"tense_used":tense_used,
			"mood_used":mood_used,
			"voice_used":voice_used,
			"tenses_used":tenses_used,
			"moods_used":moods_used,
			"voices_used":voices_used,
			"verbs_used": selected_verb
			})

def selected_verbs(verbs_avail):
	allverbs = []
	for thingg in verbs_avail:
		if thingg[0] not in allverbs:
			allverbs.append(thingg[0])
	return allverbs

def combosnotused(comboswork):
	# for each combo remove that from the arrays
	tenses_not_used = all_verb_tenses.copy()
	voices_not_used = all_verb_voices.copy()
	print(voices_not_used)
	moods_not_used = all_verb_moods.copy()

	tenses_used = []
	voices_used = []
	moods_used = []
	for acombo in comboswork:
		print("hello")
		print(acombo)
		print(voices_not_used)
		if acombo[1] in tenses_not_used:
			tenses_not_used.remove(acombo[1])
		if acombo[2] in voices_not_used:
			voices_not_used.remove(acombo[2])
		if acombo[3] in moods_not_used:
			moods_not_used.remove(acombo[3])

		if acombo[1] not in tenses_used:
			tenses_used.append(acombo[1])
		if acombo[2] not in voices_used:
			voices_used.append(acombo[2])
		if acombo[3] not in moods_used:
			moods_used.append(acombo[3])
	mood_cross_info = [["indic","id_verb_mood_submit_0"],["subj","id_verb_mood_submit_1"],["opt","id_verb_mood_submit_2"],["imper","id_verb_mood_submit_3"],["infin","id_verb_mood_submit_4"]];
	voice_cross_info = [["act","id_verb_voice_submit_0"],["mid","id_verb_voice_submit_1"],["pass","id_verb_voice_submit_2"]];
	tense_cross_info = [["present","id_verb_tense_submit_0"],["future","id_verb_tense_submit_1"],["imperfect","id_verb_tense_submit_2"],["aorist","id_verb_tense_submit_3"],["perfect","id_verb_tense_submit_4"],["pluperfect","id_verb_tense_submit_5"]];
	tense_not_used = []
	voice_not_used = []
	mood_not_used = []

	tense_used = []
	voice_used = []
	mood_used = []

	for atense in tenses_used:
		for tense_cross in tense_cross_info:
			if atense == tense_cross[0]:
				tense_used.append(tense_cross[1])
	for avoice in voices_used:
		for voice_cross in voice_cross_info:
			if avoice == voice_cross[0]:
				voice_used.append(voice_cross[1])
	for amood in moods_used:
		for mood_cross in mood_cross_info:
			if amood == mood_cross[0]:
				mood_used.append(mood_cross[1])

	for atense in tenses_not_used:
		for tense_cross in tense_cross_info:
			if atense == tense_cross[0]:
				tense_not_used.append(tense_cross[1])
	for avoice in voices_not_used:
		for voice_cross in voice_cross_info:
			if avoice == voice_cross[0]:
				voice_not_used.append(voice_cross[1])
	for amood in moods_not_used:
		for mood_cross in mood_cross_info:
			if amood == mood_cross[0]:
				mood_not_used.append(mood_cross[1])
	return tense_not_used,voice_not_used,mood_not_used,tense_used,voice_used,mood_used,tenses_used,voices_used,moods_used

def generate_random_verb(verbs_avail):
	# select random combo from verbs avail
	random_int = random.randint(0, len(verbs_avail)-1)
	selected_form = verbs_avail[random_int]
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/verb_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/verb_data.json') as f:
		response = json.load(f)
		# get forms of verb
		verb_forms = response["verbs"][selected_form[0]]["forms"]
		# get random form
		random_vform = random.randint(0, len(verb_forms)-1)
		selected_combo = verb_forms[random_vform]
		print("selected_combo: ",selected_combo)
		first_key = next(iter(selected_combo))
		first_value = selected_combo[first_key]
		# iterate through each conjugation of the form
		returned_tense = []
		returned_voice = []
		returned_mood = []
		returned_person = []
		returned_number = []
		found_form = False
		print("first val: ",first_value)
		print("len of first_value: ",len(first_value))
		for i in range(len(first_value)):
			if ((selected_form[1] in first_value[i]["tense"]) and (selected_form[2] in first_value[i]["voice"]) and (selected_form[3] in first_value[i]["mood"])):
				found_form = True
				print("FOUND FORM")
				if len(first_value) == 1:
					return first_key, first_value[i]["tense"], first_value[i]["voice"], first_value[i]["mood"], first_value[i]["person"], first_value[i]["number"]
				# add to returned tense, then  iterate through other forms and see if they are in verbs_avail
				returned_tense.append(first_value[i]["tense"][0])
				returned_voice.append(first_value[i]["voice"][0])
				returned_mood.append(first_value[i]["mood"][0])
				if (len(first_value[i]["person"]) != 0):
					returned_person.append(first_value[i]["person"][0])
				if (len(first_value[i]["number"]) != 0):
					returned_number.append(first_value[i]["number"][0])
				# iterate through the rest of first value and check if the forms are in verbs avail
				for j in range(len(first_value)):
					print("checking other things")
					# for each form not the one just checked, see if it is in verbs_avail
					if j != i:
						for thingg in verbs_avail:
							if (thingg[1] in first_value[j]["tense"] and thingg[2] in first_value[j]["voice"] and thingg[3] in first_value[j]["mood"]):
								print("adding another form")
								returned_tense.append(first_value[j]["tense"][0])
								returned_voice.append(first_value[j]["voice"][0])
								returned_mood.append(first_value[j]["mood"][0])
								if (len(first_value[i]["person"]) != 0):
									returned_person.append(first_value[j]["person"][0])
								if (len(first_value[i]["number"]) != 0):
									returned_number.append(first_value[j]["number"][0])
				break

		while (found_form == False):
			random_vform = random.randint(0, len(verb_forms)-1)
			selected_combo = verb_forms[random_vform]
			first_key = next(iter(selected_combo))
			first_value = selected_combo[first_key]
			print("first val: ",first_value)
			print("len of first_value: ",len(first_value))
			for i in range(len(first_value)):
				if ((selected_form[1] in first_value[i]["tense"]) and (selected_form[2] in first_value[i]["voice"]) and (selected_form[3] in first_value[i]["mood"])):
					found_form = True
					print("FOUND FORM")
					if len(first_value) == 1:
						return first_key, first_value[i]["tense"], first_value[i]["voice"], first_value[i]["mood"], first_value[i]["person"], first_value[i]["number"]
					# add to returned tense, then  iterate through other forms and see if they are in verbs_avail
					returned_tense.append(first_value[i]["tense"][0])
					returned_voice.append(first_value[i]["voice"][0])
					returned_mood.append(first_value[i]["mood"][0])
					if (len(first_value[i]["person"]) != 0):
						returned_person.append(first_value[i]["person"][0])
					if (len(first_value[i]["number"]) != 0):
						returned_number.append(first_value[i]["number"][0])
					# iterate through the rest of first value and check if the forms are in verbs avail
					for j in range(len(first_value)):
						print("checking other things")
						# for each form not the one just checked, see if it is in verbs_avail
						if j != i:
							for thingg in verbs_avail:
								if (thingg[1] in first_value[j]["tense"] and thingg[2] in first_value[j]["voice"] and thingg[3] in first_value[j]["mood"]):
									print("adding another form")
									returned_tense.append(first_value[j]["tense"][0])
									returned_voice.append(first_value[j]["voice"][0])
									returned_mood.append(first_value[j]["mood"][0])
									if (len(first_value[i]["person"]) != 0):
										returned_person.append(first_value[j]["person"][0])
									if (len(first_value[i]["number"]) != 0):
										returned_number.append(first_value[j]["number"][0])
					break
		# randomly selected a verb
		# iterate through its forms to see if selected form is there
		# if yes, add to forms if there is more than one form
		# if no, re-randomly select a verb
		# for conjug in first_value:

		# while ((selected_form[1] not in first_value["tense"]) or (selected_form[2] not in first_value["voice"]) or (selected_form[3] not in first_value["mood"])):
		# 	random_vform = random.randint(0, len(verb_forms)-1)
		# 	selected_combo = verb_forms[random_vform]
		# 	first_key = next(iter(selected_combo))
		# 	first_value = selected_combo[first_key]
		# 	print("going")
		print("returned person: ",returned_person)
		print("returned number: ",returned_number)
		return first_key, returned_tense, returned_voice, returned_mood, returned_person, returned_number

# returns whether there is a combo that works and an array of combos that dontwork
def check_form_combos(selected_verb, tense_forms, voice_forms, mood_forms):
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/verb_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/verb_data.json') as f:
		response = json.load(f)
		verb_viable_combos = response["verbs"][selected_verb]["viable_combos"]
		acomboworks = False
		combosdontwork = []
		comboswork = []
		print("selected verb: ", selected_verb)
		print("selected tense: ", tense_forms)
		print("selected voice: ", voice_forms)
		print("selected mood: ", mood_forms)
		print("viable combos: ", verb_viable_combos)
		for tense_form in tense_forms:
			for voice_form in voice_forms:
				for mood_form in mood_forms:
					# iterate through all the viable combos
					found = False
					for acombo in verb_viable_combos:
						print("tense: ", tense_form, " voice: ", voice_form, "mood: ", mood_form)
						first_key = next(iter(acombo))
						first_value = acombo[first_key]
						print("acombo: ", first_value)
						if ((tense_form == first_value["tense"]) and (voice_form == first_value["voice"]) and (mood_form == first_value["mood"])):
							found = True
					if found == False:
						combosdontwork.append([selected_verb, tense_form,voice_form,mood_form])
					else: 
						acomboworks = True
						comboswork.append([selected_verb, tense_form,voice_form,mood_form])
		return acomboworks,combosdontwork, comboswork

def get_random_adj(units_available_adjectives):
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/adjective_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/adjective_data.json') as f:
		print(units_available_adjectives)
		response = json.load(f)
		if (units_available_adjectives == []):
			units_available_adjectives = all_adjective_units
		selected_unit = random.choice(units_available_adjectives)
		print("selected unit: ", selected_unit)
		data = response[selected_unit]['adjectives']
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
		return verb_form, verb_data["gender"], verb_data["case"], verb_data["number"]

def get_random_adj2(adjectives_available):
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/adjective_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/adjective_data.json') as f:
		print(adjectives_available)
		# select random unit
		# select random noun
		# check if noun is in the nouns available
		response = json.load(f)
		if (adjectives_available == []):
			adjectives_available = all_adjectives
		selected_unit = random.choice(all_adjective_units)
		print("selected unit: ", selected_unit)
		data = response[selected_unit]['adjectives']
		num_nouns = len(data)
		# selecting random noun within a unit
		random_int = random.randint(0, num_nouns-1)
		data = data[random_int]

		# use random number to get random noun
		first_key = next(iter(data))
		first_value = data[first_key]
		forms = first_value["forms"]
		while first_key not in adjectives_available:
			selected_unit = random.choice(all_adjective_units)
			print("selected noun: ", first_key)
			print("ajs avail: ", adjectives_available)
			data = response[selected_unit]['adjectives']
			num_nouns = len(data)
			# selecting random noun within a unit
			random_int = random.randint(0, num_nouns-1)
			data = data[random_int]
			first_key = next(iter(data))
			first_value = data[first_key]
			forms = first_value["forms"]

		# use random number to get random noun
		# first_key = next(iter(data))
		# first_value = data[first_key]
		# forms = first_value["forms"]
		# get random thing in noun by generating random int between 0 and 9
		# retrieve its data 
		random_int = random.randint(0, len(forms)-1)
		selected_form = forms[random_int]
		verb_form = next(iter(selected_form))
		verb_data = selected_form[verb_form]
		print(verb_data)
		return verb_form, verb_data["gender"], verb_data["case"], verb_data["number"]

def adjectives(request):
	if request.method == "POST":
		if 'submit_form' in request.POST:
			if request.POST['submit_form'] == 'submitting_units':
				print("SUBMITTING UNITS")
				global on_units_adj
				on_units_adj = True

				global adjectives_available
				adjectives_available = []
				form = adjective_unit_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_adj_units']
					print("selected:", selected)
					global units_available_adjectives
					if units_available_adjectives == []:
						units_available_adjectives = all_adjective_units
					units_available_adjectives = selected
					print("units_avail_adj: ", units_available_adjectives)
				adj_form, gender, case, number = get_random_adj(units_available_adjectives)
				return render(request, "first_app/adjectives.html", {
					"form": NounForm(),
					"adj_form" : adj_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": adjective_unit_form(),
					"noun_form": select_adj_form(),
					"adjective_on_unit": on_units_adj,
					"units_available": units_available_adjectives,
					"adjectives_available": adjectives_available
					})
			elif request.POST['submit_form'] == 'submitting_adjs':
				print("SUBMITTING ADJECTIVes")
				units_available_adjectives = []
				on_units_adj = False
				form = select_adj_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_adjs']
					print("selected:", selected)
					
					if adjectives_available == []:
						print("no adjectives available in submission")
						adjectives_available = all_adjective_choices
					adjectives_available = selected
					print("adjectives_avai;: ", adjectives_available)
				adj_form, gender, case, number = get_random_adj2(adjectives_available)
				return render(request, "first_app/adjectives.html", {
					"form": NounForm(),
					"adj_form" : adj_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": adjective_unit_form(),
					"noun_form": select_adj_form(),
					"adjective_on_unit": on_units_adj,
					"units_available": units_available_adjectives,
					"adjectives_available": adjectives_available
					})
	else:
		print("adj avail : ", adjectives_available)
		print("units avail for adj : ", units_available_adjectives)

		print("hello")
		#global units_available
		if units_available_adjectives == []:
			units_available_adjectives = ["unit_4"]
		if adjectives_available == []:
			print("there are no adjectives")
			adjectives_available = ["ἀγαθός, ἀγαθή, ἀγαθόν"]
		if on_units_adj == True:
			adjectives_available = []
			adj_form, gender, case, number = get_random_adj(units_available_adjectives)
		else:
			units_available_adjectives = []
			adj_form, gender, case, number = get_random_adj2(adjectives_available)
		print(gender)
		print(case)
		print(number)
		return render(request, "first_app/adjectives.html", {
			"form": NounForm(),
			"adj_form" : adj_form,
			"gender": gender,
			"case": case,
			"number": number,
			"unit_form": adjective_unit_form(),
			"noun_form": select_adj_form(),
			"adjective_on_unit": on_units_adj,
			"units_available": units_available_adjectives,
			"adjectives_available": adjectives_available
			})

def check_form_combos_participle(selected_participle, tense_forms, voice_forms):
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/participle_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/participle_data.json') as f:
		response = json.load(f)
		participle_viable_combos = response["participles"][selected_participle]["viable_combos"]
		acomboworks = False
		combosdontwork = []
		comboswork = []
		print("selected participle: ", selected_participle)
		print("selected tense: ", tense_forms)
		print("selected voice: ", voice_forms)
		print("viable combos: ", participle_viable_combos)
		for tense_form in tense_forms:
			for voice_form in voice_forms:
				# iterate through all the viable combos
				found = False
				for acombo in participle_viable_combos:
					print("tense: ", tense_form, " voice: ", voice_form)
					first_key = next(iter(acombo))
					first_value = acombo[first_key]
					print("acombo: ", first_value)
					if ((tense_form == first_value["tense"]) and (voice_form == first_value["voice"])):
						found = True
				if found == False:
					combosdontwork.append([selected_participle, tense_form,voice_form])
				else: 
					acomboworks = True
					comboswork.append([selected_participle, tense_form,voice_form])
		return acomboworks,combosdontwork, comboswork

def combosnotused_participle(comboswork):
	# for each combo remove that from the arrays
	tenses_not_used = all_verb_tenses.copy()
	voices_not_used = all_verb_voices.copy()
	print(voices_not_used)

	tenses_used = []
	voices_used = []
	for acombo in comboswork:
		print("hello")
		print(acombo)
		print(voices_not_used)
		if acombo[1] in tenses_not_used:
			tenses_not_used.remove(acombo[1])
		if acombo[2] in voices_not_used:
			voices_not_used.remove(acombo[2])

		if acombo[1] not in tenses_used:
			tenses_used.append(acombo[1])
		if acombo[2] not in voices_used:
			voices_used.append(acombo[2])
	voice_cross_info = [["act","id_participle_voice_submit_0"],["mid","id_participle_voice_submit_1"],["pass","id_participle_voice_submit_2"]];
	tense_cross_info = [["present","id_participle_tense_submit_0"],["future","id_participle_tense_submit_1"],["aorist","id_participle_tense_submit_2"],["perfect","id_participle_tense_submit_3"]];
	
	tense_not_used = []
	voice_not_used = []

	tense_used = []
	voice_used = []

	for atense in tenses_used:
		for tense_cross in tense_cross_info:
			if atense == tense_cross[0]:
				tense_used.append(tense_cross[1])
	for avoice in voices_used:
		for voice_cross in voice_cross_info:
			if avoice == voice_cross[0]:
				voice_used.append(voice_cross[1])

	for atense in tenses_not_used:
		for tense_cross in tense_cross_info:
			if atense == tense_cross[0]:
				tense_not_used.append(tense_cross[1])
	for avoice in voices_not_used:
		for voice_cross in voice_cross_info:
			if avoice == voice_cross[0]:
				voice_not_used.append(voice_cross[1])

	return tense_not_used,voice_not_used,tense_used,voice_used,tenses_used,voices_used

def generate_random_participle(participles_avail):
	# select random combo from verbs avail
	random_int = random.randint(0, len(participles_avail)-1)
	selected_form = participles_avail[random_int]
	#with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/participle_data.json') as f:
	with open('/home/user/greek_project/greekproj/first_app/participle_data.json') as f:
		response = json.load(f)
		# get forms of verb
		participle_forms = response["participles"][selected_form[0]]["forms"]
		# get random form
		random_vform = random.randint(0, len(participle_forms)-1)
		selected_combo = participle_forms[random_vform]
		print("selected_combo: ",selected_combo)
		first_key = next(iter(selected_combo))
		first_value = selected_combo[first_key]
		# iterate through each conjugation of the form
		returned_tense = []
		returned_voice = []
		returned_case = []
		returned_gender = []
		returned_number = []
		found_form = False
		print("first val: ",first_value)
		print("len of first_value: ",len(first_value))
		for i in range(len(first_value)):
			if ((selected_form[1] in first_value[i]["tense"]) and (selected_form[2] in first_value[i]["voice"])):
				found_form = True
				print("FOUND FORM")
				if len(first_value) == 1:
					return first_key, first_value[i]["tense"], first_value[i]["voice"], first_value[i]["case"], first_value[i]["gender"], first_value[i]["number"]
				# add to returned tense, then  iterate through other forms and see if they are in verbs_avail
				returned_tense.append(first_value[i]["tense"][0])
				returned_voice.append(first_value[i]["voice"][0])
				returned_case.append(first_value[i]["case"][0])
				returned_number.append(first_value[i]["number"][0])
				returned_gender.append(first_value[i]["gender"][0])
				# iterate through the rest of first value and check if the forms are in verbs avail
				for j in range(len(first_value)):
					print("checking other things")
					# for each form not the one just checked, see if it is in verbs_avail
					if j != i:
						for thingg in participles_avail:
							if (thingg[1] in first_value[j]["tense"] and thingg[2] in first_value[j]["voice"]):
								print("adding another form")
								returned_tense.append(first_value[j]["tense"][0])
								returned_voice.append(first_value[j]["voice"][0])
								returned_case.append(first_value[j]["case"][0])
								returned_number.append(first_value[j]["number"][0])
								returned_gender.append(first_value[j]["gender"][0])
				break

		while (found_form == False):
			random_vform = random.randint(0, len(participle_forms)-1)
			selected_combo = participle_forms[random_vform]
			first_key = next(iter(selected_combo))
			first_value = selected_combo[first_key]
			print("first val: ",first_value)
			print("len of first_value: ",len(first_value))
			for i in range(len(first_value)):
				if ((selected_form[1] in first_value[i]["tense"]) and (selected_form[2] in first_value[i]["voice"])):
					found_form = True
					print("FOUND FORM")
					if len(first_value) == 1:
						return first_key, first_value[i]["tense"], first_value[i]["voice"], first_value[i]["case"], first_value[i]["gender"], first_value[i]["number"]
					# add to returned tense, then  iterate through other forms and see if they are in verbs_avail
					returned_tense.append(first_value[i]["tense"][0])
					returned_voice.append(first_value[i]["voice"][0])
					returned_case.append(first_value[i]["case"][0])
					returned_number.append(first_value[i]["number"][0])
					returned_gender.append(first_value[i]["gender"][0])
					# iterate through the rest of first value and check if the forms are in verbs avail
					for j in range(len(first_value)):
						print("checking other things")
						# for each form not the one just checked, see if it is in verbs_avail
						if j != i:
							for thingg in participles_avail:
								if (thingg[1] in first_value[j]["tense"] and thingg[2] in first_value[j]["voice"]):
									print("adding another form")
									returned_tense.append(first_value[j]["tense"][0])
									returned_voice.append(first_value[j]["voice"][0])
									returned_case.append(first_value[j]["case"][0])
									returned_number.append(first_value[j]["number"][0])
									returned_gender.append(first_value[j]["gender"][0])
					break
		print("first_key: ",first_key)
		return first_key, returned_tense, returned_voice, returned_case, returned_gender, returned_number

def participles(request):
	if request.method == "POST":
		if 'submit_form' in request.POST:
			# if the user submits the form selecting what things they want to be quizzed on
			# extract choices, see if they are available in data
			if request.POST['submit_form'] == 'submitting_type_selection':
				print("POSTTTT TO participles");
				form = ParticipleForm(request.POST)
				print(form)
				if form.is_valid():
					selected_participle = form.cleaned_data['participle_choice']
					selected_tense = form.cleaned_data['participle_tense']
					selected_voice = form.cleaned_data['participle_voice']
					print("selected:", selected_participle)
					print("selected tense :", selected_tense)
					# global variable for acombo works
					# big combosdontwork array
					# big comboswork array
					total_acomboworks = False
					total_combosdontwork = []
					total_comboswork = []

					for item in selected_participle:
						acomboworks, combosdontwork, comboswork = check_form_combos_participle(item, selected_tense, selected_voice)
						total_acomboworks = total_acomboworks or acomboworks
						total_combosdontwork = total_combosdontwork + combosdontwork
						total_comboswork = total_comboswork + comboswork

					tense_not_used,voice_not_used,tense_used,voice_used, tenses_used,voices_used = combosnotused_participle(total_comboswork)
					print("tense used: ",tense_used)
					print("voice used: ",voice_used)
					print("tenses_not_used: ", tense_not_used)
					print("acomboworks: ", total_acomboworks)
					print("combosdontwork: ", total_combosdontwork)
					# if no combo works
					if not total_acomboworks:
						errormessage = "None of the following forms exist: " + ",".join(str(x) for x in combosdontwork) + ". Please resubmit."
						return render(request, "first_app/participles.html", {
						"form": ParticipleForm(), "participle_form_submit": ParticipleFormSubmit(), "errormessage" : errormessage})
					# if some combos work but some donts
					global participles_avail
					participles_avail = total_comboswork
					if combosdontwork != []:
						errormessage = "The following forms don't exist: " + ",".join(str(x) for x in total_combosdontwork)
						participle_form, tense, voice, case, gender, number = generate_random_participle(participles_avail)
						return render(request, "first_app/participles.html", {
							"form": ParticipleForm(),
							"participle_form" : participle_form,
							"tense": tense,
							"voice": voice,
							"case": case,
							"gender": gender,
							"number": number,
							"errormessage" : errormessage,
							"participle_form_submit": ParticipleFormSubmit(),
							"tense_not_used":tense_not_used,
							"voice_not_used":voice_not_used,
							"tense_used":tense_used,
							"voice_used":voice_used,
							"tenses_used":tenses_used,
							"voices_used":voices_used,
							"participles_used":selected_participle
							})
					# if all combos work
					else:
						participle_form, tense, voice, case, gender, number = generate_random_participle(participles_avail)

						return render(request, "first_app/participles.html", {
							"form": ParticipleForm(),
							"participle_form" : participle_form,
							"tense": tense,
							"voice": voice,
							"case": case,
							"gender": gender,
							"number": number,
							"participle_form_submit": ParticipleFormSubmit(),
							"tense_not_used":tense_not_used,
							"voice_not_used":voice_not_used,
							"tense_used":tense_used,
							"voice_used":voice_used,
							"tenses_used":tenses_used,
							"voices_used":voices_used,
							"participles_used":selected_participle
							})
	else:
		if participles_avail == []:
			participles_avail = [["παιδεύω", "present","act"]]
		participle_form, tense, voice, case, gender, number = generate_random_participle(participles_avail)
		tense_not_used,voice_not_used,tense_used,voice_used,tenses_used,voices_used = combosnotused_participle(participles_avail)
		selected_participle = selected_participles(participles_avail)
		return render(request, "first_app/participles.html", {
			"form": ParticipleForm(),
			"participle_form" : participle_form,
			"tense": tense,
			"voice": voice,
			"case": case,
			"gender": gender,
			"number": number,
			"participle_form_submit": ParticipleFormSubmit(),
			"tense_not_used":tense_not_used,
			"voice_not_used":voice_not_used,
			"tense_used":tense_used,
			"voice_used":voice_used,
			"tenses_used":tenses_used,
			"voices_used":voices_used,
			"participles_used":selected_participle
			})
def selected_participles(participles_avail):
	allverbs = []
	for thingg in participles_avail:
		if thingg[0] not in participles_avail:
			allverbs.append(thingg[0])
	return allverbs

def index(request):
	return render(request, "first_app/index.html")
