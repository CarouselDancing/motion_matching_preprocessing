
DEFAULT_DENSITY = 1000#0.5
SIM_SETTINGS = dict()
SIM_SETTINGS["auto_disable"] = False
SIM_SETTINGS["ground_friction"] = 0.1
SIM_SETTINGS["error_correction"] = 0.5# 0.2
SIM_SETTINGS["surface_layer_depth"] =0.01# 0.000001# 
SIM_SETTINGS["ground_penalty"] = 0.0001#0.8#  
SIM_SETTINGS["ground_softness"] = 0.0002

SIM_SETTINGS["n_steps_per_segment"] = 6# 10 # this matters
SIM_SETTINGS["dt"] = 1/500# 1/200 # (1./30)/SIM_SETTINGS["n_steps_per_segment"]
SIM_SETTINGS["save_state_id"] = 50
SIM_SETTINGS["n_segments"] = SIM_SETTINGS["n_steps_per_segment"] 
SIM_SETTINGS["random_seed"] = 0
SIM_SETTINGS["control_mode"] = 0
    