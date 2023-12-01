import subprocess
import os
import sys

from multiprocessing.dummy import Pool

config = sys.argv[1]
iterations = int(sys.argv[2])
parallel = int(sys.argv[3])

projects = {
    "./benchmark/commanderjs": {
        "analysis": "./benchmark/commanderjs/lib/**/*.js",
        "files": [
            "./benchmark/commanderjs/lib/argument.js",
            "./benchmark/commanderjs/lib/help.js",
            "./benchmark/commanderjs/lib/option.js",
            "./benchmark/commanderjs/lib/suggestSimilar.js"
        ]
    },
    "./benchmark/express": {
        "analysis": "./benchmark/express/lib/**/*.js",
        "files": [
            "./benchmark/express/lib/application.js",
            "./benchmark/express/lib/middleware/init.js",
            "./benchmark/express/lib/middleware/query.js",
            "./benchmark/express/lib/request.js",
            "./benchmark/express/lib/response.js",
            "./benchmark/express/lib/router/index.js",
            "./benchmark/express/lib/router/route.js",
            "./benchmark/express/lib/utils.js",
            "./benchmark/express/lib/view.js"
        ]
    },
    "./benchmark/javascript-algorithms": {
        "analysis": "./benchmark/javascript-algorithms/src/**/*.js",
        "files": [
            "./benchmark/javascript-algorithms/src/algorithms/cryptography/hill-cipher/hillCipher.js",
            "./benchmark/javascript-algorithms/src/algorithms/cryptography/rail-fence-cipher/railFenceCipher.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/articulation-points/articulationPoints.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/bellman-ford/bellmanFord.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/travelling-salesman/bfTravellingSalesman.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/breadth-first-search/breadthFirstSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/depth-first-search/depthFirstSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/detect-cycle/detectDirectedCycle.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/detect-cycle/detectUndirectedCycle.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/dijkstra/dijkstra.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/eulerian-path/eulerianPath.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/floyd-warshall/floydWarshall.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/hamiltonian-cycle/hamiltonianCycle.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/kruskal/kruskal.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/prim/prim.js",
            "./benchmark/javascript-algorithms/src/algorithms/graph/strongly-connected-components/stronglyConnectedComponents.js",
            "./benchmark/javascript-algorithms/src/algorithms/image-processing/seam-carving/resizeImageWidth.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/complex-number/ComplexNumber.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/euclidean-algorithm/euclideanAlgorithmIterative.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/fourier-transform/fastFourierTransform.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/integer-partition/integerPartition.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/matrix/Matrix.js",
            "./benchmark/javascript-algorithms/src/algorithms/math/primality-test/trialDivision.js",
            "./benchmark/javascript-algorithms/src/algorithms/ml/k-means/kMeans.js",
            "./benchmark/javascript-algorithms/src/algorithms/ml/knn/kNN.js",
            "./benchmark/javascript-algorithms/src/algorithms/search/interpolation-search/interpolationSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/search/jump-search/jumpSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/cartesian-product/cartesianProduct.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/knapsack-problem/Knapsack.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/knapsack-problem/KnapsackItem.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/longest-increasing-subsequence/dpLongestIncreasingSubsequence.js",
            "./benchmark/javascript-algorithms/src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js",
            "./benchmark/javascript-algorithms/src/algorithms/sorting/counting-sort/CountingSort.js",
            "./benchmark/javascript-algorithms/src/algorithms/sorting/radix-sort/RadixSort.js",
            "./benchmark/javascript-algorithms/src/algorithms/statistics/weighted-random/weightedRandom.js",
            "./benchmark/javascript-algorithms/src/algorithms/string/knuth-morris-pratt/knuthMorrisPratt.js",
            "./benchmark/javascript-algorithms/src/algorithms/string/levenshtein-distance/levenshteinDistance.js",
            "./benchmark/javascript-algorithms/src/algorithms/string/longest-common-substring/longestCommonSubstring.js",
            "./benchmark/javascript-algorithms/src/algorithms/string/regular-expression-matching/regularExpressionMatching.js",
            "./benchmark/javascript-algorithms/src/algorithms/string/z-algorithm/zAlgorithm.js",
            "./benchmark/javascript-algorithms/src/algorithms/tree/breadth-first-search/breadthFirstSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/tree/depth-first-search/depthFirstSearch.js",
            "./benchmark/javascript-algorithms/src/algorithms/uncategorized/jump-game/dpTopDownJumpGame.js",
            "./benchmark/javascript-algorithms/src/algorithms/uncategorized/knight-tour/knightTour.js",
            "./benchmark/javascript-algorithms/src/algorithms/uncategorized/n-queens/nQueens.js",
            "./benchmark/javascript-algorithms/src/algorithms/uncategorized/unique-paths/dpUniquePaths.js",
            "./benchmark/javascript-algorithms/src/data-structures/bloom-filter/BloomFilter.js",
            "./benchmark/javascript-algorithms/src/data-structures/disjoint-set/DisjointSet.js",
            "./benchmark/javascript-algorithms/src/data-structures/doubly-linked-list/DoublyLinkedList.js",
            "./benchmark/javascript-algorithms/src/data-structures/graph/Graph.js",
            "./benchmark/javascript-algorithms/src/data-structures/linked-list/LinkedList.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/avl-tree/AvlTree.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/BinaryTreeNode.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/fenwick-tree/FenwickTree.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/red-black-tree/RedBlackTree.js",
            "./benchmark/javascript-algorithms/src/data-structures/tree/segment-tree/SegmentTree.js",
            "./benchmark/javascript-algorithms/src/data-structures/trie/Trie.js",
            "./benchmark/javascript-algorithms/src/data-structures/trie/TrieNode.js",
            "./benchmark/javascript-algorithms/src/utils/comparator/Comparator.js"
        ]
    },
    "./benchmark/lodash": {
        "analysis": "./benchmark/lodash/**/*.js",
        "files": [
            "./benchmark/lodash/.internal/equalArrays.js",
            "./benchmark/lodash/hasPath.js",
            "./benchmark/lodash/random.js",
            "./benchmark/lodash/result.js",
            "./benchmark/lodash/slice.js",
            "./benchmark/lodash/split.js",
            "./benchmark/lodash/toNumber.js",
            "./benchmark/lodash/transform.js",
            "./benchmark/lodash/truncate.js",
            "./benchmark/lodash/unzip.js"
        ]
    },
    "./benchmark/artificial": {
        "analysis": "./benchmark/artificial/**/*.js",
        "files": [
            "./benchmark/artificial/findSpecificStringProblem.js",
            "./benchmark/artificial/narrowConditionProblem.js",
            "./benchmark/artificial/performOperationProblem.js",
            "./benchmark/artificial/triangleProblem.js",
        ]
    },
    "./benchmark/moment": {
        "analysis": "./benchmark/moment/src/**/*.js",
        "files": [
            "./benchmark/moment/src/lib/moment/add-subtract.js",
            "./benchmark/moment/src/lib/moment/calendar.js",
            "./benchmark/moment/src/lib/create/check-overflow.js",
            "./benchmark/moment/src/lib/moment/compare.js",
            "./benchmark/moment/src/lib/moment/constructor.js",
            "./benchmark/moment/src/lib/create/date-from-array.js",
            "./benchmark/moment/src/lib/moment/format.js",
            "./benchmark/moment/src/lib/create/from-anything.js",
            "./benchmark/moment/src/lib/create/from-array.js",
            "./benchmark/moment/src/lib/create/from-object.js",
            "./benchmark/moment/src/lib/create/from-string-and-array.js",
            "./benchmark/moment/src/lib/create/from-string-and-format.js",
            "./benchmark/moment/src/lib/create/from-string.js",
            "./benchmark/moment/src/lib/moment/get-set.js",
            "./benchmark/moment/src/lib/create/local.js",
            "./benchmark/moment/src/lib/moment/min-max.js",
            "./benchmark/moment/src/lib/moment/now.js",
            "./benchmark/moment/src/lib/create/parsing-flags.js",
            "./benchmark/moment/src/lib/moment/start-end-of.js",
            "./benchmark/moment/src/lib/create/valid.js"
        ]
    },
    "./benchmark/numbers.js": {
        "analysis": "./benchmark/numbers.js/lib/**/*.js",
        "files": [
                "./benchmark/numbers.js/lib/numbers/basic.js"
        ]
    }
}

presets = [
    "random",
    # "NSGAII",
#    "MOSA",
    "DynaMOSA"
#    "SPEAII",
#    "MOSASPEAII",
#    "DynaMOSASPEAII"
#    "SPEA2",
#    "DynaMOSASPEA2",
#    "DynaMOSASPEA2",
#    "DynaMOSASPEA2Highest",
#    "DynaMOSASPEA2Sum",
    # "DynaMOSA-no-type",
    # "DynaMOSA-prob",
    # "DynaMOSA-prob-all",
    # "DynaMOSA-prob-dyn",
    # "DynaMOSA-prob-pool",
    # "DynaMOSA-ranked",
    # "DynaMOSA-ranked-all",
    # "DynaMOSA-ranked-dyn",
    # "DynaMOSA-ranked-pool"
    ]
    
configurations = []
    
index = 1
for iteration in range(iterations):
    for preset in presets:
        for project in projects.keys():
            files = projects[project]['files']
            analysis = projects[project]['analysis']
            for filepath in files:
                name = "syntest-{}-{}".format(config, index)
                configurations.append((name, iteration, preset, project, analysis, filepath))
                index = index + 1

def call_script(args):
    (name, iteration, preset, project, analysis, filepath) = args
    command = "docker run -it --name {} -e target_root_directory='{}' -e target_include='{}' -e analysis_include='{}' -e preset='{}' -e time=180 syntest-{}".format(name, project, filepath, analysis, preset, config)
    print("Starting command with configuration: {} {} {} {} {}".format(name, iteration, preset, project, filepath))
    result = subprocess.call(command, shell=True)
    print("Completed command with configuration: {} {} {} {} {}".format(name, iteration, preset, project, filepath))
    return result

with Pool(parallel) as p:
    exit_codes = p.map(call_script, configurations)
    print("Exit codes : {}".format(exit_codes))
    
#subprocess.check_output(['docker', 'run', '-d', '-v', "${PWD}/experiment/runs/" + runs_directories[i] + ':/app/syntest-solidity-benchmark', '-v', '${PWD}/node_modules:/app/syntest-solidity-benchmark/node_modu
