from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render
from .models import (
    Painting,
    WorkOnPaper,
    Exhibition,
    ExhibitionCategory,
    Education,
    Residency,
    Fair,
    GroupExhibition,
    PersonalExhibition,
    TextsPublications
)

# Home Page View
def index(request):
    return render(request, 'gallery/index.html')


# Paintings Gallery View
def paintings(request):
    paintings = Painting.objects.all()
    return render(request, 'gallery/paintings.html', {'paintings': paintings})



# Works on Paper Gallery View
def works_on_paper(request):
    works = WorkOnPaper.objects.all()
    return render(request, 'gallery/works-on-paper.html', {'works': works})



# Exhibition Views with Location Filtering
def exhibitions_view(request):
    category_id = request.GET.get('category')  # Get the selected category ID from the request
    categories = ExhibitionCategory.objects.all()  # Get all categories for the filter list

    if category_id:
        exhibitions = Exhibition.objects.filter(location__id=category_id).prefetch_related('images')
    else:
        exhibitions = Exhibition.objects.prefetch_related('images')  # Show all exhibitions if no category is selected

    return render(request, 'gallery/exhibition-views.html', {
        'categories': categories,
        'exhibitions': exhibitions,
        'selected_category': category_id,
    })



# Bio Page View
def bio(request):
    education = Education.objects.all()
    residencies = Residency.objects.all()
    fairs = Fair.objects.all()
    group_exhibitions = GroupExhibition.objects.all()
    personal_exhibitions = PersonalExhibition.objects.all()

    return render(request, 'gallery/bio.html', {
        'education': education,
        'residencies': residencies,
        'fairs': fairs,
        'group_exhibitions': group_exhibitions,
        'personal_exhibitions': personal_exhibitions
    })
def texts_publications_en(request):
    texts_publications = TextsPublications.objects.all()
    return render(request, 'gallery/texts-publications.html', {'texts_publications': texts_publications})


def texts_publications_fr(request):
    texts_publications = TextsPublications.objects.all()
    return render(request, 'gallery/texts-publications-fr.html', {'texts_publications': texts_publications})


def video(request):
    return render(request, 'gallery/video.html')

def coming_soon(request):
    return render(request, 'gallery/coming-soon-news.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose the email content
        subject = f"Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send the email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],  # Replace with your email or admin email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again.")

    return render(request, 'gallery/contact.html')