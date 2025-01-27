import os
import django
import sys
from io import BytesIO
import requests
from django.core.files import File
from django.contrib.auth.models import User
from pokeapp.models import Card

# Configurar o ambiente Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 2)[0])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pokemonologia.settings")
django.setup()

# Criar o usuário admin
admin_user, created = User.objects.get_or_create(
    username="admin", defaults={"is_superuser": True, "is_staff": True}
)
if created:
    admin_user.set_password("admin")
    admin_user.save()
    print("Usuário admin criado com sucesso!")
else:
    print("Usuário admin já existe.")

# Função para baixar a imagem e adicionar Pokémon
def adicionar_pokemons():
    pokemons = [
    ("Rillaboom", "Grass", 100, 120, 90, "Um Pokémon de ritmo poderoso, conhecido por criar sons hipnotizantes enquanto luta. Seu tambor invoca a força da natureza."),
    ("Incineroar", "Fire", 95, 115, 90, "Com um coração de lutador e alma de um showman, Incineroar encanta e intimida com seu estilo de combate ardente."),
    ("Kyogre", "Water", 100, 150, 90, "Uma entidade lendária que controla os mares. Seu poder pode criar tempestades que inundam o mundo."),
    ("Miraidon", "Electric", 100, 120, 90, "Um Pokémon futurista que parece vindo de outra dimensão. Seu corpo irradia eletricidade avançada."),
    ("Volcarona", "Bug", 85, 135, 105, "O sol vivo para muitos, sua dança ardente transforma qualquer campo de batalha em um espetáculo infernal."),
    ("Tornadus", "Flying", 100, 125, 90, "Mestre dos ventos, Tornadus voa a velocidades incríveis, criando tempestades que varrem tudo em seu caminho."),
    ("Terapagos", "Normal", 100, 85, 75, "Uma criatura mística com uma conexão única com a natureza. Suas escamas brilham como cristais preciosos."),
    ("Urshifu", "Fighting", 100, 130, 90, "Um guerreiro disciplinado que nunca recua. Seus golpes são rápidos e implacáveis, como um mestre de artes marciais."),
    ("Salazzle", "Poison", 68, 64, 60, "Um Pokémon venenoso sedutor que manipula outros com suas feromônios tóxicos e ataques traiçoeiros."),
    ("Calyrex", "Ghost", 100, 130, 85, "Um rei do além, Calyrex controla espíritos com uma graça arrepiante e poder espiritual incomparável."),
    ("Chi-Yu", "Dark", 100, 120, 85, "Guardião sombrio, Chi-Yu absorve energia das chamas, envolvendo-se em mistérios e segredos profundos."),
    ("Farigiraf", "Psychic", 90, 100, 70, "Uma fusão psíquica única, sua mente é uma fortaleza protegida por habilidades defensivas e ofensivas."),
    ("Zamazenta", "Steel", 100, 135, 115, "Um cavaleiro lendário que defende a justiça. Seu escudo indestrutível é uma lenda por si só."),
    ("Ogerpon", "Rock", 100, 120, 90, "Uma força da montanha, Ogerpon guarda tesouros ancestrais e luta com a força de eras passadas."),
    ("Ursaluna", "Ground", 130, 140, 90, "Um gigante da terra, suas pisadas fazem o chão tremer. É temido e respeitado por onde passa."),
    ("Calyrex", "Ice", 100, 130, 85, "Um soberano gélido que congela qualquer obstáculo em seu caminho. Elegante e impiedoso em batalha."),
    ("Raging Bolt", "Dragon", 100, 150, 85, "O trovão encarnado, este dragão carrega a fúria de tempestades antigas, liberando energia bruta."),
    ("Flutter Mane", "Fairy", 55, 135, 90, "Uma criatura etérea que flutua como um sonho. Sua presença é tão linda quanto assustadora.")
]

    def baixar_imagem(nome_pokemon):
        url = f"https://img.pokemondb.net/artwork/avif/{nome_pokemon.lower()}.avif"
        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            imagem = BytesIO(resposta.content)
            return File(imagem, name=f"{nome_pokemon.lower()}.avif")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem de {nome_pokemon}: {e}")
            return None

    for nome, classe, hp, ataque, defesa, descricao in pokemons:
        if not Card.objects.filter(nome=nome).exists():
            imagem = baixar_imagem(nome)
            if imagem:
                card = Card(
                    nome=nome,
                    classe=classe.capitalize(),
                    hp=hp,
                    ataque=ataque,
                    defesa=defesa,
                    descricao=descricao,
                    foto=imagem,
                    user=admin_user
                )
                card.save()
                print(f"{nome} adicionado com sucesso!")
            else:
                print(f"Imagem para {nome} não foi adicionada.")
        else:
            print(f"{nome} já existe no banco de dados.")

# Executar a função
adicionar_pokemons()
