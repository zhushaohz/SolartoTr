import solartotr

i_dir = solartotr.get_i_dir()
tr = solartotr.solar_to_tr(i_dir=i_dir, ta=30, b=0, sharp=120)
print(tr)
