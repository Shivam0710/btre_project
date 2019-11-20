from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing
from .choices import bedroom_choices, state_choices, price_choices

# Create your views here.
def index(request):

	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listings, 6)
	page_number = request.GET.get('page')
	filtered_pages = paginator.get_page(page_number)

	context = {
		'listings': filtered_pages,
	}
	return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

	listing = get_object_or_404(Listing, pk=listing_id)
	context = {
		"listing": listing
	}
	print(context)

	return render(request, 'listings/listing.html', context)

def search(request):

	context = {
		"bedroom_choices": bedroom_choices,
		"state_choices": state_choices,
		"price_choices": price_choices
	}

	return render(request, 'listings/search.html', context)