import subprocess
import os

from multiprocessing.dummy import Pool

projects = {
    "./benchmark/commanderjs": [
        "./benchmark/commanderjs/lib/help.js",
        "./benchmark/commanderjs/lib/option.js",
        "./benchmark/commanderjs/lib/suggestSimilar.js"
        ],
    "./benchmark/express": [
        # "./benchmark/express/lib/application.js",
        "./benchmark/express/lib/middleware/query.js",
        "./benchmark/express/lib/request.js",
        "./benchmark/express/lib/response.js",
        "./benchmark/express/lib/utils.js",
        "./benchmark/express/lib/view.js"
        ],
    "./benchmark/javascript-algorithms": [
        "./benchmark/javascript-algorithms/src/algorithms/graph/articulation-points/articulationPoints.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/bellman-ford/bellmanFord.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/travelling-salesman/bfTravellingSalesman.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/breadth-first-search/breadthFirstSearch.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/depth-first-search/depthFirstSearch.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/detect-cycle/detectDirectedCycle.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/detect-cycle/detectUndirectedCycle.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/dijkstra/dijktra.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/eulerian-path/eulerianPath.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/floyd-warshall/floydWarshall.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/hamiltonian-cycle/hamiltonianCycle.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/kruskal/kruskal.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/prim/prim.js",
        "./benchmark/javascript-algorithms/src/algorithms/graph/strongly-connected-components/stronglyConnectedComponents.js",
        "./benchmark/javascript-algorithms/src/algorithms/sets/knapsack-problem/Knapsack.js",
        "./benchmark/javascript-algorithms/src/algorithms/sets/knapsack-problem/KnapsackItem.js",
        "./benchmark/javascript-algorithms/src/algorithms/math/matrix/Matrix.js",
        "./benchmark/javascript-algorithms/src/algorithms/sorting/counting-sort/CountingSort.js",
        "./benchmark/javascript-algorithms/src/data-structures/tree/red-black-tree/RedBlackTree.js"
        ],
    "./benchmark/lodash": [
        "./benchmark/lodash/.internal/equalArrays.js",
        "./benchmark/lodash/hasPath.js",
        "./benchmark/lodash/random.js",
        "./benchmark/lodash/results.js",
        "./benchmark/lodash/slice.js",
        "./benchmark/lodash/split.js",
        "./benchmark/lodash/toNumber.js",
        "./benchmark/lodash/transform.js",
        "./benchmark/lodash/truncate.js",
        "./benchmark/lodash/unzip.js"
        ]
    # "./benchmark/moment": [
    #     "./benchmark/moment/src/lib/moment/add-subtract.js",
    #     "./benchmark/moment/src/lib/moment/calendar.js",
    #     "./benchmark/moment/src/lib/create/check-overflow.js",
    #     "./benchmark/moment/src/lib/moment/compare.js",
    #     "./benchmark/moment/src/lib/moment/constructor.js",
    #     "./benchmark/moment/src/lib/create/date-from-array.js",
    #     "./benchmark/moment/src/lib/moment/format.js",
    #     "./benchmark/moment/src/lib/create/from-anything.js",
    #     "./benchmark/moment/src/lib/create/from-array.js",
    #     "./benchmark/moment/src/lib/create/from-object.js",
    #     "./benchmark/moment/src/lib/create/from-string-and-array.js",
    #     "./benchmark/moment/src/lib/create/from-string-and-format.js",
    #     "./benchmark/moment/src/lib/create/from-string.js",
    #     "./benchmark/moment/src/lib/moment/get-set.js",
    #     "./benchmark/moment/src/lib/create/locale.js",
    #     "./benchmark/moment/src/lib/moment/min-max.js",
    #     "./benchmark/moment/src/lib/moment/now.js",
    #     "./benchmark/moment/src/lib/create/parsing-flags.js",
    #     "./benchmark/moment/src/lib/moment/start-end-of.js",
    #     "./benchmark/moment/src/lib/create/valid.js"
    #     ]
}

presets = [
    "NSGAII",
    "MOSA",
    "DynaMOSA"
    ]
    
configurations = []
    
index = 1
for preset in presets:
    for project, files in projects.items():
        for filepath in files:
            name = "syntest-{}".format(index)
            configurations.append((name, preset, project, filepath))
            index = index + 1

def call_script(args):
    (name, preset, project, filepath) = args
    command = "timeout -k 5m 5m  docker run -it --name {} -e target_root_directory={} -e include={} -e preset={} syntest-brp-2023-base".format(name, project, filepath, preset)
    print("Starting command with configuration: {} {} {} {}".format(name, preset, project, filepath))
    result = subprocess.call(command, shell=True)
    print("Completed command with configuration: {} {} {} {}".format(name, preset, project, filepath))
    return result

with Pool(5) as p:
    exit_codes = p.map(call_script, configurations)
    print("Exit codes : {}".format(exit_codes))
    
#subprocess.check_output(['docker', 'run', '-d', '-v', "${PWD}/experiment/runs/" + runs_directories[i] + ':/app/syntest-solidity-benchmark', '-v', '${PWD}/node_modules:/app/syntest-solidity-benchmark/node_modu
