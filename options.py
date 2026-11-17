from dataclasses import dataclass
from Options import OptionGroup, DeathLink, Range, Toggle, PerGameCommonOptions, Choice

# class StartingLevels(Range):
#     """Amount of levels unlocked by default."""
#     display_name = "Starting Levels"
#     range_start = 1
#     range_end = 5
#     default = 3

class GoalRequirement(Range):
    """Choose the number of levels needed to be beaten to unlock the goal."""
    display_name = "Goal Requirement"
    range_start = 3
    range_end = 25
    default = 10

class DeathAmount(Range):
    """Amount of deaths needed before sending a DeathLink signal. Does nothing if DeathLink is disabled."""
    display_name = "DeathLink Amnesty"
    range_start = 1
    range_end = 30
    default = 10

class Ultimate(Toggle):
    """Enables Ultimate Clubstep, Theory of Everything 2 and Deadlocked as locations.
    Ultimate means collecting all 3 coins in that level (Demon levels only)."""
    display_name = "Ultimate Achievements"
    default = False

class CoinLocks(Toggle):
    """Enables the vanilla coin locks for Clubstep, Theory of Everything 2 and Deadlocked.
    Turning this on will require you to collect a certain number of coins before you can access it.
    Clubstep requires 10 coins collected, ToE 2 requires 20 coins and Deadlocked requires 30 coins."""
    display_name = "Coin Locks"
    default = False

# No idea what this is nor what it does so I'll leave it commented for now - JellyMoose
# class Speed(Range):
#     """Speed up a level in the range (this is a multiplier - 125 is 1.25x speed )(Weighted based on diffculty)"""
#     display_name = "Speed"
#     range_start = 75
#     range_end = 250
#     default = 100

# class Coins(Toggle):
#     """Create coins in the world generation (disabling will remove portal checks)"""
#     display_name = "Coins"
#     default = True

# class CheckShop(Toggle):
#     """Enables Check Shop locations, lets you buy items"""
#     display_name = "Check Shop"
#     default = True

# class Spinoff(Toggle):
    # """Enables Meltdown and Subzero levels as checks. You must have MoreGames by BitZ installed!"""
    # display_name = "Meltdown and Subzero Levels"
    # default = False

@dataclass
class GDOptions(PerGameCommonOptions):
    # start_levels: StartingLevels
    goal_requirement: GoalRequirement
    coin_locks: CoinLocks
    ultimate: Ultimate
    death_link: DeathLink
    death_link_amnesty: DeathAmount
    # spinoff: Spinoff
    # speed: Speed
    # coins: Coins
    # check_shop: CheckShop

# TODO: Implement option_groups and option_preset later on
option_groups = []

option_preset = {}