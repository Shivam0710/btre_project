from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
	if request.method == "POST":
		user_id = request.POST.get('user_id', '')
		realtor_email = request.POST.get('realtor_email', '')
		listing_id = request.POST.get('listing_id', '')
		listing = request.POST.get('listing', '')
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		phone = request.POST.get('phone', '')
		message = request.POST.get('message', '')

		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
			if has_contacted:
				messages.error(request, "You have already made an enquiry to this property")
				return redirect("/listings/{0}".format(listing_id))

		contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
		contact.save()

		# send_mail(
		# 	"Property Listing Inquiry",
		# 	"Hey you have got a query for. You can see it by logging into admin panel.",
		# 	"shivamsagar888@gmail.com",
		# 	[realtor_email, "shivam.sagar@magicpin.in"],
		# 	fail_silently=False
		# )

		messages.success(request, "We have successfully recieved your request. We will confirm you soon.")

	return redirect('/listings/{0}'.format(listing_id))