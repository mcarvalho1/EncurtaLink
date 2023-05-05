from django.shortcuts import render
from encurtador.models import EncurtadorModel
from django.shortcuts import redirect
import string
import random

# Create your views here.

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        dados = request.POST # Dados do request, quando aperta submit. Fazendo request post

        link_longo = dados.get("link") # Link original colocado no form

        uid_random = self.random_id(5) # Id gerado para apos slug
        id_req = dados.get("id_request")
        id_final = f"{uid_random}"

        novo_dado = EncurtadorModel()
        novo_dado.link = link_longo
        novo_dado.uid = id_final
        novo_dado.save()

        return render(request, self.template_name, {
            'UID': request.build_absolute_uri(f'c/{id_final}')
        })

    def random_id (self, length):
        """Generates a random string of alphanumeric characters with the given length."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

def encurtado_link(request, uid):
    try: 
        dado = EncurtadorModel.objects.get(uid=uid)
        external_url = dado.link
        return redirect(external_url)
    except:
        return redirect('/home')

