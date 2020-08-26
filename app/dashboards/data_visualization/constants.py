MEDIA_DF_PATH = "./app/media/dataframes"

MEDIA_REPORT_PATH = "./app/media/reports"

ANOMALY_THRESHOLDS = {
    "Pressure": [11.5, 12.5],
    "GasFlowSpeed": [19.5, 20.5],
    "Oxygen1": [-0.1, 0.1],
    "Oxygen2": [-0.1, 0.1],
}

SLM280_COLUMNS = [
    "Time",
    "Platform",
    "Build Chamber",
    "Pump1",
    "Cabinet",
    "Cabinet 2",
    "Optical Bench",
    "Collimator",
    "Ambiance",
    "Dew point",
    "Oxygen 1",
    "Oxygen 2",
    "Pressure",
    "Filter Status",
    "T_LL",
    "T_LR",
    "T_U",
    "R_LL",
    "-",
    "-.1",
    "-.2",
    "R_LR",
    "R_U",
    "B_F",
    "B_R",
    "-.3",
    "Cyclone",
    "S_MAX",
    "S_MIN",
    "VSTG1",
    "VSTG2",
    "Gas Temp",
    "Gas flow speed",
    "MemTotal",
    "MemProcess",
    "Laser Emission Flags",
    "Laser On Flags",
    "Galvo X0",
    "Galvo Y0",
    "Galvo X1",
    "Galvo Y1",
]

SLM500_COLUMNS = [
    "Time",
    "Pressure",
    "Filter Status",
    "Gas flow speed",
    "Gas pump power",
    "Oxygen top",
    "Oxygen 2",
    "Gas Temp",
    "Platform",
    "Build Chamber",
    "Optical Bench",
    "Collimator",
    "T_U",
    "T_LL",
    "T_LR",
    "R_LL",
    "R_LR",
    "B_F",
    "B_R",
    "Pump",
    "Cabinet",
    "Cabinet 2",
    "Ambiance",
    "MemTotal",
    "MemProcess",
    "Laser Emission Flags",
    "Laser On Flags",
    "Galvo X0",
    "Galvo Y0",
    "Servo X0",
    "Servo Y0",
    "Optic1 Home-in X1",
    "Optic1 Home-in Y1",
    "Optic1 Home-in X2",
    "Optic1 Home-in Y2",
]

COLUMN_MAPPER = {
    "Gas Temp": "GasTemp",
    "Gas flow speed": "GasFlowSpeed",
    "Build Chamber": "BuildChamber",
    "Filter Status": "FilterStatus",
    "Optical Bench": "OpticalBench",
    "Oxygen top": "Oxygen1",
    "Oxygen 1": "Oxygen1",
    "Oxygen 2": "Oxygen2",
}

COLUMNS_TO_KEEP = [
    "Time",
    "Pressure",
    "GasTemp",
    "GasFlowSpeed",
    "BuildChamber",
    "FilterStatus",
    "OpticalBench",
    "Collimator",
    "Oxygen1",
    "Oxygen2",
]

DROPDOWN_OPTIONS = [
    {"label": "Pressure", "value": "Pressure"},
    {"label": "Gas Temperature", "value": "GasTemp"},
    {"label": "Gas Flow Speed", "value": "GasFlowSpeed"},
    {"label": "Build Chamber", "value": "BuildChamber"},
    {"label": "Filter Status", "value": "FilterStatus"},
    {"label": "Oxygen 1", "value": "Oxygen1"},
    {"label": "Oxygen 2", "value": "Oxygen2"},
    {"label": "Collimator", "value": "Collimator"},
    {"label": "Optical Bench", "value": "OpticalBench"},
]

TEMP_COLUMNS = ["Time", "MachineType", "NumDataPoints"]
