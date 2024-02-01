from django.shortcuts import render

def index(request):
    resultado = None
    if request.method == 'POST':
        tempo_str = request.POST.get('tempo')
        horas, minutos = map(int, tempo_str.split(':'))
        fracao_horas = horas + minutos / 60
        resultado = f"O tempo em fração de horas é: {fracao_horas:.2f}"

    return render(request, 'index.html', {'resultado': resultado})
