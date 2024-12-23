from django.shortcuts import render

def unit_converter(request):
    result = None
    unit_type = None
    if request.method == 'POST':
        value = float(request.POST.get('value', 0))
        unit_type = request.POST.get('unit_type')
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Conversion rates and functions for different unit types
        conversion_rates = {
            'length': {
                'meters': {'kilometers': 0.001, 'miles': 0.000621371},
                'kilometers': {'meters': 1000, 'miles': 0.621371},
                'miles': {'meters': 1609.34, 'kilometers': 1.60934},
            },
            'weight': {
                'grams': {'kilograms': 0.001, 'pounds': 0.00220462},
                'kilograms': {'grams': 1000, 'pounds': 2.20462},
                'pounds': {'grams': 453.592, 'kilograms': 0.453592},
            },
            'temperature': {
                # Functions for temperature conversion
                'celsius': {'fahrenheit': lambda x: x * 9/5 + 32, 'kelvin': lambda x: x + 273.15},
                'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15},
                'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32},
            },
            'time': {
                'seconds': {'minutes': 1/60, 'hours': 1/3600},
                'minutes': {'seconds': 60, 'hours': 1/60},
                'hours': {'seconds': 3600, 'minutes': 60},
            },
        }

        # Perform the conversion
        if unit_type in conversion_rates and from_unit in conversion_rates[unit_type]:
            conversion = conversion_rates[unit_type][from_unit].get(to_unit)
            if callable(conversion):  # For temperature conversions
                result = conversion(value)
            elif conversion:  # For standard conversions
                result = value * conversion

    # Units by category
    units_by_type = {
        'length': ['meters', 'kilometers', 'miles'],
        'weight': ['grams', 'kilograms', 'pounds'],
        'temperature': ['celsius', 'fahrenheit', 'kelvin'],
        'time': ['seconds', 'minutes', 'hours'],
    }

    context = {
        'result': result,
        'unit_type': unit_type,
        'units_by_type': units_by_type,
    }
    return render(request, 'converter/unit_converter.html', context)
