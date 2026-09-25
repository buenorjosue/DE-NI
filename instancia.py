def ler_instancia(caminho):
    pontos = []

    # Abrindo o arquivo 
    with open(caminho, "r", encoding="utf-8") as arquivo:


        quantidade = int(arquivo.readline().strip())

        cabecalho = arquivo.readline().strip().split("|")

        for linha in arquivo:
            if not linha.strip():
                continue

            valores = linha.strip().split("|")

            ponto = dict(zip(cabecalho, valores))

            ponto["impacto"] = int(ponto["impacto"])
            ponto["criticidade"] = int(ponto["criticidade"])
            ponto["custo"] = float(ponto["custo"])

            pontos.append(ponto)

    return quantidade, pontos