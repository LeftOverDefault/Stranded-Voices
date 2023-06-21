world_name = "defiance"
world_1 = {
	"shield_generator_chamber": {
		"name": "Shield Generator Chamber",
		"description": "You step into a dimly lit chamber pulsating with a rhythmic hum.\lCables snake along the walls, connecting to the generator's core.\lThe air crackles with static, as a faint glow illuminates the room.\lControl panels displaying complex energy readings are scattered about.",
		"examination": "Intricate circuitry, blinking lights on control panels surround you.\lA powerful blue glow is emanating from the central generator.",
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "shield_deployer_chamber_r",
			"south": "recreation_room",
			"south_east": None,
			"south_west": None,
			"west": "shield_deployer_chamber_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"shield_deployer_chamber_l": {
		"name": "Shield Deployer Chamber (L)",
		"description": "Rows of sleek, futuristic devices are suspended in mid-air.\lReady to project protective energy barriers at a moment's notice.\lDeployers hover silently filling the room with a low hum of energy.\lThe atmosphere is negatively charged, and incredibly dangerous.",
		"examination": "Each deployer is adorned with intricate circuitry.\lSmall vents emit a gentle breeze, carrying a faint scent of ozone.",
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "shield_generator_chamber",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"shield_deployer_chamber_r": {
		"name": "Shield Deployer Chamber (R)",
		"description": "The air grows thick with the acrid smell of burnt circuits.\lDim emergency lights reveal multiple rows of dormant shield deployers.\lLayers of grime coat the floor, from years of neglect and inactivity.\lWires hang like tattered cobwebs, waiting to be repaired.",
		"examination": "Amidst the debris, there is a flickering holographic display.\lThe screen is still trying to project vital shield status information.",
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "shield_generator_chamber",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"recreation_room": {
		"name": "Rec Room",
		"description": "The vibrant space, once a hub of activity, now crowded with silence.\lThe room is bathed in light, casting dynamic patterns on the walls.\lThe air carries the stench of long expired, coffee.\lAn assortment of retro arcade machines run along the walls.",
		"examination": "An old, broken-down holographic table stands at the center.\lA small bar sits at the corner of the room.",
		"directions": {
			"north": "shield_generator_chamber",
			"north_east": None,
			"north_west": None,
			"east": "crew_quarters_r",
			"south": "hydroponics_room",
			"south_east": "janitorial_room",
			"south_west": "mess_hall",
			"west": "crew_quarters_l",
			"up": "recreation_room_balcony",
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"hydroponics_room": {
		"name": "Hydroponics Room",
		"description": "You are enveloped in a warm and humid atmosphere.\lRows of wilted plants stand as a testament to neglect over the years.\lDim lights flicker endlessly, casting eerie shadows across the room.\lThe scent of decayed vegetation fills the air.",
		"examination": "Amidst the desolation, a lone plant, and a symbol of resilience.\lThe soil is dry and cool, hinting at the ship's fading life support.",
		"directions": {
			"north": "recreation_room",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "storage_room",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"storage_room": {
		"name": "Storage Room",
		"description": "Towering shelves lined with disheveled crates crowd the room.\lThe air hangs heavy with the scent of rust and forgotten treasures.\lTools scattered around the floor suggest towards past salvage attempts.\lPiles of broken equipment and spare parts create a chaotic landscape.",
		"examination": "There is a crate labeled \"Emergency Rations\", with its seal torn.\lA clutter of faded notes are pinned to the shelves, all illegible.",
		"directions": {
			"north": "hydroponics_room",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"crew_quarters_l": {
		"name": "Crew Quarters (L)",
		"description": "The cluttered room once served as a home for the ship's crew.\lThe air is tinged with a mix of stale air and hints of metallic oils.\lStacked against the walls are a few personal storage compartments.\lThe sound of distant conversations still haunt the air.",
		"examination": "Personal belongings are scattered about the floor.\lTattered posters and photographs adorn the walls.",
		"directions": {
			"north": "droid_hold_l",
			"north_east": None,
			"north_west": None,
			"east": "recreation_room",
			"south": "mess_hall",
			"south_east": None,
			"south_west": None,
			"west": "escape_pods_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": ["jason"]
	},
	"droid_hold_l": {
		"name": "Droid Hold (L)",
		"description": "You find yourself surrounded by an assortment of mechanical wonders.\lThis place serves as a maintenance/storage room for the droid units.\lThe room is bathed in a dim, bluish light.\lRows of droid compartments, marked with id-codes, crowd the room.",
		"examination": "Transparent casings showcase the complex inner workings of the droids.\lTools and spare parts lie in disarray on the workbench.",
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "crew_quarters_l",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"escape_pods_l": {
		"name": "Escape Pods (L)",
		"description": "Rows of pods lie dormant along the westward wall.\lThe cold metallic doors bear dents from heavy maintenance tools.\lThe pods are all inoperable, as all the circuitry is destroyed.\lEmergency lights bathe the room in an unsteady red glow.",
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "crew_quarters_l",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"crew_quarters_r": {
		"name": "Crew Quarters (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "droid_hold_r",
			"north_east": None,
			"north_west": None,
			"east": "escape_pods_r",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "recreation_room",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"droid_hold_r": {
		"name": "Droid Hold (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "crew_quarters_r",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"escape_pods_r": {
		"name": "Escape Pods (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "crew_quarters_r",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"mess_hall": {
		"name": "Mess Hall",
		"description": "The room is filled with silence, broken by the drip of leaking pipes.\lTables and chairs lie upturned, remnants of the ship's violent descent.\lStale air hangs heavy, carrying the faint scent of spoiled food.\lClouded windows offer a glimpse into the desolate expanse beyond.",
		"examination": None,
		"directions": {
			"north": "crew_quarters_l",
			"north_east": "recreation_room",
			"north_west": None,
			"east": None,
			"south": "galley",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"galley": {
		"name": "Galley",
		"description": None,
		"examination": None,
		"directions": {
			"north": "mess_hall",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "fueling_bay_l",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"janitorial_room": {
		"name": "Janitorial Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "crew_quarters_r",
			"north_east": None,
			"north_west": "recreation_room",
			"east": None,
			"south": "training_room",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"training_room": {
		"name": "Training Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "janitorial_room",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "fueling_bay_r",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"secondary_bridge": {
		"name": "Secondary Bridge",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "fueling_bay_r",
			"south": "hyperdrive_generator",
			"south_east": None,
			"south_west": None,
			"west": "fueling_bay_l",
			"up": None,
			"down": "spacecraft_storage_room_1"
		},
		"objects": [],
		"entities": []
	},
	"fueling_bay_l": {
		"name": "Fueling Bay (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "galley",
			"north_east": None,
			"north_west": None,
			"east": "secondary_bridge",
			"south": "engine_room_l",
			"south_east": None,
			"south_west": None,
			"west": "turret_control_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"turret_control_l": {
		"name": "Turret Control L",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "fueling_bay_l",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_room_l": {
		"name": "Engine Room (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "fueling_bay_l",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"fueling_bar_r": {
		"name": "Fueling Bay (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "training_room",
			"north_east": None,
			"north_west": None,
			"east": "turret_control_r",
			"south": "engine_room_r",
			"south_east": None,
			"south_west": None,
			"west": "secondary_bridge",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"turret_control_r": {
		"name": "Turret Control R",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "fueling_bay_r",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_room_r": {
		"name": "Engine Room (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "fueling_bay_r",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"hyperdrive_generator": {
		"name": "Hyperdrive Generator Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "secondary_bridge",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "hyperdrive_motivator",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"hyperdrive_motivator": {
		"name": "Hyperdrive Motivator Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "hyperdrive_generator",
			"north_east": None,
			"north_west": None,
			"east": "secondary_hyperdrive_unit_r",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "secondary_hyperdrive_unit_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"secondary_hyperdrive_unit_l": {
		"name": "Secondary Hyperdrive Unit Room (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "hyperdrive_motivator",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"secondary_hyperdrive_unit_r": {
		"name": "Secondary Hyperdrive Unit Room (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "hyperdrive_motivator",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"recreation_room_balcony": {
		"name": "Recreation Room Balcony",
		"description": None,
		"examination": None,
		"directions": {
			"north": "captains_station",
			"north_east": "conference_room",
			"north_west": "computer_control_room",
			"east": None,
			"south": "main_bridge",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": "recreation_room"
		},
		"objects": [],
		"entities": []
	},
	"captains_station": {
		"name": "Captain's Station",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "recreation_room_balcony",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"conference_room": {
		"name": "Conference Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": "recreation_room_balcony",
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"computer_control_room": {
		"name": "Computer Control Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": "recreation_room_balcony",
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"main_bridge": {
		"name": "Main Bridge",
		"description": None,
		"examination": None,
		"directions": {
			"north": "recreation_room_balcony",
			"north_east": None,
			"north_west": None,
			"east": "locker_room_r",
			"south": "deck",
			"south_east": "strategy_room",
			"south_west": None,
			"west": "locker_room_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"strategy_room": {
		"name": "Strategy Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": "main_bridge",
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"locker_room_l": {
		"name": "Locker Room (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "officers_office_l",
			"north_east": None,
			"north_west": None,
			"east": "main_bridge",
			"south": "laboratory",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"officers_quarters_l": {
		"name": "Officer's Quarters (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "locker_room_l",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"locker_room_r": {
		"name": "Locker Room (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": "officers_quarters_r",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "main_bridge",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"officers_quarters_r": {
		"name": "Officer's Quarters (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "locker_room_r",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"laboratory": {
		"name": "Laboratory",
		"description": None,
		"examination": None,
		"directions": {
			"north": "locker_room_l",
			"north_east": None,
			"north_west": None,
			"east": "deck",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"deck": {
		"name": "Deck",
		"description": None,
		"examination": None,
		"directions": {
			"north": "main_bridge",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "medbay",
			"south_east": "brig",
			"south_west": "weapons_storage",
			"west": "laboratory",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"brig": {
		"name": "Brig",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": "deck",
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"weapons_storage": {
		"name": "Weapons Storage",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": "deck",
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"medbay": {
		"name": "Medbay",
		"description": None,
		"examination": None,
		"directions": {
			"north": "deck",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "primary_generator",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"primary_generator": {
		"name": "Primary Generator Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "medbay",
			"north_east": None,
			"north_west": None,
			"east": "engine_platform_r",
			"south": "engineering_room",
			"south_east": None,
			"south_west": None,
			"west": "engine_platform_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_platform_l": {
		"name": "Engine Platform (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": "turret_maintenance_room_l",
			"east": "primary_generator",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"turret_maintenance_room_l": {
		"name": "Turret Maintenance Room (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": "engine_l_platform",
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_platform_r": {
		"name": "Engine Platform (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": "turret_maintenance_room_r",
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "primary_generator",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"turret_maintenance_room_r": {
		"name": "Turret Maintenance Room (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": "engine_platform_r",
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engineering_room": {
		"name": "Engineering Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "primary_generator",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"computer_core_chamber": {
		"name": "Computer Core Chamber",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "shield_generator_maintenance_room",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"shield_generator_maintenance_room": {
		"name": "Shield Generator Maintenance Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "miscellaneous_storage_room",
			"south": "landing_gear_maintenance_room",
			"south_east": None,
			"south_west": None,
			"west": "computer_core_chamber",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"miscellaneous_storage_room": {
		"name": "Miscellaneous Storage Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "cargo_bay_r_2",
			"south_east": None,
			"south_west": None,
			"west": "shield_generator_maintenance_room",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"landing_gear_maintenance_room": {
		"name": "Landing Gear Maintenance Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "shield_generator_maintenance_room",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "repulser_lift_maintenance_room",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"repulser_lift_maintenance_room": {
		"name": "Repulser Lift Maintenance Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "landing_gear_maintenance_room",
			"north_east": None,
			"north_west": None,
			"east": "cargo_bay_r_1",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "cargo_bay_l_1",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"cargo_bay_l_1": {
		"name": "Cargo Bay (L) [1]",
		"description": None,
		"examination": None,
		"directions": {
			"north": "cargo_bay_l_2",
			"north_east": None,
			"north_west": None,
			"east": "repulser_lift_maintenance_room",
			"south": "dry_storage_room",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"cargo_bay_l_2": {
		"name": "Cargo Bay (L) [2]",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "cargo_bay_l_1",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"cargo_bay_r_1": {
		"name": "Cargo Bay (R) [1]",
		"description": None,
		"examination": None,
		"directions": {
			"north": "cargo_bay_r_2",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "cold_storage_room",
			"south_east": None,
			"south_west": "spacecraft_storage_room_2",
			"west": "repulser_lift_maintenance_room",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"cargo_bay_r_2": {
		"name": "Cargo Bay (R) [2]",
		"description": None,
		"examination": None,
		"directions": {
			"north": "miscellaneous_storage_room",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": "cargo_bay_r_1",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"dry_storage_room": {
		"name": "Dry Storage Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "cargo_bay_l_1",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"cold_storage_room": {
		"name": "Cold Storage Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "cargo_bay_r_1",
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"spacecraft_storage_room_1": {
		"name": "Spacecraft Storage Room [1]",
		"description": None,
		"examination": None,
		"directions": {
			"north": "spacecraft_storage_room_2",
			"north_east": None,
			"north_west": None,
			"east": "vehicle_storage_bay",
			"south": "hyperdrive_control_room",
			"south_east": None,
			"south_west": None,
			"west": "airlock_chamber",
			"up": "secondary_bridge",
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"spacecraft_storage_room_2": {
		"name": "Spacecraft Storage Room [2]",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": "cargo_bay_r_1",
			"north_west": "cargo_bay_r_1",
			"east": None,
			"south": "spacecraft_storage_room_1",
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"airlock_chamber": {
		"name": "Airlock Chamber",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "spacecraft_storage_room_1",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"vehicle_storage_bay": {
		"name": "Vehicle Storage Bay",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "spacecraft_storage_room_1",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_mechanics_room_l": {
		"name": "Engine Mechanics Room (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "hyperdrive_control_room",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"engine_mechanics_room_r": {
		"name": "Engine Mechanics Room (R)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "hyperdrive_control_room",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"hyperdrive_control_room": {
		"name": "Hyperdrive Control Room",
		"description": None,
		"examination": None,
		"directions": {
			"north": "spacecraft_storage_room_1",
			"north_east": None,
			"north_west": None,
			"east": "engine_mechanics_room_r",
			"south": "secondary_power_core_chamber",
			"south_east": None,
			"south_west": None,
			"west": "engine_mechanics_room_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"secondary_power_core_chamber": {
		"name": "Secondary Power Core Chamber",
		"description": None,
		"examination": None,
		"directions": {
			"north": "engine_mechanics_room_r",
			"north_east": None,
			"north_west": None,
			"east": "repulser_lift_r",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "repulser_lift_l",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"repulser_lift_l": {
		"name": "Repulser Lift (L)",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": "secondary_power_core_chamber",
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": None,
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
	"repulser_lift_r": {
		"name": "Repulser Lift R",
		"description": None,
		"examination": None,
		"directions": {
			"north": None,
			"north_east": None,
			"north_west": None,
			"east": None,
			"south": None,
			"south_east": None,
			"south_west": None,
			"west": "secondary_power_core_chamber",
			"up": None,
			"down": None
		},
		"objects": [],
		"entities": []
	},
}