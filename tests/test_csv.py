import os

def test_save_and_load_csv(ecoride):
    ecoride.save_to_csv()
    assert os.path.exists("fleet_data.csv")

    new_ecoride = ecoride.__class__()
    new_ecoride.load_from_csv()

    assert "Bangalore" in new_ecoride.hubs
    assert len(new_ecoride.hubs["Bangalore"]) == 3
