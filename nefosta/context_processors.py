from nefosta.models.contact import Contact
from nefosta.models.link import LinkCategory


def nefosta(request):
    return {
        "link_categories": LinkCategory.objects.all().order_by(
            'title').only('id', 'title'),
        "contact": Contact.objects.first() or {
            "address": "N/A",
            "phone_number": "N/A",
            "email_address": "N/A"
        }
    }
