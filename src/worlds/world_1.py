world_name = "defiance"
world_1 = {
	"shield_generator_chamber": {
		"name": "Shield Generator Chamber",
		"description": "You step into a dimly lit chamber pulsating with a rhythmic hum.\lCables snake along the walls, connecting to the generator's core.\lThe air crackles with static, as a faint glow illuminates the room.\lControl panels displaying complex energy readings are scattered about.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": "shield_deployer_chamber_r",
				"move_description": ""
			},
			"south": {
				"location": "recreation_room",
				"move_description": ""
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": "shield_deployer_chamber_l",
				"move_description": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": []
	},
	"shield_deployer_chamber_l": {
		"name": "Shield Deployer Chamber (L)",
		"description": "Rows of sleek, futuristic devices are suspended in mid-air.\lReady to project protective energy barriers at a moment's notice.\lDeployers hover silently filling the room with a low hum of energy.\lThe atmosphere is negatively charged, and incredibly dangerous.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": "shield_generator_chamber",
				"move_description": ""
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"shield_deployer_chamber_r": {
		"name": "Shield Deployer Chamber (R)",
		"description": "The air grows thick with the acrid smell of burnt circuits.\lDim emergency lights reveal multiple rows of dormant shield deployers.\lLayers of grime coat the floor, from years of neglect and inactivity.\lWires hang like tattered cobwebs, waiting to be repaired.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": "shield_generator_chamber",
				"move_description": ""
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"recreation_room": {
		"name": "Rec Room",
		"description": "The vibrant space, once a hub of activity, now crowded with silence.\lThe room is bathed in light, casting dynamic patterns on the walls.\lThe air carries the stench of long expired, coffee.\lAn assortment of retro arcade machines run along the walls.",
		"directions": {
			"north": {
				"location": "shield_generator_chamber",
				"move_description": ""
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": "crew_quarters_r",
				"move_description": ""
			},
			"south": {
				"location": "hydroponics_room",
				"move_description": ""
			},
			"south_east": {
				"location": "janitorial_room",
				"move_description": ""
			},
			"south_west": {
				"location": "mess_hall",
				"move_description": ""
			},
			"west": {
				"location": "crew_quarters_l",
				"move_description": ""
			},
			"up": {
				"location": "recreation_room_balcony",
				"move_description": ""
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"hydroponics_room": {
		"name": "Hydroponics Room",
		"description": "You are enveloped in a warm and humid atmosphere.\lRows of wilted plants stand as a testament to neglect over the years.\lDim lights flicker endlessly, casting eerie shadows across the room.\lThe scent of decayed vegetation fills the air.",
		"directions": {
			"north": "recreation_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "storage_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"storage_room": {
		"name": "Storage Room",
		"description": "Towering shelves lined with disheveled crates crowd the room.\lThe air hangs heavy with the scent of rust and forgotten treasures.\lTools scattered around the floor suggest towards past salvage attempts.\lPiles of broken equipment and spare parts create a chaotic landscape.",
		"directions": {
			"north": {
				"location": "hydroponics_room",
				"move_direction": ""
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"crew_quarters_l": {
		"name": "Crew Quarters (L)",
		"description": "Stepping into the Crew Quarters, you're greeted by a scene of chaos frozen in time.\lTorn fabric hangs from the damaged bunks, like tattered dreams of rest.\lPersonal belongings are strewn across the floor, abandoned in the ship's final moments.\lThe air is heavy with a mix of mustiness and nostalgia.",
		"directions": {
			"north": {
				"location": "droid_hold_l",
				"move_description": ""
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": "recreation_room",
				"move_direction": ""
			},
			"south": {
				"location": "mess_hall",
				"move_description": ""
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": "escape_pods_l",
				"move_direction": ""
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"droid_hold_l": {
		"name": "Droid Hold (L)",
		"description": "You find yourself surrounded by an assortment of mechanical wonders.\lThis place serves as a maintenance/storage room for the droid units.\lThe room is bathed in a dim, bluish light.\lRows of droid compartments, marked with id-codes, crowd the room.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "crew_quarters_l",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": []
	},
	"escape_pods_l": {
		"name": "Escape Pods (L)",
		"description": "Rows of pods lie dormant along the westward wall.\lThe cold metallic doors bear dents from heavy maintenance tools.\lThe pods are all inoperable, as all the circuitry is destroyed.\lEmergency lights bathe the room in an unsteady red glow.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "crew_quarters_l",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			},
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"crew_quarters_r": {
		"name": "Crew Quarters (R)",
		"description": "",
		"directions": {
			"north": "droid_hold_r",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "escape_pods_r",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "recreation_room",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"droid_hold_r": {
		"name": "Droid Hold (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "crew_quarters_r",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"escape_pods_r": {
		"name": "Escape Pods (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "crew_quarters_r",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"mess_hall": {
		"name": "Mess Hall",
		"description": "The room is filled with silence, broken by the drip of leaking pipes.\lTables and chairs lie upturned, remnants of the ship's violent descent.\lStale air hangs heavy, carrying the faint scent of spoiled food.\lClouded windows offer a glimpse into the desolate expanse beyond.",
		"directions": {
			"north": "crew_quarters_l",
			"north_east": "recreation_room",
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "galley",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"galley": {
		"name": "Galley",
		"description": "",
		"directions": {
			"north": "mess_hall",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "fueling_bay_l",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"janitorial_room": {
		"name": "Janitorial Room",
		"description": "",
		"directions": {
			"north": "crew_quarters_r",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": "recreation_room",
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "training_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"training_room": {
		"name": "Training Room",
		"description": "",
		"directions": {
			"north": "janitorial_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "fueling_bay_r",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"secondary_bridge": {
		"name": "Secondary Bridge",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "fueling_bay_r",
			"south": "hyperdrive_generator",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "fueling_bay_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": "spacecraft_storage_room_1"
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"fueling_bay_l": {
		"name": "Fueling Bay (L)",
		"description": "",
		"directions": {
			"north": "galley",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "secondary_bridge",
			"south": "engine_room_l",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "turret_control_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"turret_control_l": {
		"name": "Turret Control L",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "fueling_bay_l",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"engine_room_l": {
		"name": "Engine Room (L)",
		"description": "",
		"directions": {
			"north": "fueling_bay_l",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": [],
	},
	"fueling_bay_r": {
		"name": "Fueling Bay (R)",
		"description": "",
		"directions": {
			"north": "training_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "turret_control_r",
			"south": "engine_room_r",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "secondary_bridge",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": []
		
		
		
	},
	"turret_control_r": {
		"name": "Turret Control R",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "fueling_bay_r",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"placed_objects": [],
		"entities": []
		
		
		
	},


	"engine_room_r": {
		"name": "Engine Room (R)",
		"description": "",
		"directions": {
			"north": "fueling_bay_r",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"hyperdrive_generator": {
		"name": "Hyperdrive Generator Room",
		"description": "",
		"directions": {
			"north": "secondary_bridge",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "hyperdrive_motivator",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"hyperdrive_motivator": {
		"name": "Hyperdrive Motivator Room",
		"description": "",
		"directions": {
			"north": "hyperdrive_generator",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "secondary_hyperdrive_unit_r",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "secondary_hyperdrive_unit_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"secondary_hyperdrive_unit_l": {
		"name": "Secondary Hyperdrive Unit Room (L)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "hyperdrive_motivator",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"secondary_hyperdrive_unit_r": {
		"name": "Secondary Hyperdrive Unit Room (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "hyperdrive_motivator",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"recreation_room_balcony": {
		"name": "Recreation Room Balcony",
		"description": "",
		"directions": {
			"north": "captains_station",
			"north_east": "conference_room",
			"north_west": "computer_control_room",
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "main_bridge",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": "recreation_room"
		},
		"objects": [],
		"entities": []
		,
	},
	"captains_station": {
		"name": "Captain's Station",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "recreation_room_balcony",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": []
		,
	},
	"conference_room": {
		"name": "Conference Room",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": "recreation_room_balcony",
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"computer_control_room": {
		"name": "Computer Control Room",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": "recreation_room_balcony",
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"main_bridge": {
		"name": "Main Bridge",
		"description": "",
		"directions": {
			"north": "recreation_room_balcony",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "locker_room_r",
			"south": "deck",
			"south_east": "strategy_room",
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "locker_room_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"strategy_room": {
		"name": "Strategy Room",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": "main_bridge",
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"locker_room_l": {
		"name": "Locker Room (L)",
		"description": "",
		"directions": {
			"north": "officers_office_l",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "main_bridge",
			"south": "laboratory",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"officers_quarters_l": {
		"name": "Officer's Quarters (L)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "locker_room_l",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"locker_room_r": {
		"name": "Locker Room (R)",
		"description": "",
		"directions": {
			"north": "officers_quarters_r",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "main_bridge",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"officers_quarters_r": {
		"name": "Officer's Quarters (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "locker_room_r",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"laboratory": {
		"name": "Laboratory",
		"description": "",
		"directions": {
			"north": "locker_room_l",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "deck",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"deck": {
		"name": "Deck",
		"description": "",
		"directions": {
			"north": "main_bridge",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "medbay",
			"south_east": "brig",
			"south_west": "weapons_storage",
			"west": "laboratory",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"brig": {
		"name": "Brig",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": "deck",
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"weapons_storage": {
		"name": "Weapons Storage",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": "deck",
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"medbay": {
		"name": "Medbay",
		"description": "",
		"directions": {
			"north": "deck",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "primary_generator",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"primary_generator": {
		"name": "Primary Generator Room",
		"description": "",
		"directions": {
			"north": "medbay",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "engine_platform_r",
			"south": "engineering_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "engine_platform_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"engine_platform_l": {
		"name": "Engine Platform (L)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": "turret_maintenance_room_l",
			"east": "primary_generator",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"turret_maintenance_room_l": {
		"name": "Turret Maintenance Room (L)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": "engine_l_platform",
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"engine_platform_r": {
		"name": "Engine Platform (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": "turret_maintenance_room_r",
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "primary_generator",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"turret_maintenance_room_r": {
		"name": "Turret Maintenance Room (R)",
		"description": "",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": "engine_platform_r",
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"engineering_room": {
		"name": "Engineering Room",
		"description": "",
		"directions": {
			"north": "primary_generator",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"computer_core_chamber": {
		"name": "Computer Core Chamber",
		"description": "The Computer Core Chamber houses the CPU of the ship.\lDimly lit consoles and rows of servers fill the room.\lWires crisscross the floor, connecting the intricate machinery.\lFaint humming and blinking lights indicate the system's functionality.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "shield_generator_maintenance_room",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"shield_generator_maintenance_room": {
		"name": "Shield Generator Maintenance",
		"description": "The room is a spacious area for maintaining the ship's force field.\lThe walls are lined with control panels and diagnostic tools.\lA large generator stands at the center, emitting a gentle hum.\lTechnicians in protective suits occasionally work on the equipment.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "miscellaneous_storage_room",
			"south": "landing_gear_maintenance_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "computer_core_chamber",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"miscellaneous_storage_room": {
		"name": "Miscellaneous Storage Room",
		"description": "The room serves as a broad space for various supplies and equipment.\lMetal shelves line the walls, holding an array of labeled containers.\lDust-covered boxes and forgotten tools are scattered around.\lThe room is chaotic, with each item in a random place on the shelf.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "cargo_bay_r_2",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "shield_generator_maintenance_room",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"landing_gear_maintenance_room": {
		"name": "Landing Gear Maintenance Room",
		"description": "The room is where the ship's landing gear is repaired and maintained.\lTools and spare parts are chaotically arranged on workbenches.\lThe Hydraulic systems seem to need adjusting.\lThe sound of clanking metal and hissing air fills the air.",
		"directions": {
			"north": "shield_generator_maintenance_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "repulser_lift_maintenance_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"repulser_lift_maintenance_room": {
		"name": "Repulser Lift Maintenance",
		"description": "The entire Bay is dedicated to the upkeep of the repulser lift system.\lHeavy machinery and maintenance platforms dominate the space.\lSome of the repulsers are in dire need of repair.\lThe room echoes with the whirring of engines and metallic clattering.",
		"directions": {
			"north": "landing_gear_maintenance_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "cargo_bay_r_1",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "cargo_bay_l_1",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"cargo_bay_l_1": {
		"name": "Cargo Bay (L) [1]",
		"description": "The left Cargo Bay is a vast storage area for the ship's cargo.\lStacked crates and containers create a maze-like arrangement.\lThe air is filled with a faint scent of metal and plastic.\lLoading docks and robotic arms are positioned along the walls.",
		"directions": {
			"north": "cargo_bay_l_2",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "repulser_lift_maintenance_room",
			"south": "dry_storage_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"cargo_bay_l_2": {
		"name": "Cargo Bay (L) [2]",
		"description": "The second left Cargo Bay is an extension of the left cargo storage.\lIt shares the same chaotic organisation as the previous bay.\lThis room contains extra shelving units and storage areas.\lThe room is illuminated by bright overhead lights.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "cargo_bay_l_1",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"cargo_bay_r_1": {
		"name": "Cargo Bay (R) [1]",
		"description": "The right Cargo Bay mirrors its counterpart on the ship's left side.\lIt is filled with stacked cargo containers awaiting transportation.\lConveyor belts and automated systems facilitate the movement of goods.\lThe flicker of warning lights creates urgency in the atmosphere.",
		"directions": {
			"north": "cargo_bay_r_2",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "cold_storage_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": "spacecraft_storage_room_2",
			"west": "repulser_lift_maintenance_room",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"cargo_bay_r_2": {
		"name": "Cargo Bay (R) [2]",
		"description": "The right secondary Cargo Bay is an annex to it's counterpart.\lIt continues the pattern of disorder, housing additional supplies.\lThe room is well-lit, casting tall shadows on the messy floor.\lThe bright light makes navigation through the maze-like stacks easier.",
		"directions": {
			"north": "miscellaneous_storage_room",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "cargo_bay_r_1",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"dry_storage_room": {
		"name": "Dry Storage Room",
		"description": "The room is a secure area for storing non-perishable provisions.\lShelves filled with sealed containers and vacuum-sealed bags lay still.\lThe air is dry, preserving the long shelf life of the stored goods.\lA faint aroma of preserved food lingers in the room.",
		"directions": {
			"north": "cargo_bay_l_1",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"cold_storage_room": {
		"name": "Cold Storage Room",
		"description": "The room is a frigid chamber designed to preserve perishable items.\lShelves hold containers of frozen provisions and scientific samples.\lThe frost filled air accentuates the room's purpose.\lSoft white lights cast an ethereal glow on the icy surfaces.",
		"directions": {
			"north": "cargo_bay_r_1",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"spacecraft_storage_room_1": {
		"name": "Spacecraft Storage [1]",
		"description": "The Spacecraft Storage chamber houses the smaller space vehicles.\lThe room exudes an atmosphere of controlled chaos.\lSpacecrafts of various sizes sit neatly arranged in designated spaces.\lThe grandeur room's scent hints towards past interstellar explorations.",
		"directions": {
			"north": "spacecraft_storage_room_2",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "vehicle_storage_bay",
			"south": "hyperdrive_control_room",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "airlock_chamber",
			"up": "secondary_bridge",
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"spacecraft_storage_room_2": {
		"name": "Spacecraft Storage [2]",
		"description": "The primary storage extension accommodates additional space vehicles.\lThe room is arranged in a way that maximizes the available space.\lDim lighting highlights the formidable forms of the dormant ships.\lThe room holds an anticipation for future interstellar ventures.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": "cargo_bay_r_1",
			"north_west": "cargo_bay_r_1",
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": "spacecraft_storage_room_1",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"airlock_chamber": {
		"name": "Airlock Chamber",
		"description": "The controlled environment of the ship links with the void of space.\lSealed doors and pressure systems ensure the integrity of the vessel.\lThe chamber features a decontamination area, with ultraviolet lights.\lDisinfectant sprays sit there, ready to cleanse any potential hazards.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "spacecraft_storage_room_1",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"vehicle_storage_bay": {
		"name": "Vehicle Storage Bay",
		"description": "The bay is a small room to house the ship's ground-based vehicles.\lA large seal, placed on the wall to prevent space from consuming you.\lTools and parts are meticulously hung in disarray along the walls.\lThe air carries a faint scent of engine oil, polluting the room.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "spacecraft_storage_room_1",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"engine_mechanics_room_l": {
		"name": "Engine Mechanics Room (L)",
		"description": "The room houses the machinery that propels the ship through space.\lThe room hums with quiet energy, housing a network of pipes and valves.\lSoft lighting illuminates the mechanical wonders.\lThe room is scarred from the immense power held in the engines.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "hyperdrive_control_room",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"engine_mechanics_room_r": {
		"name": "Engine Mechanics Room (R)",
		"description": "The room houses the machinery responsible for the ship's propulsion.\lThe room is filled with intricate gauges and humming conduits.\lIlluminated consoles display critical engine diagnostics and warnings.\lThe walls reverberate with the vibrations of the ship's engines.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "hyperdrive_control_room",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"hyperdrive_control_room": {
		"name": "Hyperdrive Control Room",
		"description": "The room serves as the nerve center for the ship's propulsion system.\lA complex array of controls and monitors are meticulously arranged.\lSoft blue lighting bathes the room in a calming glow.\lEach button press brings the ship closer to traversing space.",
		"directions": {
			"north": "spacecraft_storage_room_1",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "engine_mechanics_room_r",
			"south": "secondary_power_core_chamber",
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "engine_mechanics_room_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"secondary_power_core_chamber": {
		"name": "Secondary Power Core Chamber",
		"description": "The chamber houses a backup energy source incase the primary one fails.\lThe secondary power core augments the ship's primary power systems.\lWithin this chamber, a towering generator hums with contained power.\lThe rhythmic pulsation of energy creates an almost palpable presence.",
		"directions": {
			"north": "engine_mechanics_room_r",
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "repulser_lift_r",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "repulser_lift_l",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"repulser_lift_l": {
		"name": "Repulser Lift (L)",
		"description": "The lift is a vertical transport system for moving cargo around.\lA low hum fills the air, accompanied by a gentle breeze.\lThe lift's interior is spacious, terminals indicate it's current level.\lThe lift vibrates as it moves through the ship's structural framework.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": "secondary_power_core_chamber",
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": {
				"location": None,
				"move_direction": None
			},
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
	"repulser_lift_r": {
		"name": "Repulser Lift R",
		"description": "The lift provides efficient vertical transportation within the ship.\lMetal can be heard scraping the walls as pistons move about.\lThe lift filled with broken control panels displaying the it's status.\lThe lift once connected the various realms of the spacecraft.",
		"directions": {
			"north": {
				"location": None,
				"move_direction": None
			},
			"north_east": {
				"location": None,
				"move_direction": None
			},
			"north_west": {
				"location": None,
				"move_direction": None
			},
			"east": {
				"location": None,
				"move_direction": None
			},
			"south": {
				"location": None,
				"move_direction": None
			},
			"south_east": {
				"location": None,
				"move_direction": None
			},
			"south_west": {
				"location": None,
				"move_direction": None
			},
			"west": "secondary_power_core_chamber",
			"up": {
				"location": None,
				"move_direction": None
			},
			"down": {
				"location": None,
				"move_direction": None
			}
		},
		"objects": [],
		"entities": [],
	},
}