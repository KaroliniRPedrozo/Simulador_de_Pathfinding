import heapq

NUM_DISCOS = 3

class EstadoHanoi:
    def __init__(self, pinos, pai=None, acao="", g=0):
        self.pinos = pinos 
        self.pai = pai
        self.acao = acao
        
        # g(n): Custo real do caminho até este estado [cite: 656]
        self.g = g
        # h(n): Estimativa heurística (discos fora do pino objetivo) [cite: 657]
        self.h = len(self.pinos[0]) + len(self.pinos[1])
        # f(n): Função de avaliação f(n) = g(n) + h(n) [cite: 658]
        self.f = self.g + self.h

    def __lt__(self, outro):
        return self.f < outro.f

    def __eq__(self, outro):
        return self.pinos == outro.pinos

    def __hash__(self):
        return hash(self.pinos)

def obter_sucessores(estado):
    sucessores = []
    for origem in range(3):
        for destino in range(3):
            if origem == destino:
                continue
            pino_origem = estado.pinos[origem]
            pino_destino = estado.pinos[destino]
            
            if pino_origem:
                disco_topo = pino_origem[-1]
                if not pino_destino or pino_destino[-1] > disco_topo:
                    novos_pinos = list(list(p) for p in estado.pinos)
                    novos_pinos[origem].pop()
                    novos_pinos[destino].append(disco_topo)
                    
                    novos_pinos = tuple(tuple(p) for p in novos_pinos)
                    acao = f"Mover Disco {disco_topo} para o Pino {destino + 1}"
                    sucessores.append(EstadoHanoi(novos_pinos, estado, acao, estado.g + 1))
    return sucessores

def resolver_hanoi_com_metricas():
    pino_inicial = tuple(range(NUM_DISCOS, 0, -1))
    inicial = EstadoHanoi((pino_inicial, (), ()), acao="Estado Inicial")
    objetivo_pinos = ((), (), pino_inicial)
    
    fronteira = []
    heapq.heappush(fronteira, inicial)
    explorados = set()
    
    # Métricas de Desempenho
    nos_expandidos = 0
    pico_memoria = 1

    while fronteira:
        if len(fronteira) > pico_memoria:
            pico_memoria = len(fronteira)
            
        atual = heapq.heappop(fronteira)
        nos_expandidos += 1

        if atual.pinos == objetivo_pinos:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = atual.pai
            return caminho[::-1], nos_expandidos, pico_memoria

        explorados.add(atual)

        for sucessor in obter_sucessores(atual):
            if sucessor not in explorados:
                heapq.heappush(fronteira, sucessor)

    return None, nos_expandidos, pico_memoria

# --- Execução ---
solucao, nos_exp, pico_mem = resolver_hanoi_com_metricas()

print("--- RESULTADOS PARA O FRONT-END ---")
print(f"Nós Expandidos: {nos_exp}")
print(f"Pico de Memória na Fronteira: {pico_mem}")
print("\nArray JavaScript (copie e cole no JS):")

js_array = "[\n"
for i in range(1, len(solucao)):
    passo = solucao[i]
    # Descobre de onde o disco saiu e para onde foi comparando com o passo anterior
    for p_idx in range(3):
        if len(passo.pinos[p_idx]) > len(solucao[i-1].pinos[p_idx]):
            dest = p_idx
        elif len(passo.pinos[p_idx]) < len(solucao[i-1].pinos[p_idx]):
            orig = p_idx
            
    js_array += f"    {{ orig: {orig}, dest: {dest}, g: {passo.g}, h: {passo.h}, f: {passo.f}, desc: '{passo.acao}' }},\n"
js_array += "]"
print(js_array)