from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Pokemones
import pokebase as pb


class HomePageView(ListView):
    """ This is the home class. 
    In this class, connection is made with the api of the pokemon 
    to extract them and save them in the database. 
    Only the first 50 Pokemon are drawn for speed."""

    template_name = "home.html"

    context_object_name = "po"
    def get_queryset(self):
        
        for i in range(1,50):
            poke = pb.evolution_chain(i)
            Pokemones.objects.get_or_create(name=poke.chain.species.name, 
            evolution = poke.chain.evolves_to[0].species.name, poke_id=i,
            min_level = poke.chain.evolves_to[0].evolution_details[0].min_level,
            needs_overworld_rain = poke.chain.evolves_to[0].evolution_details[0].needs_overworld_rain,
            turn_upside_down = poke.chain.evolves_to[0].evolution_details[0].turn_upside_down)
            
        return Pokemones.objects.all()

            
            
            

class EvolutionChange(ListView):
    """This is the evolution class. 
    In this class, a request is made for the pokemon by ID 
    that have been saved in the database and then displayed.
    Note that in this view we do not use the pokemon api but 
    the data from the database."""

    template_name = "evolution.html"
    context_object_name = "pokemon"
    model = Pokemones
    
    def get_queryset(self):
        name = self.kwargs["name"]
        pok = Pokemones.objects.get(name=name)
        return pok
    
    

class PokemonInfo(ListView):
    """
    This is the kind of information of the pokemon.
    In this view, information is extracted from a pokemon 
    by its ID by making a query in the pokemon api.
    Notice that the information is extracted and then 
    returned and displayed in the html
    """


    template_name = "inform.html"
    context_object_name = "pokemon"

    def get_queryset(self):
        id = self.kwargs["id"]
        ec = pb.evolution_chain(int(id))
        name = ec.chain.species.name
        poke = pb.pokemon(str(name))
        height = poke.height
        weight = poke.weight
        name = poke.name
        id_p = poke.id
        base_stats = [poke.stats[0].__dict__,poke.stats[1].__dict__, poke.stats[2].__dict__,
                      poke.stats[3].__dict__,poke.stats[4].__dict__, poke.stats[5].__dict__]
        evolution = ec.chain.evolves_to[0].species.name
        a = {"name": name, "height":height,"weight":weight,  "id":id_p,"base_stats":base_stats, "evolution":evolution }
        return a
    
