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

	return render(request, 'listings/listing.html', context)

def search(request):

	filtered_query = Listing.objects.order_by('-list_date')

	keywords = request.GET.get('keywords')
	if keywords:
		filtered_query = filtered_query.filter(description__icontains=keywords)
	
	city = request.GET.get('city')
	if city:
		filtered_query = filtered_query.filter(city__iexact=city)
	
	state = request.GET.get('state')
	if state:
		filtered_query = filtered_query.filter(state__iexact=state)
	
	bedrooms = request.GET.get('bedrooms')
	if bedrooms:
		filtered_query = filtered_query.filter(bedrooms__lte=bedrooms)
	
	price = request.GET.get('price')
	if price:
		filtered_query = filtered_query.filter(price__lte=price)

	context = {
		"bedroom_choices": bedroom_choices,
		"state_choices": state_choices,
		"price_choices": price_choices,
		"listings": filtered_query,
		"values": request.GET
	}

	return render(request, 'listings/search.html', context)