raw_id = "105"
raw_nickname = "Juggernaut"
raw_level = "30"
raw_kd = "1.42"
raw_online = "False"

player_id = int(raw_id)
nickname = str(raw_nickname)
level = int(raw_level)
kd = float(raw_kd)
is_online = raw_online == "True"

print(type(player_id))
print(type(nickname))
print(type(level))
print(type(kd))
print(type(is_online))