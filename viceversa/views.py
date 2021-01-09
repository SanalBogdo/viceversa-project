from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	word_text = user_text.split()
	number_of_words = len(word_text)
	reverse_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reverstext':reverse_text,
		'number_of_words': number_of_words})