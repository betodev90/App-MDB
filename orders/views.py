from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages

from .forms import ModelFormClient, SimpleFormClient
from .models import Client

# Apartado de VBF ( Vista Basadas en Función )

@login_required(login_url='users/login')
def create_client(request):
    """Vista vasada en funcion para crear un nuevo objeto Client"""
    form = SimpleFormClient()  # Declaracion del formulario
    if request.method == 'POST':
        form = SimpleFormClient(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Client.objects.create(
                dni=data.get('dni'), first_name=data.get('first_name'), 
                last_name=data.get("last_name"),
            )
            # Nueva Alternativa para crear un nuevo objeto Estudiante
            # client = Client()
            # client.dni = data.get('dni')
            # client.first_name = data.get('first_name')
            # client.las_name = data.get('las_name')
            # estudiante.save()
            messages.success(request, "Se ha creado exitosamente un cliente")
            return redirect('orders:clients')
        else:
            # Forma para acceder a los mensajes de error que generamos en el clean_data (validacion de formularios)
            lista_errores = "Por favor verifique los siguientes campos: "
            for i in form.errors:
                lista_errores = lista_errores + i + ", "
            if form.errors:
                messages.error(request, lista_errores[0:-2])
            for i in form:
                if i.errors:
                    i.field.widget.attrs['class'] = 'danger'
    return render(request, 'orders/form.html', {'form': form})


@login_required(login_url='users/login')
def edit_client(request, pk):
    """Vista Basada en Funcion para Editar la informacion de un objeto estudiante"""
    client = Client.objects.get(pk=pk)
    form = SimpleFormClient(initial={
        'dni': client.dni,
        'first_name': client.first_name,
        'last_name': client.last_name,
    })
    if request.method == 'POST':
        form = SimpleFormClient(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            client.dni = data.get('dni')
            client.first_name = data.get('first_name')
            client.last_name = data.get('last_name')
            client.save()
            messages.success(request, "Se realizo el cambio exitosamente")
            return redirect("orders:clients")
        else:
            messages.error(request, "Error al editar la información")
    return render(request, 'orders/form.html', {'form': form})


@login_required(login_url='users/login')
def delete_client(request, pk):
    Client.objects.filter(pk=pk).delete()
    messages.info(request, "El cliente ha sido eliminado")
    return redirect("orders:clients")

@login_required(login_url='users/login')
def detail_client(request, pk):
    """Obtiene el objeto a mostrar informacion en detalle le envia por parametro el pk (identificador único de un objeto)"""
    try:
        # Obtiene el objeto Estudiante haciendo la consulta mediante el metodo get(pk=pk)
        client = Client.objects.get(pk=pk)
        return render(request, 'orders/detail_client.html', context={'object': client})
    except Client.DoesNotExist:  # Manejo de Excepcion si no encuentra el objecto, similar al Try catch de Java
        # Si ingresa a este bloque es porque accedió a la excepcion, es decir no encontró al objecto con ese
        # pk enviando en la vista.
        messages.error(
            request, "El cliente seleccionado no se encuentra en el sistema, favor verifique con el admin"
        )
        return redirect('orders: clients')


@login_required(login_url='users/login')
def list_client(request):
    """"""
    q = request.GET.get('q', '')
    querys = (Q(dni__icontains=q) | Q(last_name__icontains=q))
    clients = Client.objects.filter(querys)
    page = request.GET.get('page', 1)
    paginator = Paginator(clients, 10)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request, 'orders/list_client.html', context={'clients': clients})


# Apartado de VBC ( Vista Basadas en clase )

class ListClientView(LoginRequiredMixin, ListView):
    """Vista Basda en Clase , controlador de Django para listar objetos de la clase Estudiante
        NOTA: Realiza el mismo proceso que la vista 'lista_estudiantes'
    """
    model = Client
    # Redirect al login si al intentar acceder a esta vista no esta ha hecho login
    login_url = reverse_lazy('login')
    # Template a utilizar para renderizar
    template_name = 'orders/list_client.html'
    # Le indica que nombre lo va a llamar desde el template si no asignamos el atributo 'context_object_name' asume
    # que en el template tiene que estar la variable {{ object_list }}
    context_object_name = 'clients'
    # Query consulta filtrado
    # queryset = ''
    # Indica cuando se quiere aplicar paginacion
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        # parametros de filtro | busqueda
        querys = (Q(dni__icontains=q) | Q(last_name__icontains=q))
        object_list = Client.objects.filter(querys)
        return object_list

    def get_context_data(self, **kwargs):
        ctx = super(ListClientView, self).get_context_data(**kwargs)
        page = ctx['page_obj']
        paginator = ctx['paginator']
        ctx['page_is_first'] = (page.number == 1)
        ctx['page_is_last'] = (page.number == paginator.num_pages)
        return ctx

class CreateClientView(LoginRequiredMixin, CreateView):
    """Vista Basda en Clase , controlador de Django para crear un nuevo objeto estudiante"""
    # Model del objeto que va a crear la vista
    model = Client
    # Redirect al login si al intentar acceder a esta vista no esta ha hecho login
    login_url = reverse_lazy('login')
    # Indica el template a renderizar
    template_name = 'orders/form.html'
    # Mapea los campos del model Estudiantes y los crea como formulario IMPORTANTE en el template que utilizamos debe
    # nombrar el formulario en el HTML como "{{ form }} "
    fields = ['dni', 'first_name', 'last_name']
    # metodo reverse_lazy(<url_name>) para que redireccione una vez agregue el objeto estudiante
    success_url = reverse_lazy('odres: clients')

class DetailClientView(DetailView):
    model = Client
    template_name = 'orders/detail_client.html'
