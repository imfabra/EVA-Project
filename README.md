# Capa de Comunicacion de app con robot

``` Python3
def mov_robot(angles, velocity):

    max_angle = max(angles)

    if isinstance(velocity, int):
        velocity = [velocity] * len(angles)

    speeds = [int(round(v * angle / max_angle)) for angle, v in zip(angles, velocity)]

    print(angles, speeds)
```
