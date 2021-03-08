from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def contact(request):

	if request.method == "POST":

		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send_mail(
		# 	# subject
		# 	message_name,
		# 	message,
		# 	message_email, # from email
		# 	['mike@fsddsfs.com'], # to email
		# 	fail_silently=False,

		# 	)

		# send_mail(
		#     'Subject here',
		#     'Here is the message.',
		#     'from@example.com',
		#     ['to@example.com'],
		#     fail_silently=False,
		# )

		return render(request, 'contact.html', {'message_name':message_name})

	else:
		# return the page

		return render(request, 'contact.html', {})