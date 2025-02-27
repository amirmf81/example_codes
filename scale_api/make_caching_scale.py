def make_caching_scale_func(speed_scale, acceleration_scale, location_scale):
    ans = {
        "speed_scale": speed_scale,
        "acceleration_scale": acceleration_scale,
        "location_scale": location_scale,
    }
    return str(ans)
