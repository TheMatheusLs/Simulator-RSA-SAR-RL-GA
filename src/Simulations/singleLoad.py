
import time

from Enviroment.Manager import Enviroment
from Enviroment.Settings import *
    
def single_load(load: float, k_routes: int, number_of_slots: int, alg_heuristic: int, seed: int = 42) -> (float, float):
    """
    Simulates a single load in the network. 

    Parameters:
        - load: Network load in Erlangs.
        - k_routes: Number of routes to be considered.
        - number_of_slots: Number of slots in the network.
        - alg_heuristic: Heuristic to be used. 0 for RSA, 1 for SAR and 2 for MSCL.

    Returns:
        - (blocking_probability, simulation_time): A tuple containing the blocking probability and the simulation time.
    """


    # Cria o ambiente de simulação
    env = Enviroment(network_load = load, k_routes = k_routes, number_of_slots = number_of_slots)

    # Reseta o ambiente
    state, _ = env.reset(seed)

    # Inicia a contagem de tempo
    start_time = time.time()

    blocking = 0
    for _ in range(MAX_REQS):

        _, reward, _, _, info = env.step(alg_heuristic)

        if info["is_blocked"]:
            blocking += 1

    return blocking / MAX_REQS, time.time() - start_time