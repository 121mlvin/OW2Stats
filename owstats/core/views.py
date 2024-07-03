from django.shortcuts import render, redirect
from django.views import View
import requests
from .utils import get_random_character


class MainPageView(View):
    template_name = 'main_page.html'

    def get(self, request):
        context = self.get_random_characters()
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}

        battle_tag = request.POST.get('battle_tag')
        response = requests.get(f'https://overfast-api.tekrop.fr/players/{battle_tag}/stats/summary')

        if response.status_code == 200:
            return redirect('profile_search', battle_tag=battle_tag)
        else:
            context['error'] = 'Could not retrieve statistics. Please check the battle tag and try again.'

        context.update(self.get_random_characters())
        return render(request, self.template_name, context)

    def get_random_characters(self):
        character1 = get_random_character()
        character2 = get_random_character()

        response_character1 = requests.get(f'https://overfast-api.tekrop.fr/heroes/{character1}')
        response_character2 = requests.get(f'https://overfast-api.tekrop.fr/heroes/{character2}')

        context = {}

        if response_character1.status_code == 200 and response_character2.status_code == 200:
            character1_data = response_character1.json()
            character2_data = response_character2.json()

            context.update({
                'character1_name': character1_data.get('name', 'Character name not available'),
                'character1_age': character1_data.get('age', 'Character age not available'),
                'character1_image': character1_data.get('portrait', ''),
                'character2_name': character2_data.get('name', 'Character name not available'),
                'character2_age': character2_data.get('age', 'Character age not available'),
                'character2_image': character2_data.get('portrait', ''),
            })
        else:
            context['error'] = 'Could not retrieve character information.'

        return context


class ProfileSearchView(View):
    template_name = 'profile_search.html'

    def get(self, request, battle_tag):
        response = requests.get(f'https://overfast-api.tekrop.fr/players/{battle_tag}/summary')
        if response.status_code == 200:
            player_summary = response.json()
            context = {'player_summary': player_summary, 'battle_tag': battle_tag}
        else:
            context = {'error': 'Could not retrieve summary. Please check the battle tag and try again.'}
        return render(request, self.template_name, context)


class ProfileStatsView(View):
    template_name = 'profile_stats.html'

    def get(self, request, battle_tag):
        response = requests.get(f'https://overfast-api.tekrop.fr/players/{battle_tag}/stats/summary')
        if response.status_code == 200:
            player_stats = response.json()
            context = {'player_stats': player_stats, 'battle_tag': battle_tag}
        else:
            context = {'error': 'Could not retrieve statistics. Please check the battle tag and try again.'}
        return render(request, self.template_name, context)
