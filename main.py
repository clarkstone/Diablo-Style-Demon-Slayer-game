import random
import time
import pickle

# Define the player class
class Player:
    def __init__(self, name, health, attack, attack_speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.potions = 3
        self.breathing_style = None
        self.special_ability = None
        self.rank = "Initiate"
        self.skill_points = 0
        self.inventory = []
        self.quest = None
        self.talent_points = 0
        self.skill_tree = {
            "Water Breathing": {
                "Active Skills": ["Water Splash", "Whirlpool"],
                "Passive Skills": ["Water Veil", "Water Mastery"]
            },
            "Thunder Breathing": {
                "Active Skills": ["Thunderclap", "Lightning Bolt"],
                "Passive Skills": ["Electric Charge", "Lightning Mastery"]
            },
            "Flame Breathing": {
                "Active Skills": ["Fire Burst", "Inferno"],
                "Passive Skills": ["Burning Aura", "Fire Mastery"]
            },
            "Love Breathing": {
                "Active Skills": ["Heart's Touch", "Love's Embrace"],
                "Passive Skills": ["Healing Touch", "Heart's Shield"]
            },
            "Mist Breathing": {
                "Active Skills": ["Mist Shroud", "Waterfall Mist"],
                "Passive Skills": ["Mist Cloak", "Mist Manipulation"]
            },
            "Sound Breathing": {
                "Active Skills": ["Sonic Wave", "Harmonious Melody"],
                "Passive Skills": ["Resonating Melody", "Sound Amplification"]
            }
        }

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        if random.random() <= self.attack_speed:  # Attack speed chance
            if random.random() <= 0.1:  # 10% chance for a critical hit
                damage = self.attack * 2
                print(f"{self.name} lands a critical hit on {enemy.name} for {damage} damage!")
            else:
                damage = random.randint(1, self.attack)
                print(f"{self.name} attacks {enemy.name} for {damage} damage.")
            enemy.take_damage(damage)
        else:
            print(f"{self.name}'s attack missed!")

    def gain_experience(self, experience):
        self.exp += experience
        print(f"{self.name} gains {experience} experience points.")
        if self.exp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.attack += 5
        self.health += 10
        self.attack_speed += 0.05
        self.skill_points += 1
        self.talent_points += 1
        print(f"Level up! {self.name} is now level {self.level}.")
        print(f"{self.name}'s health, attack, and attack speed have increased.")
        print(f"{self.name} has gained 1 skill point and 1 talent point.")

    def update_rank(self):
        if self.level >= 5 and self.rank == "Initiate":
            self.rank = "Pillar"
            print(f"{self.name} has been promoted to the rank of Pillar!")
        elif self.level >= 10 and self.rank == "Pillar":
            self.rank = "Hashira"
            print(f"{self.name} has been promoted to the rank of Hashira!")

    def earn_gold(self, gold):
        self.gold += gold
        print(f"{self.name} earns {gold} gold.")

    def spend_gold(self, cost):
        if self.gold >= cost:
            self.gold -= cost
            return True
        else:
            print("Insufficient gold.")
            return False

    def use_health_potion(self):
        if self.potions > 0:
            self.health += 20
            if self.health > 100:
                self.health = 100
            self.potions -= 1
            print(f"{self.name} drinks a health potion and restores 20 health.")
            print(f"{self.name} has {self.potions} health potions left.")
        else:
            print("No health potions left.")

    def choose_breathing_style(self):
        print("\nChoose your Breathing Style:")
        print("1. Water Breathing")
        print("2. Thunder Breathing")
        print("3. Flame Breathing")
        print("4. Love Breathing")
        print("5. Mist Breathing")
        print("6. Sound Breathing")
        print("7. Exit")

        style_choice = input("Enter your choice: ")

        if style_choice == "1":
            self.breathing_style = "Water Breathing"
            self.attack += 10
            print(f"{self.name} has chosen Water Breathing! Attack increased by 10.")
            self.special_ability = "Water Splash"
        elif style_choice == "2":
            self.breathing_style = "Thunder Breathing"
            self.attack += 15
            print(f"{self.name} has chosen Thunder Breathing! Attack increased by 15.")
            self.special_ability = "Lightning Bolt"
        elif style_choice == "3":
            self.breathing_style = "Flame Breathing"
            self.attack += 12
            print(f"{self.name} has chosen Flame Breathing! Attack increased by 12.")
            self.special_ability = "Fire Burst"
        elif style_choice == "4":
            self.breathing_style = "Love Breathing"
            self.attack += 8
            self.attack_speed += 0.1
            print(f"{self.name} has chosen Love Breathing! Attack increased by 8 and attack speed increased.")
            self.special_ability = "Heart's Touch"
        elif style_choice == "5":
            self.breathing_style = "Mist Breathing"
            self.attack += 10
            print(f"{self.name} has chosen Mist Breathing! Attack increased by 10.")
            self.special_ability = "Mist Shroud"
        elif style_choice == "6":
            self.breathing_style = "Sound Breathing"
            self.attack += 12
            print(f"{self.name} has chosen Sound Breathing! Attack increased by 12.")
            self.special_ability = "Sonic Wave"
        elif style_choice == "7":
            print("Breathing Style selection canceled.")
        else:
            print("Invalid choice. Try again.")

    def use_special_ability(self, enemy):
        if self.special_ability:
            print(f"{self.name} uses {self.special_ability} on {enemy.name}!")
            if self.special_ability == "Water Splash":
                damage = self.attack * 1.5
                print(f"{self.name} creates a powerful water splash, dealing {damage} damage to {enemy.name}!")
            elif self.special_ability == "Lightning Bolt":
                damage = self.attack * 2
                print(f"{self.name} summons a lightning bolt, striking {enemy.name} for {damage} damage!")
            elif self.special_ability == "Fire Burst":
                damage = self.attack * 1.8
                print(f"{self.name} releases a fiery burst, burning {enemy.name} for {damage} damage!")
            elif self.special_ability == "Heart's Touch":
                damage = self.attack * 1.2
                heal = damage // 2
                print(f"{self.name} touches {enemy.name}'s heart, dealing {damage} damage and healing for {heal} health!")
                self.health += heal
                if self.health > 100:
                    self.health = 100
            enemy.take_damage(damage)
        else:
            print("No special ability available.")

    def allocate_skill_points(self):
        print(f"\n{self.name}, you have {self.skill_points} skill points to allocate.")
        while self.skill_points > 0:
            print(f"Current Attack: {self.attack}")
            print(f"Current Health: {self.health}")
            print(f"Current Attack Speed: {self.attack_speed}")
            print(f"Skill Points Available: {self.skill_points}")
            print("1. Increase Attack")
            print("2. Increase Health")
            print("3. Increase Attack Speed")
            print("4. Exit")

            skill_choice = input("Enter your choice: ")

            if skill_choice == "1":
                self.attack += 3
                self.skill_points -= 1
                print(f"{self.name}'s attack has increased!")
            elif skill_choice == "2":
                self.health += 5
                self.skill_points -= 1
                print(f"{self.name}'s health has increased!")
            elif skill_choice == "3":
                self.attack_speed += 0.02
                self.skill_points -= 1
                print(f"{self.name}'s attack speed has increased!")
            elif skill_choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    def allocate_talent_points(self):
        print(f"\n{self.name}, you have {self.talent_points} talent points to allocate.")
        while self.talent_points > 0:
            print("Available Skills:")
            print("1. Water Splash (Water Breathing)")
            print("2. Whirlpool (Water Breathing)")
            print("3. Thunderclap (Thunder Breathing)")
            print("4. Lightning Bolt (Thunder Breathing)")
            print("5. Fire Burst (Flame Breathing)")
            print("6. Inferno (Flame Breathing)")
            print("7. Heart's Touch (Love Breathing)")
            print("8. Love's Embrace (Love Breathing)")
            print("9. Exit")

            talent_choice = input("Enter the number of the skill you want to allocate points to: ")

            if talent_choice == "1":
                if self.breathing_style == "Water Breathing":
                    self.skill_tree["Water Breathing"]["Active Skills"][0] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Water Splash!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "2":
                if self.breathing_style == "Water Breathing":
                    self.skill_tree["Water Breathing"]["Active Skills"][1] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Whirlpool!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "3":
                if self.breathing_style == "Thunder Breathing":
                    self.skill_tree["Thunder Breathing"]["Active Skills"][0] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Thunderclap!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "4":
                if self.breathing_style == "Thunder Breathing":
                    self.skill_tree["Thunder Breathing"]["Active Skills"][1] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Lightning Bolt!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "5":
                if self.breathing_style == "Flame Breathing":
                    self.skill_tree["Flame Breathing"]["Active Skills"][0] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Fire Burst!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "6":
                if self.breathing_style == "Flame Breathing":
                    self.skill_tree["Flame Breathing"]["Active Skills"][1] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Inferno!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "7":
                if self.breathing_style == "Love Breathing":
                    self.skill_tree["Love Breathing"]["Active Skills"][0] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Heart's Touch!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "8":
                if self.breathing_style == "Love Breathing":
                    self.skill_tree["Love Breathing"]["Active Skills"][1] += 1
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to Love's Embrace!")
                else:
                    print("You can only allocate talent points to skills of your chosen Breathing Style.")
            elif talent_choice == "9":
                break
            else:
                print("Invalid choice. Try again.")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} obtained {item}!")

    def display_inventory(self):
        print(f"\n{self.name}'s Inventory:")
        if len(self.inventory) == 0:
            print("Empty")
        else:
            for item in self.inventory:
                print(item)

    def start_quest(self):
        if not self.quest:
            quest = generate_random_quest()
            self.quest = quest
            print(f"{self.name} has started the quest: {quest['name']}")
            print(f"Objective: {quest['objective']}")
        else:
            print(f"{self.name} is already on a quest.")

    def check_quest_progress(self):
        if self.quest:
            print(f"{self.name}'s Quest Progress:")
            print(f"Quest: {self.quest['name']}")
            print(f"Objective: {self.quest['objective']}")
            print(f"Progress: {self.quest['progress']}/{self.quest['target']}")
        else:
            print(f"{self.name} is not on a quest.")

    def complete_quest(self):
        if self.quest:
            if self.quest['progress'] >= self.quest['target']:
                print(f"Congratulations! {self.name} has completed the quest: {self.quest['name']}")
                self.exp += self.quest['reward_exp']
                self.gold += self.quest['reward_gold']
                reward_items = self.quest.get('reward_items', [])
                if reward_items:
                    for item in reward_items:
                        self.add_item_to_inventory(item)
                self.quest = None
            else:
                print(f"{self.name} has not completed the quest yet.")
        else:
            print(f"{self.name} is not on a quest.")

    def allocate_talent_points(self):
        print(f"\n{self.name}, you have {self.talent_points} talent points to allocate.")
        while self.talent_points > 0:
            print("Available Skills:")
            print("1. Water Splash (Water Breathing)")
            print("2. Whirlpool (Water Breathing)")
            print("3. Thunderclap (Thunder Breathing)")
            print("4. Lightning Bolt (Thunder Breathing)")
            print("5. Fire Burst (Flame Breathing)")
            print("6. Inferno (Flame Breathing)")
            print("7. Heart's Touch (Love Breathing)")
            print("8. Love's Embrace (Love Breathing)")
            print("9. Exit")

            talent_choice = input("Enter the number of the skill you want to allocate points to: ")

            if talent_choice == "9":
                break
            elif talent_choice.isdigit() and 1 <= int(talent_choice) <= 8:
                skill_name = self.get_skill_from_talent_choice(talent_choice)
                if skill_name is not None:
                    self.increment_skill(skill_name)
                    self.talent_points -= 1
                    print(f"{self.name} has allocated a talent point to {skill_name}!")
            else:
                print("Invalid choice. Try again.")

    def get_skill_from_talent_choice(self, talent_choice):
        if self.breathing_style is None:
            return None

        breathing_style_skills = self.skill_tree.get(self.breathing_style)
        if breathing_style_skills is None:
            return None

        active_skills = breathing_style_skills.get("Active Skills")
        if active_skills is None:
            return None

        if talent_choice.endswith("1") and len(active_skills) > 0:
            return active_skills[0]
        elif talent_choice.endswith("2") and len(active_skills) > 1:
            return active_skills[1]
        else:
            return None

    def increment_skill(self, skill_name):
        skill_level = self.skill_tree[self.breathing_style]["Active Skills"][skill_name]
        self.skill_tree[self.breathing_style]["Active Skills"][skill_name] = skill_level + 1

    def save_game(self):
        with open("savegame.pkl", "wb") as f:
            pickle.dump(self, f)
        print("Game saved!")

    @staticmethod
    def load_game():
        try:
            with open("savegame.pkl", "rb") as f:
                player = pickle.load(f)
            print("Game loaded!")
            return player
        except FileNotFoundError:
            print("No saved game found.")
            return None

# Define the enemy class
class Enemy:
    def __init__(self, name, health, attack, experience, gold, drop_items):
        self.name = name
        self.health = health
        self.attack = attack
        self.experience = experience
        self.gold = gold
        self.drop_items = drop_items

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} for {damage} damage.")

    def give_experience(self, player):
        player.gain_experience(self.experience)

    def give_gold(self, player):
        player.earn_gold(self.gold)

    def drop_item(self, player):
        item = random.choice(self.drop_items)
        player.add_item_to_inventory(item)


# Define the shop class
class Shop:
    def __init__(self):
        self.weapons = {
            "Sword": {"attack": 10, "cost": 20},
            "Axe": {"attack": 15, "cost": 30},
            "Bow": {"attack": 12, "cost": 25}
        }
        self.potions = {
            "Health Potion": {"health": 20, "cost": 10},
            "Power Potion": {"attack": 5, "cost": 15}
        }

    def show_weapons(self):
        print("Available Weapons:")
        for weapon, stats in self.weapons.items():
            print(f"{weapon} (+{stats['attack']} attack) - {stats['cost']} gold")

    def show_potions(self):
        print("Available Potions:")
        for potion, stats in self.potions.items():
            if 'health' in stats:
                print(f"{potion} (+{stats['health']} health) - {stats['cost']} gold")
            elif 'attack' in stats:
                print(f"{potion} (+{stats['attack']} attack) - {stats['cost']} gold")

    def buy_weapon(self, player, weapon):
        if weapon in self.weapons:
            if player.spend_gold(self.weapons[weapon]["cost"]):
                player.attack += self.weapons[weapon]["attack"]
                player.add_item_to_inventory(weapon)
                print(f"{player.name} has bought a {weapon} (+{self.weapons[weapon]['attack']} attack)!")
        else:
            print("Weapon not available.")

    def buy_potion(self, player, potion):
        if potion in self.potions:
            if player.spend_gold(self.potions[potion]["cost"]):
                if 'health' in self.potions[potion]:
                    player.potions += 1
                    print(f"{player.name} has bought a {potion} (+{self.potions[potion]['health']} health)!")
                elif 'attack' in self.potions[potion]:
                    player.attack += self.potions[potion]["attack"]
                    print(f"{player.name} has bought a {potion} (+{self.potions[potion]['attack']} attack)!")
        else:
            print("Potion not available.")

# Define the game function
def game():
    player = Player("Tanjiro", 100, 10, 0.5)
    enemy = Enemy("Demon", 50, 8, 20, 10, ["Demon Blood", "Demon Horn"])
    shop = Shop()

    while True:
        print("\nWhat would you like to do?")
        print("1. Battle Enemy")
        print("2. Use Health Potion")
        print("3. Buy Weapons or Potions")
        print("4. Display Inventory")
        print("5. Start Quest")
        print("6. Check Quest Progress")
        print("7. Complete Quest")
        print("8. Allocate Skill Points")
        print("9. Allocate Talent Points")
        print("10. Save Game")
        print("11. Load Game")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            battle(player, enemy)
        elif choice == "2":
            player.use_health_potion()
        elif choice == "3":
            shop_menu(player, shop)
        elif choice == "4":
            player.display_inventory()
        elif choice == "5":
            player.start_quest()
        elif choice == "6":
            player.check_quest_progress()
        elif choice == "7":
            player.complete_quest()
        elif choice == "8":
            player.allocate_skill_points()
        elif choice == "9":
            player.allocate_talent_points()
        elif choice == "10":
            player.save_game()
        elif choice == "11":
            player = Player.load_game()
        elif choice == "12":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Define the battle function
def battle(player, enemy):
    print(f"\n{player.name} vs {enemy.name} - FIGHT!")

    while player.is_alive() and enemy.is_alive():
        player.attack_enemy(enemy)
        if enemy.is_alive():
            enemy.attack_player(player)

    if player.is_alive():
        print(f"{player.name} wins the battle!")
        player.gain_experience(enemy.experience)
        player.earn_gold(enemy.gold)
        enemy.drop_item(player)
    else:
        print(f"{enemy.name} wins the battle! {player.name} has been defeated.")

    player.update_rank()

# Define the shop menu function
def shop_menu(player, shop):
    while True:
        print("\nWelcome to the Shop!")
        print("1. Buy Weapons")
        print("2. Buy Potions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            shop.show_weapons()
            weapon_choice = input("Enter the name of the weapon you want to buy (or 'exit'): ")
            if weapon_choice == "exit":
                continue
            shop.buy_weapon(player, weapon_choice)
        elif choice == "2":
            shop.show_potions()
            potion_choice = input("Enter the name of the potion you want to buy (or 'exit'): ")
            if potion_choice == "exit":
                continue
            shop.buy_potion(player, potion_choice)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


# Generate a random quest
def generate_random_quest():
    quests = [
        {
            "name": "Defeat the Demon",
            "objective": "Defeat 5 demons",
            "progress": 0,
            "target": 5,
            "reward_exp": 50,
            "reward_gold": 20,
            "reward_items": ["Demon Slayer Sword"]
        },
        {
            "name": "Collect Herbs",
            "objective": "Collect 10 healing herbs",
            "progress": 0,
            "target": 10,
            "reward_exp": 30,
            "reward_gold": 10,
            "reward_items": ["Health Potion", "Healing Herb"]
        },
        {
            "name": "Rescue the Hostage",
            "objective": "Rescue the hostage from the enemy base",
            "progress": 0,
            "target": 1,
            "reward_exp": 100,
            "reward_gold": 50,
            "reward_items": ["Rescue Badge"]
        }
    ]
    return random.choice(quests)


# Start the game
game()
