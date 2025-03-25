from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit

def voucher_html(request):
    # Пример данных, которые можно заменить на реальные из вашей базы или формы
    context = {
        'company_name': 'ООО "АВИАСЕЙЛС БИЗНЕС"',
        'company_tax_id': '4953332211',
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
            'guest_name': 'ROSTRIGIN PAVEL',
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
        'company_name': 'ООО "АВИАСЕЙЛС БИЗНЕС"',
        'company_tax_id': '4953332211',
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
            'guest_name': 'ROSTRIGIN PAVEL',
            'meal_info': 'Завтрак включён',
            'price': '6349,00 ₽',
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