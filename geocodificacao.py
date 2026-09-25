# Nominatim, que trabalha com dados do OpenStreetMap.
# Da biblioteca geopy, dentro dos geocodificadores, quero utilizar o Nominatim.
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(
    user_agent = "tcc_mclp_nova_iguacu",
    timeout = 10
)

geocode = RateLimiter(
    geolocator.geocode,
    min_delay_seconds = 1,
    max_retries = 2,
    error_wait_seconds = 5
)

def buscar_coordenadas(logradouro, bairro):
    endereco = (
        f"{logradouro}, "
        f"{bairro}, "
        f"Nova Iguaçu, Rio de Janeiro, Brasil"
    )

    print(f"  Tentando: {endereco}")

    localizacao = geocode(
        endereco,
        country_codes="br",
        exactly_one=True,
        addressdetails=True
    )

    if localizacao is None:
        print("  Não encontrado")
        return None, None, None

    print(f"  Encontrado: {localizacao.address}")

    return (
        localizacao.latitude,
        localizacao.longitude,
        localizacao.address
    )

def geocodificar_pontos(pontos):
    for ponto in pontos:
        latitude, longitude, endereco_encontrado = buscar_coordenadas(
            ponto["logradouro"],
            ponto["bairro"]
        )

        ponto["latitude"] = latitude
        ponto["longitude"] = longitude
        ponto["endereco_encontrado"] = endereco_encontrado

        print(
            ponto["id"],
            latitude,
            longitude
        )

    return pontos