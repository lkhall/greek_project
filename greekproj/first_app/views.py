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
					for item in selected_verb:
						acomboworks, combosdontwork, comboswork = check_form_combos(item, selected_tense, selected_voice, selected_mood)

						tense_not_used,voice_not_used,mood_not_used = combosnotused(comboswork)
						print("tenses_not_used: ", tense_not_used)
						print("acomboworks: ", acomboworks)
						print("combosdontwork: ", combosdontwork)
						# if no combo works
						if not acomboworks:
							errormessage = "None of the following forms exist: " + ",".join(str(x) for x in combosdontwork) + ". Please resubmit."
							return render(request, "first_app/verbs.html", {
							"form": VerbForm(), "verb_form_submit": VerbFormSubmit(), "errormessage" : errormessage})
						# if some combos work but some donts
						global verbs_avail
						verbs_avail = comboswork
						if combosdontwork != []:
							errormessage = "The following forms don't exist: " + ",".join(str(x) for x in combosdontwork)
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
								"mood_not_used":mood_not_used
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
								"mood_not_used":mood_not_used
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
		tense_not_used,voice_not_used,mood_not_used = combosnotused(verbs_avail)
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
			"mood_not_used":mood_not_used
			})

def combosnotused(comboswork):
	# for each combo remove that from the arrays
	tenses_not_used = all_verb_tenses.copy()
	voices_not_used = all_verb_voices.copy()
	print(voices_not_used)
	moods_not_used = all_verb_moods.copy()
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
	mood_cross_info = [["indic","id_verb_mood_submit_0"],["subj","id_verb_mood_submit_1"],["opt","id_verb_mood_submit_2"],["imper","id_verb_mood_submit_3"],["infin","id_verb_mood_submit_4"]];
	voice_cross_info = [["act","id_verb_voice_submit_0"],["mid","id_verb_voice_submit_1"],["pass","id_verb_voice_submit_2"]];
	tense_cross_info = [["present","id_verb_tense_submit_0"],["future","id_verb_tense_submit_1"],["imperfect","id_verb_tense_submit_2"],["aorist","id_verb_tense_submit_3"],["perfect","id_verb_tense_submit_4"],["pluperfect","id_verb_tense_submit_5"]];
	tense_not_used = []
	voice_not_used = []
	mood_not_used = []
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
	return tense_not_used,voice_not_used,mood_not_used

def generate_random_verb(verbs_avail):
	# select random combo from verbs avail
	random_int = random.randint(0, len(verbs_avail)-1)
	selected_form = verbs_avail[random_int]
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/verb_data.json') as f:
		response = json.load(f)
		# get forms of verb
		verb_forms = response["verbs"][selected_form[0]]["forms"]
		# get random form
		random_vform = random.randint(0, len(verb_forms)-1)
		selected_combo = verb_forms[random_vform]
		first_key = next(iter(selected_combo))
		first_value = selected_combo[first_key]
		while ((selected_form[1] not in first_value["tense"]) or (selected_form[2] not in first_value["voice"]) or (selected_form[3] not in first_value["mood"])):
			random_vform = random.randint(0, len(verb_forms)-1)
			selected_combo = verb_forms[random_vform]
			first_key = next(iter(selected_combo))
			first_value = selected_combo[first_key]
			print("going")
		return first_key, first_value["tense"], first_value["voice"], first_value["mood"], first_value["person"], first_value["number"]

# returns whether there is a combo that works and an array of combos that dontwork
def check_form_combos(selected_verb, tense_forms, voice_forms, mood_forms):
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/verb_data.json') as f:
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
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/adjective_data.json') as f:
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
	with open('/Users/lauren/greek_proj/greek_project/greekproj/first_app/adjective_data.json') as f:
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
				global on_units_adj
				on_units_adj = True
				form = adjective_unit_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_adj_units']
					print("selected:", selected)
					global units_available_adjectives
					if units_available_adjectives == []:
						units_available_adjectives = all_adjective_units
					units_available_adjectives = selected
				adj_form, gender, case, number = get_random_adj(units_available_adjectives)
				return render(request, "first_app/adjectives.html", {
					"form": NounForm(),
					"adj_form" : adj_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": adjective_unit_form(),
					"noun_form": select_adj_form()
					})
			elif request.POST['submit_form'] == 'submitting_adjs':
				on_units_adj = False
				form = select_adj_form(request.POST)
				print(form)
				if form.is_valid():
					selected = form.cleaned_data['selected_adjs']
					print("selected:", selected)
					global adjectives_available
					if adjectives_available == []:
						adjectives_available = all_adjectives
					adjectives_available = selected
				adj_form, gender, case, number = get_random_adj2(adjectives_available)
				return render(request, "first_app/adjectives.html", {
					"form": NounForm(),
					"adj_form" : adj_form,
					"gender": gender,
					"case": case,
					"number": number,
					"unit_form": adjective_unit_form(),
					"noun_form": select_adj_form()
					})
	else:
		print("hello")
		#global units_available
		if units_available_adjectives == []:
			units_available_adjectives = all_adjective_units
		if adjectives_available == []:
			adjectives_available = all_adjective_choices
		if on_units_adj == True:
			adj_form, gender, case, number = get_random_adj(units_available_adjectives)
		else:
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
			"noun_form": select_adj_form()
			})

def participles(request):
	return render(request, "first_app/participles.html")

def index(request):
	return render(request, "first_app/index.html")
