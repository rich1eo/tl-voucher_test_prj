from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit

def voucher_html(request):
    # Пример данных, которые можно заменить на реальные из вашей базы или формы
    context = {
        'voucher': {
            'internal_booking_number': 'ee8e2cd1-a5f9-4472-9a1d-3d85019d84b8',
            'booking_number': '227075106',
            'booking_date': '25.03.2025',
            'hotel_name': 'Гостиница Заречная',
            'hotel_address': '603076, проспект Ленина, д. 36, Нижний Новгород',
            'hotel_phone': '+79200774940',
            'checkin_date': '25.03.2025',
            'checkin_time': '14:00',
            'checkout_date': '26.03.2025',
            'checkout_time': '12:00',
            'room_type': 'Двухместный номер Стандарт (двуспальная кровать)',
            'bed_type': 'Двуспальная кровать',
            'guests': ["Иван Иванов", "Петр Петров"],
            'hotel_image_url': 'https://media.istockphoto.com/id/104731717/photo/luxury-resort.jpg?s=612x612&w=0&k=20&c=cODMSPbYyrn1FHake1xYz9M8r15iOfGz9Aosy9Db7mI=',
            'meal_info': 'Завтрак включён',
            'price': '6349,00 ₽',
            'vat': 'Без НДС',
            'additional_contact': 'Гостиница Заречная',
            'gps': '56.284943 43.929684'
        }
    }
    return render(request, 'voucher/voucher_template.html', context)

def voucher_pdf(request):
    context = {
        'voucher': {
            'internal_booking_number': 'ee8e2cd1-a5f9-4472-9a1d-3d85019d84b8',
            'booking_number': '227075106',
            'booking_date': '25.03.2025',
            'hotel_name': 'Гостиница Заречная',
            'hotel_address': '603076, проспект Ленина, д. 36, Нижний Новгород',
            'hotel_phone': '+79200774940',
            'checkin_date': '25.03.2025',
            'checkin_time': '14:00',
            'checkout_date': '26.03.2025',
            'checkout_time': '12:00',
            'room_type': 'Двухместный номер Стандарт (двуспальная кровать)',
            'bed_type': 'Двуспальная кровать',
            'guests': ["Иван Иванов", "Петр Петров"],
            'hotel_image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnHFyGj0c1K-Mk106ZGT-juvcp-4Z8aMocHw&s',
            'meal_info': 'Завтрак включён',
            'price': '6349,00',
            'vat': 'Без НДС',
            'additional_contact': 'Гостиница Заречная',
            'gps': '56.284943 43.929684'
        }
    }
    # Рендерим HTML в строку
    html_string = render_to_string('voucher/voucher_template.html', context)
    # Генерация PDF из строки HTML (параметр False возвращает PDF в виде байтовой строки)
    pdf = pdfkit.from_string(html_string, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="voucher.pdf"'
    return response