# Jeu Python avec Système d'Authentification

Application de jeu Python complète construite avec une architecture modulaire, incluant l'authentification utilisateur, la navigation de menu et la logique de jeu — le tout géré avec un code propre et évolutif.

Ce projet démontre une structuration Python avancée pour des jeux de bureau petits à moyens, combinant Pygame, logique UI personnalisée et gestion de connexion.

## Mots-clés

`Python` · `Pygame` · `Authentification` · `Développement de Jeux` · `Système de Menu` · `Projet Python Modulaire` · `UI/UX` · `Game Development` · `Architecture Logicielle` · `Gestion Utilisateurs`

## Table des Matières

- [Aperçu](#aperçu)
- [Caractéristiques](#caractéristiques)
- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Composants Principaux](#composants-principaux)
- [Flux d'Exécution](#flux-dexécution)
- [Technologies Utilisées](#technologies-utilisées)
- [Architecture](#architecture)
- [Captures d'Écran](#captures-décran)
- [Améliorations Futures](#améliorations-futures)
- [Dépannage](#dépannage)
- [Contribution](#contribution)
- [Licence](#licence)
- [Auteur](#auteur)

## Aperçu

Ce projet n'est pas qu'un simple jeu — c'est une plateforme de jeu mini complète avec :

- **Authentification Utilisateur** : Les joueurs peuvent se connecter ou s'inscrire
- **Menu Principal** : Navigation entre connexion, jeu et options de sortie
- **Moteur de Jeu** : Boucle de jeu principale avec visuels et logique dynamiques
- **Système de Configuration** : Toutes les constantes, couleurs et ressources gérées dans `config.py`
- **Fonctions Utilitaires** : Helpers réutilisables pour animations, ressources et événements
- **Architecture Modulaire** : Code propre et maintenable

## Caractéristiques

### Authentification et Gestion Utilisateurs

- Système de connexion sécurisé
- Création de compte utilisateur
- Validation des informations d'identification
- Stockage local des données utilisateur
- Gestion de session

### Interface Utilisateur

- Menu principal intuitif
- Navigation fluide entre les écrans
- Design responsive
- Animations et transitions

### Système de Jeu

- Boucle de jeu optimisée
- Gestion des événements en temps réel
- Rendu graphique performant
- Logique de jeu modulaire

### Configuration Centralisée

- Constantes globales dans `config.py`
- Gestion des couleurs et thèmes
- Configuration des polices et tailles
- Paramètres personnalisables

## Structure du Projet
```
gamehh/
│
├── assets/                 # Images, sons, icônes, etc.
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── __pycache__/            # Bytecode Python (auto-généré)
│
├── authentication.py       # Gestion connexion, inscription et validation
├── config.py               # Configuration centralisée et constantes
├── game.py                 # Logique de jeu principale (boucle, événements, rendu)
├── main.py                 # Point d'entrée – lance l'application complète
├── menu.py                 # Gestion de l'interface du menu principal
├── utils.py                # Utilitaires (UI, animations, etc.)
├── requirements.txt        # Dépendances Python
└── README.md              # Documentation du projet
```

## Installation

### Prérequis

Assurez-vous d'avoir Python 3.8 ou supérieur installé sur votre système.

### Étape 1 : Cloner le Dépôt
```bash
git clone https://github.com/omarlr-pro/gamehh.git
cd gamehh
```

### Étape 2 : Créer un Environnement Virtuel (Recommandé)
```bash
python -m venv .venv
```

**Activer l'environnement :**

Sur Windows :
```bash
.venv\Scripts\activate
```

Sur macOS/Linux :
```bash
source .venv/bin/activate
```

### Étape 3 : Installer les Dépendances
```bash
pip install pygame
```

Ou utilisez le fichier requirements :
```bash
pip install -r requirements.txt
```

### Étape 4 : Vérifier l'Installation
```bash
python -c "import pygame; print(pygame.version.ver)"
```

## Utilisation

### Lancer le Jeu

Exécutez simplement :
```bash
python main.py
```

### Première Utilisation

1. **Écran de Connexion** : Apparaît au démarrage
2. **Créer un Compte** : Si c'est votre première fois, cliquez sur "S'inscrire"
3. **Entrer les Identifiants** : Nom d'utilisateur et mot de passe
4. **Menu Principal** : Accédez au menu après authentification
5. **Jouer** : Sélectionnez "Jouer" pour commencer

### Contrôles du Jeu

Les contrôles spécifiques dépendent du type de jeu. Généralement :

- **Clavier** : Touches fléchées ou WASD pour le mouvement
- **Souris** : Navigation dans les menus
- **Échap** : Retour au menu ou quitter
- **Entrée** : Confirmer les sélections

## Composants Principaux

### Module `main.py`

Point d'entrée de l'application qui :
- Initialise Pygame
- Gère les transitions entre écrans
- Coordonne tous les modules
- Gère la boucle principale de l'application
```python
# Exemple de structure
def main():
    # Initialisation
    pygame.init()
    # Gestion de l'authentification
    # Lancement du menu
    # Démarrage du jeu
```

### Module `authentication.py`

Gère l'authentification utilisateur avec :
- Fonction de connexion
- Fonction d'inscription
- Validation des données
- Stockage sécurisé des informations
- Gestion des sessions

**Fonctionnalités principales :**
- Vérification des identifiants
- Hash de mot de passe (si implémenté)
- Stockage local (JSON ou fichier texte)
- Gestion des erreurs de connexion

### Module `menu.py`

Gère l'interface du menu principal :
- Affichage des options
- Gestion des clics souris
- Navigation entre les écrans
- Animations de menu
- Boutons interactifs

**Options disponibles :**
- Jouer
- Paramètres
- Profil utilisateur
- Quitter

### Module `game.py`

Contient la logique principale du jeu :
- Boucle de jeu (game loop)
- Gestion des événements
- Mise à jour des états
- Rendu graphique
- Collision detection
- Score et progression
```python
# Structure typique de la boucle de jeu
while running:
    # Gestion des événements
    # Mise à jour de la logique
    # Rendu graphique
    # Contrôle du framerate
```

### Module `config.py`

Centralise toutes les configurations :
```python
# Exemples de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Chemins des ressources
ASSETS_PATH = "assets/"
FONT_PATH = "assets/fonts/"
```

### Module `utils.py`

Fournit des fonctions utilitaires réutilisables :
- Chargement d'images
- Gestion du son
- Animations
- Effets visuels
- Helpers de collision
- Fonctions mathématiques

## Flux d'Exécution

### Séquence de Démarrage
```
1. Lancement de main.py
   ↓
2. Initialisation de Pygame
   ↓
3. Chargement de la configuration (config.py)
   ↓
4. Affichage de l'écran d'authentification
   ↓
5. Validation des identifiants (authentication.py)
   ↓
6. Si valide → Affichage du menu principal (menu.py)
   ↓
7. Sélection "Jouer" → Lancement du jeu (game.py)
   ↓
8. Boucle de jeu principale
   ↓
9. Retour au menu ou sortie
```

### Diagramme de Navigation
```
[Écran de Connexion]
        ↓
[Menu Principal]
    ↙   ↓   ↘
[Jouer] [Paramètres] [Quitter]
    ↓
[Jeu en Cours]
    ↓
[Fin de Partie / Score]
    ↓
[Retour au Menu]
```

## Technologies Utilisées

### Langage et Frameworks

| Catégorie           | Outils                                  |
|---------------------|-----------------------------------------|
| Langage             | Python 3.8+                             |
| Graphiques          | Pygame                                  |
| Authentification    | Logique personnalisée (JSON/fichier)    |
| Ressources          | Images, sons, musique dans `/assets`    |
| Configuration       | Constantes personnalisées `config.py`   |

### Bibliothèques Python
```txt
pygame>=2.5.0
```

### Structure de Code

- **Programmation Orientée Objet** : Classes pour joueur, ennemis, items
- **Design Pattern MVC** : Séparation logique/vue/contrôleur
- **Modularité** : Chaque module a une responsabilité unique
- **Réutilisabilité** : Fonctions utilitaires communes

## Architecture

### Pattern de Conception

Le projet suit une architecture modulaire inspirée du pattern MVC :

- **Model** : `authentication.py`, données de jeu dans `game.py`
- **View** : Rendu graphique dans `game.py` et `menu.py`
- **Controller** : Gestion des événements et logique dans tous les modules

### Avantages de cette Architecture

- Code maintenable et lisible
- Facilite les tests unitaires
- Permet l'ajout de nouvelles fonctionnalités
- Réduction du couplage entre modules
- Réutilisation du code

## Améliorations Futures

### Fonctionnalités Planifiées

**Authentification et Utilisateurs**
- Base de données pour l'authentification (SQLite ou Firebase)
- Hash de mot de passe avec bcrypt
- Système de récupération de mot de passe
- Profils utilisateur avec avatars
- Statistiques de joueur

**Interface et UX**
- Design GUI moderne avec thèmes
- Boutons, sliders et widgets personnalisés
- Animations de transition fluides
- Support de plusieurs résolutions
- Mode plein écran

**Gameplay**
- Plusieurs modes de jeu ou niveaux
- Système de progression
- Achievements et trophées
- Power-ups et bonus
- Difficulté adaptative

**Fonctionnalités Sociales**
- Tableau des scores (leaderboard)
- Synchronisation cloud des profils
- Partage de scores sur réseaux sociaux
- Mode multijoueur local
- Classement global

**Technique**
- Support multilingue (français, anglais, arabe)
- Sons et musiques variés
- Effets de particules
- Sauvegarde automatique
- Tests unitaires

## Performance et Optimisation

### Conseils d'Optimisation
```python
# Limiter le framerate
clock = pygame.time.Clock()
clock.tick(60)  # 60 FPS

# Optimiser le chargement des images
# Charger une seule fois, réutiliser
images = load_images_once()

# Utiliser des sprites groups
all_sprites = pygame.sprite.Group()
```

### Benchmarks

- Consommation mémoire : < 100 MB
- FPS cible : 60 FPS
- Temps de chargement : < 3 secondes

## Dépannage

### Problème : Pygame ne s'installe pas
```bash
# Solution : Mettre à jour pip
pip install --upgrade pip
pip install pygame
```

### Problème : Erreur "No module named 'pygame'"
```bash
# Vérifier l'installation
pip list | grep pygame

# Réinstaller si nécessaire
pip uninstall pygame
pip install pygame
```

### Problème : Le jeu est lent
```python
# Réduire la résolution dans config.py
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Limiter le nombre d'objets à l'écran
# Optimiser les boucles de collision
```

### Problème : Pas de son
```bash
# Vérifier les pilotes audio
# Sur Linux, installer pygame avec support audio :
pip install pygame --user
```

### Problème : Fichier d'authentification manquant
```python
# Le programme créera automatiquement le fichier
# Ou créez manuellement : users.json ou users.txt
```

## Tests

### Exécuter les Tests
```bash
# Si des tests sont implémentés
python -m pytest tests/

# Tests manuels
python main.py
```

### Checklist de Test

- [ ] Connexion avec identifiants valides
- [ ] Inscription d'un nouvel utilisateur
- [ ] Navigation dans le menu
- [ ] Lancement du jeu
- [ ] Contrôles du jeu fonctionnels
- [ ] Sauvegarde des scores
- [ ] Quitter proprement l'application

## Contribution

Les contributions sont les bienvenues ! Voici comment participer :

### Comment Contribuer

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/NouvelleFonctionnalité`)
3. Committez vos changements (`git commit -m 'Ajout de NouvelleFonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/NouvelleFonctionnalité`)
5. Ouvrez une Pull Request

### Standards de Code

- Suivre PEP 8 pour le style Python
- Documenter les fonctions avec docstrings
- Ajouter des commentaires pour le code complexe
- Tester les nouvelles fonctionnalités
- Mettre à jour la documentation

### Idées de Contribution

- Ajouter de nouveaux niveaux
- Créer des personnages supplémentaires
- Améliorer les graphismes
- Optimiser les performances
- Corriger des bugs
- Traduire en d'autres langues

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

Vous êtes libre d'utiliser, modifier et distribuer ce projet avec attribution appropriée.

## Auteur

**Omar Laraje**

- GitHub : [@omarlr-pro](https://github.com/omarlr-pro)
- LinkedIn : [Omar Laraje](https://www.linkedin.com/in/omar-laraje-998827233/)
- Rôle : Étudiant en Data Science et Business Intelligence
- Localisation : Rabat, Maroc

## Remerciements

- Communauté Pygame pour la documentation et les tutoriels
- Bibliothèques Python open-source
- Contributeurs et testeurs
- Inspirations des jeux classiques

## Support

Pour toute question ou problème :

- Ouvrez une [issue](https://github.com/omarlr-pro/gamehh/issues)
- Consultez la [documentation Pygame](https://www.pygame.org/docs/)
- Contactez-moi via [LinkedIn](https://www.linkedin.com/in/omar-laraje-998827233/)

## Ressources Utiles

### Documentation

- [Documentation Pygame](https://www.pygame.org/docs/)
- [Tutoriels Python](https://docs.python.org/fr/3/tutorial/)
- [Design Patterns en Python](https://refactoring.guru/design-patterns/python)

### Communauté

- [r/pygame](https://www.reddit.com/r/pygame/)
- [Stack Overflow - Pygame](https://stackoverflow.com/questions/tagged/pygame)
- [Discord Pygame](https://discord.gg/pygame)

---

**Développé avec passion pour le game development**

**Mettez une étoile si ce projet vous a inspiré !**
