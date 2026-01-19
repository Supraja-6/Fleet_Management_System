import os

def test_save_and_load_json(ecoride):
    ecoride.save_to_json()
    assert os.path.exists("fleet_data.json")

    new_ecoride = ecoride.__class__()
    new_ecoride.load_from_json()

    assert len(new_ecoride.hubs["Bangalore"]) == 3
