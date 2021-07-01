from django.core import paginator
from django.forms.fields import FileField
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
from django.db.models import Q
from app.forms import AnunciosForm
from app.models import Anuncios
from app.calculadora import valorInvestido, calculoAproximadoDeVisualizacoes, cliquesPorVisualizacoes, compartilhamentosPorCliques

def home(request):
    data = {};
    search = request.GET.get("search");
    data_inicio_i = request.GET.get("data_inicio_i");
    data_fim_i = request.GET.get("data_fim_i");
    data_inicio_t = request.GET.get("data_inicio_t");
    data_fim_t = request.GET.get("data_fim_t");
    if search:
        all = Anuncios.objects.filter(nome_cliente__icontains=search);
        paginator = Paginator(all, 100);
        pages = request.GET.get("page");
        data["db"] = paginator.get_page(pages);
    elif data_inicio_i or data_fim_i:
        if data_inicio_i and not data_fim_i:
            data_inicio = parse_date(data_inicio_i);
            all = Anuncios.objects.filter(data_inicio__icontains=data_inicio);
        if data_fim_i and not data_inicio_i:
            data_fim = parse_date(data_fim_i);
            all = Anuncios.objects.filter(data_fim__icontains=data_fim);
        if data_inicio_i and data_fim_i:
            data_inicio = parse_date(data_inicio_i);
            data_fim = parse_date(data_fim_i);
            all = Anuncios.objects.filter(data_inicio__range=[data_inicio, data_fim]);
        paginator = Paginator(all, 100);
        pages = request.GET.get("page");
        data["db"] = paginator.get_page(pages);
    elif data_inicio_t or data_fim_t:
        if data_inicio_t and not data_fim_t:
            data_inicio = parse_date(data_inicio_t);
            all = Anuncios.objects.filter(data_inicio__icontains=data_inicio);
        if data_fim_t and not data_inicio_t:
            data_fim = parse_date(data_fim_t);
            all = Anuncios.objects.filter(data_fim__icontains=data_fim);
        if data_inicio_t and data_fim_t:
            data_inicio = parse_date(data_inicio_t);
            data_fim = parse_date(data_fim_t);
            all = Anuncios.objects.filter(data_fim__range=[data_inicio, data_fim]);
        paginator = Paginator(all, 100);
        pages = request.GET.get("page");
        data["db"] = paginator.get_page(pages);
    else:
        all = Anuncios.objects.all();
        paginator = Paginator(all, 10);
        pages = request.GET.get("page");
        data["db"] = paginator.get_page(pages);
    return render(request, "index.html", data);

def form(request):
    data = {};
    data['form'] = AnunciosForm();
    return render(request, "form.html", data);

def create(request):
    form = AnunciosForm(request.POST or None);
    if request.method == "POST":
        if form.is_valid():
            nome_anuncio = form.cleaned_data["nome_anuncio"];
            nome_cliente = form.cleaned_data["nome_cliente"];
            data_inicio = form.cleaned_data["data_inicio"];
            data_fim = form.cleaned_data["data_fim"];
            investimento_dia = form.cleaned_data["investimento_dia"];
            data = Anuncios();
            data.nome_anuncio = nome_anuncio;
            data.nome_cliente = nome_cliente;
            data.data_inicio = data_inicio;
            data.data_fim = data_fim;
            data.investimento_dia = investimento_dia;
            data.save();
            return redirect("home");

def view(request, pk):
    data = {};
    data["db"] = Anuncios.objects.get(pk=pk);
    data["db"].valor_investido = valorInvestido(data["db"].data_inicio, data["db"].data_fim, data["db"].investimento_dia);
    data["db"].qnt_max_view = int(calculoAproximadoDeVisualizacoes(float(data["db"].valor_investido)));
    data["db"].qnt_max_click = int(cliquesPorVisualizacoes(float(data["db"].qnt_max_view)));
    data["db"].qnt_max_share = int(compartilhamentosPorCliques(float(data["db"].qnt_max_click)));
    return render(request, "view.html", data);

def edit(request, pk):
    data = {};
    data["db"] = Anuncios.objects.get(pk=pk);
    data["form"] = AnunciosForm(initial={"nome_anuncio":data["db"].nome_anuncio,
                                        "nome_cliente":data["db"].nome_cliente,
                                        "data_inicio":data["db"].data_inicio,
                                        "data_fim":data["db"].data_fim,
                                        "investimento_dia":data["db"].investimento_dia});
    return render(request, "form.html", data);

def update(request, pk):
    data = {};
    data["db"] = Anuncios.objects.get(pk=pk);
    form = AnunciosForm(request.POST or None, initial={"nome_anuncio":data["db"].nome_anuncio,
                                                        "nome_cliente":data["db"].nome_cliente,
                                                        "data_inicio":data["db"].data_inicio,
                                                        "data_fim":data["db"].data_fim,
                                                        "investimento_dia":data["db"].investimento_dia});
    if request.method == "POST":
        if form.is_valid():
            nome_anuncio = form.cleaned_data["nome_anuncio"];
            nome_cliente = form.cleaned_data["nome_cliente"];
            data_inicio = form.cleaned_data["data_inicio"];
            data_fim = form.cleaned_data["data_fim"];
            investimento_dia = form.cleaned_data["investimento_dia"];
            data = Anuncios();
            data.id = pk;
            data.nome_anuncio = nome_anuncio;
            data.nome_cliente = nome_cliente;
            data.data_inicio = data_inicio;
            data.data_fim = data_fim;
            data.investimento_dia = investimento_dia;
            data.save();
            return redirect("home");

def delete(request, pk):
    db = Anuncios.objects.get(pk=pk);
    db.delete();
    return redirect("home");